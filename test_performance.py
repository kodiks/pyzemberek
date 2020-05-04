#!/usr/bin/python
# -*- coding: utf-8 -*-
from zemberek.tokenization import Tokenization
from zemberek.stemmer import Stemmer
from tqdm import tqdm

zmbrk_tokenization = Tokenization()

content = "Bakan Soylu, Avrupa Birliği (AB) desteğiyle Orta Doğu Araştırmaları Merkezi (ORSAM) ve TOBB Üniversitesi iş birliğinde yürütülen proje kapsamında bir otelde düzenlenen ‘Uluslararası Radikalleşme ve Aşırılık Sempozyumu’nda yaptığı konuşmada, teröristlerin kaçırdığı 13-14 yaşlarındaki kız çocuklarının cinsel istismarına maruz kaldıklarını anlatarak bu yaştaki çocukların anne sevgisine muhtaç olduklarını söyledi.Teröristlerin bu eylemlerinin Birleşmiş Milletler tarafından da teyit edildiğini belirten Soylu, bugün şehirlerin PKK’dan tamamen temizlendiğini,  Doğu ve Güneydoğu’da yapılan yatırımlara değinen Soylu, şunları kaydetti: “Bunun sonucunda örgüte katılım tarihin en düşük seviyesindedir. Bir zamanlar yıllık 5 binli rakamlarla ifade edilen örgüte katılım sayısı 2018’de 136 kişi, bu yıl da şu ana kadar 101 kişidir. Örgütün rakamlarında daha düşük. Bu konuyu da kendilerine dert ediniyorlar. Elebaşlarından bir tanesi, son bir haftadaki değerlendirmesinde güneyden yani Suriye civarından örgüte katılım alabiliyoruz ama kuzeyden Türkiye tarafından örgüte artık katılım alamıyoruz diyor.” AA"

for i in tqdm(range(10000000)):
    sentences = zmbrk_tokenization.sentence_tokenize(content)
    words = zmbrk_tokenization.word_tokenize_for_sentences(sentences)
    #print(sentences)