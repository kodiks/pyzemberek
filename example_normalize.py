#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from zemberek.tokenization import Tokenization
from zemberek.normalizer import Normalizer

from tqdm import tqdm

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)

LOOK_UP_ROOT = os.path.join(PROJECT_ROOT, 'zemberek-data', 'normalization')
LM_FILE_PATH = os.path.join(PROJECT_ROOT, 'zemberek-data', 'lm', 'lm.2gram.slm')


zmbrk_tokenization = Tokenization()
zmbrk_normalize = Normalizer(LOOK_UP_ROOT, LM_FILE_PATH)


content = "Bakan Soylu, Avrupa Birliği (AB) desteğiyle Orta Doğu Araştırmaları Merkezi (ORSAM) ve TOBB Üniversitesi iş birliğinde yürütülen proje kapsamında bir otelde düzenlenen ‘Uluslararası Radikalleşme ve Aşırılık Sempozyumu’nda yaptığı konuşmada, teröristlerin kaçırdığı 13-14 yaşlarındaki kız çocuklarının cinsel istismarına maruz kaldıklarını anlatarak bu yaştaki çocukların anne sevgisine muhtaç olduklarını söyledi.Teröristlerin bu eylemlerinin Birleşmiş Milletler tarafından da teyit edildiğini belirten Soylu, bugün şehirlerin PKK’dan tamamen temizlendiğini,  Doğu ve Güneydoğu’da yapılan yatırımlara değinen Soylu, şunları kaydetti: “Bunun sonucunda örgüte katılım tarihin en düşük seviyesindedir. Bir zamanlar yıllık 5 binli rakamlarla ifade edilen örgüte katılım sayısı 2018’de 136 kişi, bu yıl da şu ana kadar 101 kişidir. Örgütün rakamlarında daha düşük. Bu konuyu da kendilerine dert ediniyorlar. Elebaşlarından bir tanesi, son bir haftadaki değerlendirmesinde güneyden yani Suriye civarından örgüte katılım alabiliyoruz ama kuzeyden Türkiye tarafından örgüte artık katılım alamıyoruz diyor.” AA"

# some Turkish tweet examples
content2 = "seni uzun zamadır takip ediyorum usta .   ?  napıcaz peki abi ,  teslim mi olucaz .  o kadar vahim durum  ?  ?  ama ilk defa seni bu kadar ümidini kaybetmiş gördüm .  o zaman bakabileceğimiz ooook işimiz olacak mı . "
content3 = 'izmiiir ’ e de gelecek misiniz :('
content4 = 'kardeş ali koc büyükk düşünüyor baya gidicek getircek bir yabancı kuracak sistemi ,  her açıdan alt yapı , taktiksel sistem yani o açıdan onu kaldırcak turk yok malesef ,  hem ali koç dedi şunu kariyerin sonlarına gelmiş yıldız oyuncu almak yok işte vizyon dedim vizyon'

sentences = zmbrk_tokenization.sentence_tokenize(content4)


# Example usage
# Sentences, which have been tokenized, are normalized.
for i, s in enumerate(sentences):
    print("Sentence {0}:  {1}".format(i, s))
    normalized_sentence = zmbrk_normalize.normalize(s)
    print("Normalized sentence: {0}\n".format(normalized_sentence))
