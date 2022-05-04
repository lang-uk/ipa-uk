# ipa-uk
Python package to generate IPA (international phonetic alphabet) for ukrainian words and sentences.

The module provides a python implementation of the IPA phonemisation algorithm, found
on wiktionary (https://uk.wiktionary.org/wiki/Модуль:uk-pron) 

Original code also has a comment on the input words:
```
Дифонемні послідовності приголосних, що передають один звук, повинні бути записані з
другим додатковим елементом: дж → джж: віджи́лій → віджжи́лий дз → ДЗЗ: підзе́мний → підззе́мній
```

The module exposes one function `ipa` and two constants, `acute` and `grave` so you can
add stresses to the words like this `f"Украї{acute}ні"`
