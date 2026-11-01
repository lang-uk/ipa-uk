"""Generate tests/test_phonemizations.py from tests/phonemizations.txt.

Data file format:

    # comment                  -> comment above the generated `def` (module level)
    | <test_name>              -> def test_<test_name>():
    # comment                  -> a comment placed inside the test body
    <source> <accent> <ipa>    -> assert ipa("<source>", check_accent=...) == "<ipa>"

A `#` line directly above a `|` line is emitted as a module-level comment just
above the generated `def`; any other `#` line is emitted inside the test body.

In a case line the keyword column is either ``accent`` (check_accent=True) or
``noaccent`` (check_accent=False). Columns are separated by runs of whitespace,
so sources/outputs may be aligned freely; neither keyword ever appears inside a
Cyrillic source or an IPA output, so the first keyword marks the split.
"""

import re
import sys

CASE_RE = re.compile(r"^(.*?)\s+(accent|noaccent)\s+(.+)$")


def parse(text):
    blocks = []
    body = None
    pending = []  # comments not yet bound to a `def` or a test body
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("|"):
            body = []
            # comments directly above a `|` go above the `def`
            blocks.append((line[1:].strip(), list(pending), body))
            pending = []
        elif line.startswith("#"):
            pending.append(line[1:].strip())
        else:
            m = CASE_RE.match(line)
            if not m:
                raise ValueError(f"cannot parse line: {raw!r}")
            # comments between cases stay inside the body
            body.extend(("comment", c) for c in pending)
            pending = []
            body.append(("case", m.group(1).strip(), m.group(2), m.group(3)))
    return blocks


def render(blocks):
    lines = ["from ipa_uk import pronunciation as ipa", "", ""]
    for name, leading, items in blocks:
        for comment in leading:
            lines.append(f"# {comment}")
        lines.append(f"def test_{name}():")
        for item in items:
            if item[0] == "comment":
                lines.append(f"    # {item[1]}")
            else:
                _, src, kw, out = item
                flag = "True" if kw == "accent" else "False"
                lines.append(
                    f'    assert ipa("{src}", check_accent={flag}) == "{out}"'
                )
        lines.extend(("", ""))
    return "\n".join(lines).rstrip("\n") + "\n"


def main():
    inp = sys.argv[1] if len(sys.argv) > 1 else "tests/phonemizations.txt"
    out = sys.argv[2] if len(sys.argv) > 2 else "tests/test_phonemizations.py"
    with open(inp, encoding="utf-8") as f:
        blocks = parse(f.read())
    with open(out, "w", encoding="utf-8") as f:
        f.write(render(blocks))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
