from ipa_uk import ipa, ACUTE

def test_stressed_a():
    assert ipa(f"ма{ACUTE}ма") == "ˈmɑmɐ"

def test_unstressed_a():
    assert ipa(f"мо{ACUTE}ва") == "ˈmɔu̯ɐ"

def test_stressed_e():
    assert ipa(f"ве{ACUTE}лич") == "ˈʋɛlet͡ʃ"

def test_unstressed_e():
    assert ipa(f"Пе{ACUTE}тре") == "ˈpɛtre"

def test_stressed_y():
    assert ipa(f"при{ACUTE}мха") == "ˈprɪmxɐ"

def test_unstressed_y():
    assert ipa(f"мине{ACUTE}") == "meˈnɛ"

def test_stressed_i():
    assert ipa(f"ві{ACUTE}ра") == "ˈʋʲirɐ"

def test_unstressed_i():
    assert ipa(f"ко{ACUTE}рінь") == "ˈkɔrʲinʲ"

def test_stressed_o():
    assert ipa(f"коро{ACUTE}ва") == "kɔˈrɔu̯ɐ"

def test_unstressed_o():
    assert ipa(f"о{ACUTE}сінь") == "ˈɔsʲinʲ"

def test_stressed_u():
    assert ipa(f"У{ACUTE}мань") == "ˈumɐnʲ"

def test_unstressed_u():
    assert ipa(f"туди{ACUTE}") == "tʊˈdɪ"

    # assert ipa("тому") == "tomu"


    
    # assert ipa("пил") == "pɪl"
    # assert ipa("піт") == "pʲit"
    # assert ipa("бук") == "buk"
    # assert ipa("біль") == "bʲilʲ"
    # assert ipa("мат") == "mɑt"
    # assert ipa("стать") == "stɑtʲ"
    # assert ipa("дим") == "dɪm"
    # assert ipa("дім") == "dʲim"
    # assert ipa("кут") == "kut"
    # assert ipa("кіт") == "kʲit"
    # assert ipa("ґуля") == "gulʲɐ"
    # assert ipa("ґіпс") == "gʲips"
    # assert ipa("глум") == "ɦlum"
    # assert ipa("гість") == "ɦʲisʲtʲ"
    # assert ipa("хор") == "xɔr"
    # assert ipa("хід") == "xʲid"
    # assert ipa("фах") == "fɑx"
    # assert ipa("фільм") == "fʲilʲm"
    # assert ipa("вир") == "ʋɪr"
    # assert ipa("він") == "ʋʲin"
    # assert ipa("вухо") == "wuxo"
    # assert ipa("враз") == "wrɑz"
    # assert ipa("вперше") == "ʍpɛrʃe"
    # assert ipa("сад") == "sɑd"
    # assert ipa("Сян") == "sʲɐn" # alternative ɕɐn
    # assert ipa("зад") == "zɑd"
    # assert ipa("зір") == "zʲir" # alternative ʑir
    # assert ipa("шар") == "ʃɑr"
    # assert ipa("шість") == "ʃʲisʲtʲ"
    # assert ipa("затишшя") == "zɐtɪʃʲ:ɐ"
    # assert ipa("жар") == "ʒɑr"
    # assert ipa("жінка") == "ʒʲinkɐ"
    # assert ipa("заміжжя") == "zɐmiʒʲ:ɐ"
    # assert ipa("цирк") == "ʦɪrk"
    # assert ipa("ціна") == "ʦʲinɑ"
    # assert ipa("дзень") == "ʣɛnʲ"
    # assert ipa("дзінь") == "ʣʲinʲ"
    # assert ipa("час") == "ʧɑs"
    # assert ipa("чіп") == "ʧʲip"
    # assert ipa("узбіччя") == "ʊzbʲiʧʲ:ɐ"
    # assert ipa("бджола") == "bdʒolɑ"
    # assert ipa("бджіл") == "bdʒʲil"
    # assert ipa("мат") == "mɑt"
    # assert ipa("міра") == "mʲirɐ"
    # assert ipa("нас") == "nɑs"
    # assert ipa("ніс") == "nʲis"
    # assert ipa("лук") == "luk"
    # assert ipa("люк") == "lʲʊk"
    # assert ipa("рак") == "rɑk"
    # assert ipa("ряд") == "rʲɐd"
    # assert ipa("як") == "jɐk"
    # assert ipa("гай") == "ɦɑi̯"
    # assert ipa("найшов") == "nɐi̯ʃɔu̯"
    # assert ipa("став") == "stɑu̯"
    
    # assert ipa("Полісся") == "polʲisʲ:ɐ"
    # assert ipa("чужоземець") == "ˌt͡ʃʊʒozɛmet͡sʲ"




