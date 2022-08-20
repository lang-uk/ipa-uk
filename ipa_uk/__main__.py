import sys
from ipa_uk import ipa


for word in sys.stdin:
    word = word.rstrip()
    print(word, ipa(word, check_accent=False))
