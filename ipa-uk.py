"""
That module provides a python implementation of the IPA phonemisation algorithm, found
on wiktionary (https://uk.wiktionary.org/wiki/Модуль:uk-pron) 

Original code also has a comment on the input words:
Дифонемні послідовності приголосних, що передають один звук, повинні бути записані з
другим додатковим елементом: дж → джж: віджи́лій → віджжи́лий дз → ДЗЗ: підзе́мний → підззе́мній

The module exposes one function `ipa` and two constants, `acute` and `grave` so you can
add stresses to the words like this f"Украї{acute}ні"
"""

import re

acute = chr(0x301)
grave = chr(0x300)


class AccentIsMissing(Exception):
    pass


def ipa(word: str, accent: bool) -> str:
    """
    Returns the IPA transcription of the given word or sentence according to the wiktionary algorithm

    Parameters:
        word (str): the word or the sentence to transcribe
        accent (bool): enable mandatory verification for at least one stressed syllable
    Returns:
        phonetic (str): phonemised string
    """
    word = word.lower()

    needs_accent: bool = False

    if accent:
        if acute not in word and grave not in word:
            if len(re.findall(r"[аеєиіїоуюя]", word)) > 1:
                raise AccentIsMissing(
                    f"The provided word is missing an accent (and has more than one syllable). Set accent=False to disable that check"
                )

    palatalizable: str = r"[tdsznlrbpʋfɡmkɦxʃʒ]"
    voiced_obstruent: str = r"[bdzʒɡɦ]"
    vowel: str = r"[ɑɛiɪuɔɐoʊe]"
    consonant: str = r"[bdzʒɡɦmnlrpftskxʃʋ]"

    phonetic_chars_map: list[dict[str, str]] = [
        #  последовательность трёх символов, которая переводится в звуки МФА
        {
            "дзь": "d͡zʲ",
            #  Dental plosives assimilate to following hissing/hushing consonants, which is not noted in the spelling.
            "тьс": "t͡sʲː",
        },
        #  последовательность двух символов, которая переводится в звуки МФА
        {
            "дж": "d͡ʒ",
            "дз": "d͡z",
            #  Dental plosives assimilate to following hissing/hushing consonants, which is not noted in the spelling.
            "дс": "d͡zs",
            "дш": "d͡ʒʃ",
            "дч": "d͡ʒt͡ʃ",
            "дц": "d͡zt͡s",
            "тс": "t͡s",
            "тш": "t͡ʃʃ",
            "тч": "t͡ʃː",
            "тц": "t͡sː",
        },
        #  отдельные символы, которые переводятся в звуки МФА; они обрабатываются последними
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
            #  ударные гласные
            acute: "ˈ",
            grave: "ˈ",
        },
    ]
    orthographic_replacements: dict = {
        # first apply consonant cluster simplifications that always occur orthographically
        r"нтськ": "ньськ",
        r"стськ": "ськ",
        r"нтст": "нст",
        r"стч": "шч",
        r"стд": "зд",
        r"стс": "сː",
        r"стськ": "ськ",
        r"^зш": "шː",
        r"зш": "жш",
        r"^зч": "шч",
        r"зч": "жч",
        # then long consonants that are orthographically geminated.
        r"([бвгґд])\1": r"\1ː",  # TODO: correct replacements
        r"([^д]+)жж": r"\1жː",  # джж последовательность кодирует дифонический дж
        r"([^д]+)зз": r"\1зː",  # дзз последовательность кодирует дифонический дз
        r"([йклмнпрстфхцчшщ])\1": r"\1ː",
        r"дждж": r"джː",
        r"дздз": r"дзː",
    }

    phonetic: str = word

    for regex, replacement in orthographic_replacements.items():
        phonetic = re.sub(regex, replacement, phonetic)

    # переназначение апострофа на '!', чтобы не противоречило ударной отметке МФА
    phonetic = phonetic.replace("'", "!")

    for replacements in phonetic_chars_map:
        for key, replacement in replacements.items():
            phonetic = re.sub(key, replacement, phonetic)

    phonetic = re.sub(r"([ɑɛiɪuɔ])ˈ", r"ˈ\1", phonetic)

    # добавление ударения, если слово с одним слогом и без "|ударение=откл"
    number_of_vowels = len(re.findall(r"[ɑɛiɪuɔ]", phonetic))

    if number_of_vowels == 1 and accent:
        phonetic = re.sub(r"([ɑɛiɪuɔ])", r"ˈ\1", phonetic)

    # palatalizable consonants before /i/ or /j/ become palatalized
    phonetic = re.sub(r"(" + palatalizable + ")([ː]?)([ˈ]?)i", r"\1ʲ\2\3i", phonetic)
    phonetic = re.sub(r"(" + palatalizable + ")([ː]?)j", r"\1ʲ\2", phonetic)

    # eliminate garbage sequences of [ʲːj] resulting from -тьс- cluster followed by [j]
    phonetic = re.sub(r"ʲːj", r"ʲː", phonetic)

    # -- упрощение согласных: ст + ц' → [с'ц']. Мы создаём это из-за палатализации.
    # -- Так как т +ц → [ц:] присутствует правило о долготе. Согласно «Орфоэпическому словарю» p. 13,
    # -- обе формы правильные, без долготы в обычной (разговорной) речи и с долготой
    # -- в медленной речи, поэтому мы заключаем в скобки долготу как опциональную.
    phonetic = re.sub(r"st͡sʲ([ː]?)", r"sʲt͡sʲ(\1)", phonetic)

    # ассимиляция: глухой + звонкий = звонкий + звонкий
    # должна ли /ʋ/ включаться как звонкая? «Орфоепічний словник» не озвучивает начальный кластер шв (p. 116)
    voicing: dict[str, str] = {
        "p": "b",
        "f": "v",
        "t": "d",
        "tʲ": "dʲ",
        "s": "z",
        "sʲ": "zʲ",
        "ʃ": "ʒ",
        "k": "ɡ",
        "x": "ɦ",
        "t͡s": "d͡z",
        "t͡sʲ": "d͡zʲ",
        "t͡ʃ": "d͡ʒ",
        "ʃt͡ʃ": "ʒd͡ʒ",
    }

    for voiceless, voiced in voicing.items():
        phonetic = re.sub(voiceless + "(" + voiced_obstruent + "+)", voiced + "\1", phonetic)

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
    # /ʋ/ has an allophone [ʍ] before before voiceless consonants (not after a vowel)
    phonetic = re.sub(r"ʋ([pftskxʃ]+)", r"ʍ\1", phonetic)

    # in a syllable-final position (i.e. the first position of a syllable coda) /j/ has an allophone [i̯]:
    phonetic = re.sub(r"(" + vowel + "+)j([ˈ]?)(" + re.sub(r"ʋ", r"", consonant) + "+)", r"\1i̯\2%3", phonetic)
    phonetic = re.sub(r"(" + vowel + "+)j$", r"\1i̯", phonetic)
    # also at the beginning of a word before a consonant
    phonetic = re.sub(r"^j(" + re.sub(r"ʋ", r"", consonant) + "+)", r"i̯\1", phonetic)

    # remove old orthographic apostrophe
    phonetic = re.sub(r"!", "", phonetic)
    # stress mark in correct place
    phonetic = re.sub(r"([bdzʒɡɦjʲmnlrpftskxʃʋwʍː͡]+)ˈ", r"ˈ\1", phonetic)
    phonetic = re.sub(r"([ui]̯)ˈ([ʲ]?" + vowel + ")", r"ˈ\1\2", phonetic)
    phonetic = re.sub(r"ˈ(l[ʲ]?[ː]?)(" + re.sub(r"l", r"", consonant) + ")", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ˈ(r[ʲ]?[ː]?)(" + re.sub(r"r", r"", consonant) + ")", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ˈ(m[ʲ]?[ː]?)([bpfɦszʃʋʒ])", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ˈ(n[ʲ]?[ː]?)([dtfkɡɦlxszʃʋʒ])", r"\1ˈ\2", phonetic)
    phonetic = re.sub(r"ʲ?ːʲ", r"ʲː", phonetic)

    return phonetic


if __name__ == "__main__":
    for w in [f"Сла{acute}ва", f"Украї{acute}ні", f"сме{acute}рть", f"ворога{acute}м"]:
        print(w, "->", ipa(w, accent=True))
