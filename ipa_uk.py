"""
This module provides a Python implementation of the IPA phonetic transcription algorithm found
on Wiktionary (https://uk.wiktionary.org/wiki/Модуль:uk-pron)

The module exposes one function `ipa` and two constants, `ACUTE` and `GRAVE`, so you can
add stresses to the words like this: f"Украї{acute}ні"

Where the дж/дз sequences denote two separate sounds instead of a single one, please indicate this by doubling
the second letter: pass віджжи́лий instead of віджи́лий, підззе́мний instead of підзе́мний, etc.
"""

import re
from collections import OrderedDict

__all__ = [
    'AccentIsMissing',
    'ACUTE',
    'GRAVE',
    'ipa',
]

ACUTE = chr(0x301)
GRAVE = chr(0x300)


class AccentIsMissing(ValueError):
    pass


def ipa(text: str, check_accent: bool) -> str:
    """
    Returns the IPA transcription of the given word or sentence according to the Wiktionary algorithm

    Parameters:
        text (str): the word or the sentence to transcribe
        check_accent (bool): enable mandatory verification for at least one stressed syllable
    Returns:
        phonetic (str): phonetic transcription
    """
    text = text.lower()

    if check_accent:
        if ACUTE not in text and GRAVE not in text:
            if len(re.findall(r"[аеєиіїоуюя]", text)) > 1:
                raise AccentIsMissing(
                    f"The provided text is missing an accent (and has more than one syllable). "
                    f"Set check_accent=False to disable that check"
                )

    palatalizable: str = r"[tdsznlrbpʋfɡmkɦxʃʒ]"
    voiced_obstruent: str = r"[bdzʒɡɦ]"
    vowel: str = r"[ɑɛiɪuɔɐoʊe]"
    consonant: str = r"[bdzʒɡɦmnlrpftskxʃʋ]"

    phonetic_chars_map: list[dict[str, str]] = [
        # 3-character sequences:
        {
            "дзь": "d͡zʲ",
            # dental plosives assimilate to the following hissing/hushing consonants,
            # which is not reflected in the spelling
            "тьс": "t͡sʲː",
        },
        # 2-character sequences:
        {
            "дж": "d͡ʒ",
            "дз": "d͡z",
            # dental plosives assimilate to the following hissing/hushing consonants,
            # which is not reflected in the spelling
            "дс": "d͡zs",
            "дш": "d͡ʒʃ",
            "дч": "d͡ʒt͡ʃ",
            "дц": "d͡zt͡s",
            "тс": "t͡s",
            "тш": "t͡ʃʃ",
            "тч": "t͡ʃː",
            "тц": "t͡sː",
        },
        # single characters:
        {
            "а": "ɑ",
            "б": "b",
            "в": "ʋ",
            "г": "ɦ",
            "ґ": "ɡ",
            "д": "d",
            "е": "ɛ",
            "є": "jɛ",
            "ж": "ʒ",
            "з": "z",
            "и": "ɪ",
            "і": "i",
            "ї": "ji",
            "й": "j",
            "к": "k",
            "л": "l",
            "м": "m",
            "н": "n",
            "о": "ɔ",
            "п": "p",
            "р": "r",
            "с": "s",
            "т": "t",
            "у": "u",
            "ф": "f",
            "х": "x",
            "ц": "t͡s",
            "ч": "t͡ʃ",
            "ш": "ʃ",
            "щ": "ʃt͡ʃ",
            "ь": "ʲ",
            "ю": "ju",
            "я": "jɑ",
            "’": "j",
            # stress marks:
            ACUTE: "ˈ",
            GRAVE: "ˈ",
        },
    ]
    orthographic_replacements: dict = {
        # first apply consonant cluster simplifications that always occur orthographically:
        r"нтськ": "ньськ",
        r"стськ": "ськ",
        r"нтст": "нст",
        r"стч": "шч",
        r"стд": "зд",
        r"стс": "сː",
        r"^зш": "шː",
        r"зш": "жш",
        r"^зч": "шч",
        r"зч": "жч",
        # then long consonants that are orthographically geminated:
        r"([бвгґд])\1": r"\1ː",
        r"([^д]+)жж": r"\1жː",  # джж denotes non-affricate дж
        r"([^д]+)зз": r"\1зː",  # дзз denotes non-affricate дз
        r"([йклмнпрстфхцчшщ])\1": r"\1ː",
        r"дждж": r"джː",
        r"дздз": r"дзː",
    }

    phonetic: str = text

    for regex, replacement in orthographic_replacements.items():
        phonetic = re.sub(regex, replacement, phonetic)

    # so that the character is not mixed up with the IPA stress mark
    phonetic = phonetic.replace("'", "!")

    for replacements in phonetic_chars_map:
        for key, replacement in replacements.items():
            phonetic = re.sub(key, replacement, phonetic)

    phonetic = re.sub(r"([ɑɛiɪuɔ])ˈ", r"ˈ\1", phonetic)

    # including stress mark for single-syllable words if check_accent is set to true
    number_of_vowels = len(re.findall(r"[ɑɛiɪuɔ]", phonetic))
    if number_of_vowels == 1 and check_accent:
        phonetic = re.sub(r"([ɑɛiɪuɔ])", r"ˈ\1", phonetic)

    # palatalizable consonants before /i/ or /j/ become palatalized
    phonetic = re.sub(r"(" + palatalizable + ")([ː]?)([ˈ]?)i", r"\1ʲ\2\3i", phonetic)
    phonetic = re.sub(r"(" + palatalizable + ")([ː]?)j", r"\1ʲ\2", phonetic)

    # eliminate garbage sequences of [ʲːj] resulting from the -тьс- cluster followed by [j]
    phonetic = re.sub(r"ʲːj", r"ʲː", phonetic)

    # -- Simplifying consonants: ст + ц' → [с'ц']. needed due to the palatalization.
    # -- There is also a rule т +ц → [цː]. According to «Орфоепічний словник», p. 13,
    # -- both forms are valid, with no lengthening in colloquial speech and with lengthening
    # -- in slow speech, hence ː is enclosed in brackets as optional.
    phonetic = re.sub(r"st͡sʲ([ː]?)", r"sʲt͡sʲ(\1)", phonetic)

    # assimilation: voiceless + voiced = voiced + voiced
    # should /ʋ/ be counted as voiced? According to «Орфоепічний словник»,
    # the assimilation doesn't apply to an initial шв (p. 116)
    voicing: tuple[tuple[str, str], ...] = (
        ("p", "b"),
        ("s", "z"),
        ("t͡sʲ", "d͡zʲ"),
        ("t", "d"),
        ("f", "v"),
        ("ʃt͡ʃ", "ʒd͡ʒ"), # віщба́
        ("x", "ɦ"),
        ("k", "ɡ"),
        ("ʃ", "ʒ"),
        ("tʲ", "dʲ"),
        ("sʲ", "zʲ"),
        ("t͡ʃ", "d͡ʒ"),
        ("t͡s", "d͡z"),
    )

    while True:
        prev_phonetic: str = phonetic
        for voiceless, voiced in voicing:
            phonetic = re.sub(voiceless + "(" + voiced_obstruent + "+)", voiced + r"\1", phonetic)

        # Till there is no more replacements
        if prev_phonetic == phonetic:
            break
        else:
            prev_phonetic = phonetic

    # In the sequence of two consonants, of which the second is soft, the first is pronounced soft too
    # unless the first consonant is a labial, namely б, п, в, ф, м.
    phonetic = re.sub(r"([tdsznl])(.)ʲ", r"\1ʲ\2ʲ", phonetic)
    phonetic = re.sub(r"([tdsznl])t͡sʲ", r"\1ʲt͡sʲ", phonetic)
    phonetic = re.sub(r"([tdsznl])d͡zʲ", r"\1ʲd͡zʲ", phonetic)
    phonetic = re.sub(r"t͡s(.)ʲ", r"t͡sʲ\1ʲ", phonetic)
    phonetic = re.sub(r"d͡z(.)ʲ", r"d͡zʲ\1ʲ", phonetic)
    phonetic = re.sub(r"d͡zt͡sʲ", r"d͡zʲt͡sʲ", phonetic)
    phonetic = re.sub(r"t͡sd͡zʲ", r"t͡sʲd͡zʲ", phonetic)

    # Hushing consonants ж, ч, ш assimilate to the following hissing consonants, giving a long hissing consonant:
    # [ʒ] + [t͡sʲ] → [zʲt͡sʲ], [t͡ʃ] + [t͡sʲ] → [t͡sʲː], [ʃ] + [t͡sʲ] → [sʲt͡sʲ], [ʃ] + [sʲ] → [sʲː]
    phonetic = re.sub(r"ʒt͡sʲ", r"zʲt͡sʲ", phonetic)
    phonetic = re.sub(r"t͡ʃt͡sʲ", r"t͡sʲː", phonetic)
    phonetic = re.sub(r"ʃt͡sʲ", r"sʲt͡sʲ", phonetic)
    phonetic = re.sub(r"ʃsʲ", r"sʲː", phonetic)

    # Hissing consonants before hushing consonants within a word assimilate - on зш and зч word-initially and
    # word-medially see above.
    # [s] + [ʃ] → [ʃː],  [z] + [ʃ] → [ʒʃ], [z] + [t͡s] → [ʒt͡s]
    # [z] + [d͡ʒ] → [ʒd͡ʒ]
    phonetic = re.sub(r"zʒ", r"ʒː", phonetic)
    phonetic = re.sub(r"sʃ", r"ʃː", phonetic)
    phonetic = re.sub(r"zt͡s", r"ʒt͡s", phonetic)
    phonetic = re.sub(r"zd͡ʒ", r"ʒd͡ʒ", phonetic)

    # cleanup: excessive palatalization: CʲCʲCʲ → CCʲCʲ
    phonetic = re.sub(r"([^ɑɛiɪuɔ]+)ʲ([^ɑɛiɪuɔ]+)ʲ([^ɑɛiɪuɔ]+)ʲ", r"\1\2ʲ\3ʲ", phonetic)

    # unstressed /ɑ/ has an allophone [ɐ]
    phonetic = re.sub(r"([^ˈ])ɑ", r"\1ɐ", phonetic)
    phonetic = re.sub(r"^ɑ", r"ɐ", phonetic)
    # unstressed /u/ has an allophone [ʊ]
    phonetic = re.sub(r"([^ˈ])u", r"\1ʊ", phonetic)
    phonetic = re.sub(r"^u", r"ʊ", phonetic)
    # unstressed /ɔ/ has by assimilation an allophone [o] before a stressed syllable with /u/ or /i/
    phonetic = re.sub(r"ɔ([bdzʒɡɦmnlrpftskxʲʃ͡]+)ˈ([uiʊ]+)", r"o\1ˈ\2", phonetic)
    # one allophone [e] covers unstressed /ɛ/ and /ɪ/
    phonetic = re.sub(r"([^ˈ])ɛ", r"\1e", phonetic)
    phonetic = re.sub(r"^ɛ", r"e", phonetic)
    phonetic = re.sub(r"([^ˈ])ɪ", r"\1e", phonetic)
    phonetic = re.sub(r"^ɪ", r"e", phonetic)

    # /ʋ/ has an allophone [u̯] in a syllable coda
    phonetic = re.sub(r"(" + vowel + "+)ʋ", r"\1u̯", phonetic)
    # /ʋ/ has an allophone [w] before /ɔ, u/and voiced consonants (not after a vowel)
    phonetic = re.sub(r"ʋ([ˈ]?)([ɔuoʊbdzʒɡɦmnlr]+)", r"w\1\2", phonetic)
    # /ʋ/ has an allophone [ʍ] before voiceless consonants (not after a vowel)
    phonetic = re.sub(r"ʋ([pftskxʃ]+)", r"ʍ\1", phonetic)

    # in a syllable-final position (i.e. the first position of a syllable coda) /j/ has an allophone [i̯]:
    phonetic = re.sub(r"(" + vowel + "+)j([ˈ]?)(" + re.sub(r"ʋ", r"", consonant) + "+)", r"\1i̯\2\3", phonetic)
    phonetic = re.sub(r"(" + vowel + "+)j$", r"\1i̯", phonetic)
    # also at the beginning of a word before a consonant
    phonetic = re.sub(r"^j(" + re.sub(r"ʋ", r"", consonant) + "+)", r"i̯\1", phonetic)

    # remove old orthographic apostrophe
    phonetic = re.sub(r"!", "", phonetic)
    # moving the stress mark to where it belongs
    phonetic = re.sub(r"([bdzʒɡɦjʲmnlrpftskxʃʋwʍː͡]+)ˈ", r"ˈ\1", phonetic)
    phonetic = re.sub(r"([ui]̯)ˈ([ʲ]?" + vowel + ")", r"ˈ\1\2", phonetic)
    phonetic = re.sub(r"ˈ(l[ʲ]?[ː]?)(" + re.sub(r"l", r"", consonant) + ")", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ˈ(r[ʲ]?[ː]?)(" + re.sub(r"r", r"", consonant) + ")", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ˈ(m[ʲ]?[ː]?)([bpfɦszʃʋʒ])", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ˈ(n[ʲ]?[ː]?)([dtfkɡɦlxszʃʋʒ])", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ʲ?ːʲ", r"ʲː", phonetic)

    return phonetic


if __name__ == "__main__":
    for w in [f"Сла{ACUTE}ва", f"Украї{ACUTE}ні", f"сме{ACUTE}рть", f"ворога{ACUTE}м"]:
        print(w, "->", ipa(w, check_accent=True))
    for w in [f"остзе́йці"]:
        print(w, "->", ipa(w, check_accent=True))
