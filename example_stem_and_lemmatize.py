#!/usr/bin/python
# -*- coding: utf-8 -*-
from zemberek.tokenization import Tokenization
from zemberek.stemmer import Stemmer
from tqdm import tqdm

zmbrk_stemmer = Stemmer()

stems = zmbrk_stemmer.stem('ışıklandırma')
#print(stems)
for s in stems:
    print(
        '{0}\n\tStems ={1}\n\tLemmas ={2}'.format(
            str(s.formatLong()),
            ", ".join([str(s) for s in s.getStems().toArray()]),
            ", ".join([str(s) for s in s.getLemmas().toArray()])
        )
    )

