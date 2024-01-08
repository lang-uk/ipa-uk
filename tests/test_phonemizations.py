from ipa_uk import pronunciation as ipa


def test_pronunciation_secondary_stress():
    assert ipa("а̀віаполі́т", check_accent=True) == "ˌaʋʲiɐpoˈlʲit"
    assert ipa("нѐйробіоло́гія", check_accent=True) == "ˌnɛi̯rɔbʲiɔˈɫɔɦʲijɐ"


def test_pronunciation_monosyllabic():
    assert ipa("бік", check_accent=True) == "bʲik"
    assert ipa("нема́ за́ що", check_accent=True) == "neˈma ˈza ʃt͡ʃɔ"


def test_pronunciation_allophones_e_i():
    assert ipa("мене́", check_accent=True) == "meˈnɛ"
    assert ipa("мине́", check_accent=True) == "meˈnɛ"


def test_pronunciation_allophones_j():
    assert ipa("хай", check_accent=True) == "xai̯"
    assert ipa("зна́йте", check_accent=True) == "ˈznai̯te"
    assert ipa("ча́йка", check_accent=True) == "ˈt͡ʃai̯kɐ"
    assert ipa("мій", check_accent=True) == "mʲii̯"
    assert ipa("йня́ти", check_accent=True) == "ˈi̯nʲate"
    assert ipa("йод", check_accent=True) == "jɔd"
    assert ipa("моя́", check_accent=True) == "mɔˈja"
    assert ipa("мою́", check_accent=True) == "mɔˈju"
    assert ipa("моє́", check_accent=True) == "mɔˈjɛ"
    assert ipa("мої́", check_accent=True) == "mɔˈji"


def test_pronunciation_allophones_v():
    assert ipa("мав", check_accent=True) == "mau̯"
    assert ipa("був", check_accent=True) == "buu̯"
    assert ipa("ма́впа", check_accent=True) == "ˈmau̯pɐ"
    assert ipa("шовк", check_accent=True) == "ʃɔu̯k"
    assert ipa("вниз", check_accent=True) == "wnɪz"
    assert ipa("вона́", check_accent=True) == "wɔˈna"
    assert ipa("ву́хо", check_accent=True) == "ˈwuxɔ"
    assert ipa("впе́рше", check_accent=True) == "ˈʍpɛrʃe"
    assert ipa("він", check_accent=True) == "ʋʲin"


def test_pronunciation_voicing_slovnik_no10():
    assert ipa("відділи́ти", check_accent=True) == "ʋʲidʲːiˈɫɪte"
    assert ipa("надті́сувати", check_accent=True) == "nɐdʲˈtʲisʊʋɐte"


def test_pronunciation_voicing_slovnik_no6():
    assert ipa("боротьба́", check_accent=True) == "bɔrɔdʲˈba"


def test_pronunciation_assimilations_slovnik():
    assert ipa("ви́рісши", check_accent=True) == "ˈʋɪrʲiʃːe"
    assert ipa("ви́візши", check_accent=True) == "ˈʋɪʋʲiʒʃe"
    assert ipa("зши́ти", check_accent=True) == "ˈʃːɪte"
    assert ipa("зжо́вкнути", check_accent=True) == "ˈʒːɔu̯knʊte"
    assert ipa("безжа́лісний", check_accent=True) == "beˈʒːalʲisnei̯"
    assert ipa("безче́сний", check_accent=True) == "beʒˈt͡ʃɛsnei̯"
    assert ipa("зчи́стити", check_accent=True) == "ˈʃt͡ʃɪstete"


def test_pronunciation_assimilations_norm():
    assert ipa("відсі́ль", check_accent=True) == "ʋʲid͡zʲˈsʲilʲ"
    assert ipa("два́дцять", check_accent=True) == "ˈdʋad͡zʲt͡sʲɐtʲ"
    assert ipa("ро́биться", check_accent=True) == "ˈrɔbet͡sʲːɐ"
    assert ipa("кори́тця", check_accent=True) == "kɔˈrɪt͡sʲːɐ"


def test_pronunciation_phonetic_lengthened_consonants():
    assert ipa("знання́", check_accent=True) == "znɐˈnʲːa"
    assert ipa("рілля́", check_accent=True) == "rʲiˈlʲːa"
    assert ipa("ті́нню", check_accent=True) == "ˈtʲinʲːʊ"
    assert ipa("ллю", check_accent=True) == "lʲːu"
    assert ipa("обби́ти", check_accent=True) == "ɔˈbːɪte"
    assert ipa("зако́нний", check_accent=True) == "zɐˈkɔnːei̯"
    assert ipa("вітчи́зна", check_accent=True) == "ʋʲiˈt͡ʃːɪznɐ"
    assert ipa("болі́тце", check_accent=True) == "boˈlʲit͡sːe"
    assert ipa("ви́нісши", check_accent=True) == "ˈʋɪnʲiʃːe"
    assert ipa("зжува́ти", check_accent=True) == "ʒːʊˈʋate"
    assert ipa("бере́шся", check_accent=True) == "beˈrɛsʲːɐ"
    assert ipa("бері́ться", check_accent=True) == "beˈrʲit͡sʲːɐ"


def test_pronunciation_phonetic_simplification():
    assert ipa("студе́нтський", check_accent=True) == "stʊˈdɛnʲsʲkei̯"
    assert ipa("тури́стський", check_accent=True) == "tʊˈrɪsʲkei̯"
    assert ipa("аге́нтство", check_accent=True) == "ɐˈɦɛnstwɔ"
    assert ipa("солі́стці", check_accent=True) == "soˈlʲisʲt͡sʲ(ː)i"
    assert ipa("шістдеся́т", check_accent=True) == "ʃʲizdeˈsʲat"
    assert ipa("шістсо́т", check_accent=True) == "ʃʲiˈsːɔt"


def test_pronunciation_phonetic_consonant_assimilations_Pugh_p36_37_38():
    assert ipa("кни́жка", check_accent=True) == "ˈknɪʒkɐ"
    assert ipa("кни́жці", check_accent=True) == "ˈknɪzʲt͡sʲi"
    assert ipa("дочка́", check_accent=True) == "dɔt͡ʃˈka"
    assert ipa("дочці́", check_accent=True) == "dɔˈt͡sʲːi"
    assert ipa("чита́єш", check_accent=True) == "t͡ʃeˈtajeʃ"
    assert ipa("сміє́шся", check_accent=True) == "sʲmʲiˈjɛsʲːɐ"
    assert ipa("до́шка", check_accent=True) == "ˈdɔʃkɐ"
    assert ipa("до́шці", check_accent=True) == "ˈdɔsʲt͡sʲi"
    assert ipa("безжа́лісний", check_accent=True) == "beˈʒːalʲisnei̯"
    assert ipa("підрі́сши", check_accent=True) == "pʲiˈdʲrʲiʃːe"
    assert ipa("кімна́тці", check_accent=True) == "kʲimˈnat͡sʲːi"
    assert ipa("крава́тці", check_accent=True) == "krɐˈʋat͡sʲːi"
    assert ipa("неві́стці", check_accent=True) == "neˈʋʲisʲt͡sʲ(ː)i"
    assert ipa("борі́дці", check_accent=True) == "boˈrʲid͡zʲt͡sʲi"
    assert ipa("лю́дський", check_accent=True) == "ˈlʲud͡zʲsʲkei̯"
    # Pugh p. 37 claims that it should be sɔlˈdat͡sʲsʲkɪj, but Орфоепскі словник p. 97 claims otherwise
    assert ipa("солда́тський", check_accent=True) == "sɔɫˈdat͡sʲkei̯"


def test_pronunciation_phonetic_apostrophe_Pugh_p32():
    assert ipa("від'ї́зд", check_accent=True) == "ʋʲiˈdjizd"
    assert ipa("п'ю", check_accent=True) == "pju"
    assert ipa("ф'ю́кати", check_accent=True) == "ˈfjukɐte"
    assert ipa("об'є́кт", check_accent=True) == "ɔˈbjɛkt"
    assert ipa("п'ять", check_accent=True) == "pjatʲ"
    assert ipa("здоро́в'я", check_accent=True) == "zdɔˈrɔʋjɐ"
    assert ipa("м'яки́й", check_accent=True) == "mjɐˈkɪi̯"


def test_pronunciation_phonetic_Pugh_p29_p30():
    assert ipa("ти", check_accent=True) == "tɪ"
    assert ipa("ті", check_accent=True) == "tʲi"
    assert ipa("дя́кую", check_accent=True) == "ˈdʲakʊjʊ"
    assert ipa("сад", check_accent=True) == "sad"
    assert ipa("сядь", check_accent=True) == "sʲadʲ"
    assert ipa("пала́ц", check_accent=True) == "pɐˈɫat͡s"
    assert ipa("хло́пець", check_accent=True) == "ˈxɫɔpet͡sʲ"
    assert ipa("дзвін", check_accent=True) == "d͡zʲʋʲin"
    assert ipa("дзво́на", check_accent=True) == "ˈd͡zwɔnɐ"
    assert ipa("ра́са", check_accent=True) == "ˈrasɐ"
    assert ipa("ря́са", check_accent=True) == "ˈrʲasɐ"
    assert ipa("бі́лий", check_accent=True) == "ˈbʲiɫei̯"
    assert ipa("вів", check_accent=True) == "ʋʲiu̯"
    assert ipa("кінь", check_accent=True) == "kʲinʲ"
    assert ipa("шість", check_accent=True) == "ʃʲisʲtʲ"
    assert ipa("ножі́", check_accent=True) == "noˈʒʲi"
    assert ipa("уночі́", check_accent=True) == "ʊnoˈt͡ʃʲi"
    assert ipa("мі́сті", check_accent=True) == "ˈmʲisʲtʲi"
    assert ipa("одні́й", check_accent=True) == "odʲˈnʲii̯"
    assert ipa("сніг", check_accent=True) == "sʲnʲiɦ"
    assert ipa("люблю́", check_accent=True) == "lʲʊˈblʲu"
    assert ipa("коно́плі", check_accent=True) == "kɔˈnɔplʲi"
    assert ipa("графля́ть", check_accent=True) == "ɦrɐˈflʲatʲ"
    assert ipa("ко́рмлять", check_accent=True) == "ˈkɔrmlʲɐtʲ"


# If a vowel, an apostrophe, or nothing precedes я, є, ю, then they represent [j] + [a, ɛ, u].
def test_pronunciation_phonetic_ja_je_ju():
    assert ipa("а́я", check_accent=True) == "ˈajɐ"
    assert ipa("ея́", check_accent=True) == "eˈja"
    assert ipa("і́я", check_accent=True) == "ˈijɐ"
    assert ipa("ия́", check_accent=True) == "eˈja"
    assert ipa("о́я", check_accent=True) == "ˈɔjɐ"
    assert ipa("уя́", check_accent=True) == "ʊˈja"
    assert ipa("а́є", check_accent=True) == "ˈaje"
    assert ipa("еє́", check_accent=True) == "eˈjɛ"
    assert ipa("і́є", check_accent=True) == "ˈije"
    assert ipa("иє́", check_accent=True) == "eˈjɛ"
    assert ipa("о́є", check_accent=True) == "ˈɔje"
    assert ipa("ую́", check_accent=True) == "ʊˈju"
    assert ipa("а́ю", check_accent=True) == "ˈajʊ"
    assert ipa("ею́", check_accent=True) == "eˈju"
    assert ipa("і́ю", check_accent=True) == "ˈijʊ"
    assert ipa("ию́", check_accent=True) == "eˈju"
    assert ipa("о́ю", check_accent=True) == "ˈɔjʊ"
    assert ipa("ую́", check_accent=True) == "ʊˈju"
    assert ipa("'я", check_accent=False) == "jɐ"
    assert ipa("'є", check_accent=False) == "je"
    assert ipa("'ю", check_accent=False) == "jʊ"
    assert ipa("я", check_accent=False) == "jɐ"
    assert ipa("є", check_accent=False) == "je"
    assert ipa("ю", check_accent=False) == "jʊ"


# phonemic and subphonemic weak palatalization.
def test_pronunciation_phonetic_softening_ja_je_ji_ju():
    # first 12 subphonemic: б п в ф м к г х ж ш ч щ дж ждж
    assert ipa("б", check_accent=True) == "b"
    assert ipa("бі", check_accent=False) == "bʲi"
    assert ipa("бя", check_accent=False) == "bʲɐ"
    assert ipa("бє", check_accent=False) == "bʲe"
    assert ipa("бю", check_accent=False) == "bʲʊ"
    assert ipa("п", check_accent=True) == "p"
    assert ipa("пі", check_accent=False) == "pʲi"
    assert ipa("пя", check_accent=False) == "pʲɐ"
    assert ipa("пє", check_accent=False) == "pʲe"
    assert ipa("пю", check_accent=False) == "pʲʊ"
    assert ipa("в", check_accent=True) == "ʋ"
    assert ipa("ві", check_accent=False) == "ʋʲi"
    assert ipa("вя", check_accent=False) == "ʋʲɐ"
    assert ipa("вє", check_accent=False) == "ʋʲe"
    assert ipa("вю", check_accent=False) == "ʋʲʊ"
    assert ipa("ф", check_accent=True) == "f"
    assert ipa("фі", check_accent=False) == "fʲi"
    assert ipa("фя", check_accent=False) == "fʲɐ"
    assert ipa("фє", check_accent=False) == "fʲe"
    assert ipa("фю", check_accent=False) == "fʲʊ"
    assert ipa("м", check_accent=True) == "m"
    assert ipa("мі", check_accent=False) == "mʲi"
    assert ipa("мя", check_accent=False) == "mʲɐ"
    assert ipa("мє", check_accent=False) == "mʲe"
    assert ipa("мю", check_accent=False) == "mʲʊ"
    assert ipa("к", check_accent=True) == "k"
    assert ipa("кі", check_accent=False) == "kʲi"
    assert ipa("кя", check_accent=False) == "kʲɐ"
    assert ipa("кє", check_accent=False) == "kʲe"
    assert ipa("кю", check_accent=False) == "kʲʊ"
    assert ipa("г", check_accent=True) == "ɦ"
    assert ipa("гі", check_accent=False) == "ɦʲi"
    assert ipa("гя", check_accent=False) == "ɦʲɐ"
    assert ipa("гє", check_accent=False) == "ɦʲe"
    assert ipa("гю", check_accent=False) == "ɦʲʊ"
    assert ipa("х", check_accent=True) == "x"
    assert ipa("хі", check_accent=False) == "xʲi"
    assert ipa("хя", check_accent=False) == "xʲɐ"
    assert ipa("хє", check_accent=False) == "xʲe"
    assert ipa("хю", check_accent=False) == "xʲʊ"
    assert ipa("ж", check_accent=True) == "ʒ"
    assert ipa("жі", check_accent=False) == "ʒʲi"
    assert ipa("жя", check_accent=False) == "ʒʲɐ"
    assert ipa("жє", check_accent=False) == "ʒʲe"
    assert ipa("жю", check_accent=False) == "ʒʲʊ"
    assert ipa("ш", check_accent=True) == "ʃ"
    assert ipa("ші", check_accent=False) == "ʃʲi"
    assert ipa("шя", check_accent=False) == "ʃʲɐ"
    assert ipa("шє", check_accent=False) == "ʃʲe"
    assert ipa("шю", check_accent=False) == "ʃʲʊ"
    assert ipa("ч", check_accent=True) == "t͡ʃ"
    assert ipa("чі", check_accent=False) == "t͡ʃʲi"
    assert ipa("чя", check_accent=False) == "t͡ʃʲɐ"
    assert ipa("чє", check_accent=False) == "t͡ʃʲe"
    assert ipa("чю", check_accent=False) == "t͡ʃʲʊ"
    assert ipa("щ", check_accent=True) == "ʃt͡ʃ"
    assert ipa("щі", check_accent=False) == "ʃt͡ʃʲi"
    assert ipa("щя", check_accent=False) == "ʃt͡ʃʲɐ"
    assert ipa("щє", check_accent=False) == "ʃt͡ʃʲe"
    assert ipa("щю", check_accent=False) == "ʃt͡ʃʲʊ"
    assert ipa("дж", check_accent=True) == "d͡ʒ"
    assert ipa("джі", check_accent=False) == "d͡ʒʲi"
    assert ipa("джя", check_accent=False) == "d͡ʒʲɐ"
    assert ipa("джє", check_accent=False) == "d͡ʒʲe"
    assert ipa("джю", check_accent=False) == "d͡ʒʲʊ"
    assert ipa("ждж", check_accent=True) == "ʒd͡ʒ"
    assert ipa("жджі", check_accent=False) == "ʒd͡ʒʲi"
    assert ipa("жджя", check_accent=False) == "ʒd͡ʒʲɐ"
    assert ipa("жджє", check_accent=False) == "ʒd͡ʒʲe"
    assert ipa("жджю", check_accent=False) == "ʒd͡ʒʲʊ"
    # 9 phonemic softenings: т д с з ц дз н л
    assert ipa("т", check_accent=True) == "t"
    assert ipa("ті", check_accent=False) == "tʲi"
    assert ipa("тя", check_accent=False) == "tʲɐ"
    assert ipa("тє", check_accent=False) == "tʲe"
    assert ipa("тю", check_accent=False) == "tʲʊ"
    assert ipa("д", check_accent=True) == "d"
    assert ipa("ді", check_accent=False) == "dʲi"
    assert ipa("дя", check_accent=False) == "dʲɐ"
    assert ipa("дє", check_accent=False) == "dʲe"
    assert ipa("дю", check_accent=False) == "dʲʊ"
    assert ipa("с", check_accent=True) == "s"
    assert ipa("сі", check_accent=False) == "sʲi"
    assert ipa("ся", check_accent=False) == "sʲɐ"
    assert ipa("сє", check_accent=False) == "sʲe"
    assert ipa("сю", check_accent=False) == "sʲʊ"
    assert ipa("з", check_accent=True) == "z"
    assert ipa("зі", check_accent=False) == "zʲi"
    assert ipa("зя", check_accent=False) == "zʲɐ"
    assert ipa("зє", check_accent=False) == "zʲe"
    assert ipa("зю", check_accent=False) == "zʲʊ"
    assert ipa("ц", check_accent=True) == "t͡s"
    assert ipa("ці", check_accent=False) == "t͡sʲi"
    assert ipa("ця", check_accent=False) == "t͡sʲɐ"
    assert ipa("цє", check_accent=False) == "t͡sʲe"
    assert ipa("цю", check_accent=False) == "t͡sʲʊ"
    assert ipa("дз", check_accent=True) == "d͡z"
    assert ipa("дзі", check_accent=False) == "d͡zʲi"
    assert ipa("дзя", check_accent=False) == "d͡zʲɐ"
    assert ipa("дзє", check_accent=False) == "d͡zʲe"
    assert ipa("дзю", check_accent=False) == "d͡zʲʊ"
    assert ipa("н", check_accent=True) == "n"
    assert ipa("ні", check_accent=False) == "nʲi"
    assert ipa("ня", check_accent=False) == "nʲɐ"
    assert ipa("нє", check_accent=False) == "nʲe"
    assert ipa("ню", check_accent=False) == "nʲʊ"
    assert ipa("л", check_accent=True) == "ɫ"
    assert ipa("лі", check_accent=False) == "lʲi"
    assert ipa("ля", check_accent=False) == "lʲɐ"
    assert ipa("лє", check_accent=False) == "lʲe"
    assert ipa("лю", check_accent=False) == "lʲʊ"
    assert ipa("р", check_accent=True) == "r"
    assert ipa("рі", check_accent=False) == "rʲi"
    assert ipa("ря", check_accent=False) == "rʲɐ"
    assert ipa("рє", check_accent=False) == "rʲe"
    assert ipa("рю", check_accent=False) == "rʲʊ"


def test_pronunciation_phonetic_hard_soft_sign():
    assert ipa("т", check_accent=True) == "t"
    assert ipa("ть", check_accent=True) == "tʲ"
    assert ipa("д", check_accent=True) == "d"
    assert ipa("дь", check_accent=True) == "dʲ"
    assert ipa("с", check_accent=True) == "s"
    assert ipa("сь", check_accent=True) == "sʲ"
    assert ipa("з", check_accent=True) == "z"
    assert ipa("зь", check_accent=True) == "zʲ"
    assert ipa("ц", check_accent=True) == "t͡s"
    assert ipa("ць", check_accent=True) == "t͡sʲ"
    assert ipa("дз", check_accent=True) == "d͡z"
    assert ipa("дзь", check_accent=True) == "d͡zʲ"
    assert ipa("н", check_accent=True) == "n"
    assert ipa("нь", check_accent=True) == "nʲ"
    assert ipa("л", check_accent=True) == "ɫ"
    assert ipa("ль", check_accent=True) == "lʲ"
    assert ipa("п", check_accent=True) == "p"
    assert ipa("пь", check_accent=True) == "pʲ"


def test_pronunciation_phonetic_dual_pronunciation_prefix_bez_roz():
    assert ipa("розписа́ти", check_accent=True) == "rɔzpeˈsate"
    assert ipa("росписа́ти", check_accent=True) == "rɔspeˈsate"
    assert ipa("безпла́тний", check_accent=True) == "bezˈpɫatnei̯"
    assert ipa("беспла́тний", check_accent=True) == "beˈspɫatnei̯"


def test_pronunciation_phonetic_assimilation_voiceless_voiced():
    assert ipa("вокза́л", check_accent=True) == "wɔɡˈzaɫ"
    assert ipa("якби́", check_accent=True) == "jɐɡˈbɪ"
    assert ipa("молотьба́", check_accent=True) == "mɔɫɔdʲˈba"
    assert ipa("анекдо́т", check_accent=True) == "ɐneɡˈdɔt"
    assert ipa("при", check_accent=True) == "prɪ"


def test_pronunciation_phonetic_basic():
    assert ipa("ходжу́", check_accent=True) == "xoˈd͡ʒu"
    assert ipa("джи́нси", check_accent=True) == "ˈd͡ʒɪnse"
    assert ipa("дзе́ркало", check_accent=True) == "ˈd͡zɛrkɐɫɔ"
    assert ipa("дзво́ник", check_accent=True) == "ˈd͡zwɔnek"
    assert ipa("дзьоб", check_accent=True) == "d͡zʲɔb"
    assert ipa("агре́сія", check_accent=True) == "ɐˈɦrɛsʲijɐ"
    assert ipa("шви́дше", check_accent=True) == "ˈʃʋɪd͡ʒʃe"
    assert ipa("ї́жте", check_accent=True) == "ˈjiʒte"
    assert ipa("ро́зталь", check_accent=True) == "ˈrɔztɐlʲ"
    assert ipa("шви́дко", check_accent=True) == "ˈʃʋɪdkɔ"
    assert ipa("ніж", check_accent=True) == "nʲiʒ"
    assert ipa("ри́бка", check_accent=True) == "ˈrɪbkɐ"
    assert ipa("ка́зка", check_accent=True) == "ˈkazkɐ"
    assert ipa("ка́ска", check_accent=True) == "ˈkaskɐ"
    assert ipa("залюбки́", check_accent=True) == "zɐlʲʊbˈkɪ"
    assert ipa("мед", check_accent=True) == "mɛd"
    # must be rʲ, error in the book p. 26
    assert ipa("скрізь", check_accent=True) == "skrʲizʲ"
    # word-initial stressed vowel; formerly not handled correctly
    assert ipa("О́сло", check_accent=True) == "ˈɔsɫɔ"


def test_pronunciation_phonetic_diphonemic_dz_dzh_dsh_dch():
    assert ipa("піджжива́ти", check_accent=True) == "pʲid͡ʒʒeˈʋate"
    assert ipa("віджжи́лий", check_accent=True) == "ʋʲid͡ʒˈʒɪɫei̯"
    assert ipa("підззе́мний", check_accent=True) == "pʲid͡zˈzɛmnei̯"
    assert ipa("підззира́ти", check_accent=True) == "pʲid͡zzeˈrate"
    assert ipa("відшу́кувати", check_accent=True) == "ʋʲid͡ʒˈʃukʊʋɐte"
    assert ipa("відчуття́", check_accent=True) == "ʋʲid͡ʒt͡ʃʊˈtʲːa"
    assert ipa("відці́джувати", check_accent=True) == "ʋʲid͡zʲˈt͡sʲid͡ʒʊʋɐte"
    assert ipa("відцвіта́ти", check_accent=True) == "ʋʲid͡zt͡sʲʋʲiˈtate"


def test_pronunciation_multiword_expressions():
    # initial stress in a medial word formerly not handled correctly
    assert (
        ipa("Сполу́чені Шта́ти Аме́рики", check_accent=True)
        == "spoˈɫut͡ʃenʲi ˈʃtate ɐˈmɛreke"
    )
