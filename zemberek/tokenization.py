# coding=utf-8
import os
from os.path import join

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)

ZEMBEREK_PATH = join(BASE_DIR, 'zemberek', 'bin', 'zemberek-full-0.17.1.jar')

import jnius_config
#jnius_config.add_options('-Xrs', '-Xmx4096')
if not jnius_config.vm_running:
    jnius_config.set_classpath(ZEMBEREK_PATH)

import jnius

class Tokenization():
    def __init__(self):
        
        self.TurkishSentenceExtractor = jnius.autoclass('zemberek.tokenization.TurkishSentenceExtractor')
        self.TurkishTokenizer = jnius.autoclass('zemberek.tokenization.TurkishTokenizer')
        self.Token = jnius.autoclass('zemberek.tokenization.Token')
        self.TokenType = jnius.autoclass('zemberek.tokenization.Token$Type')
    
        #print(dir(self.Token))

    def sentence_tokenize(self, text):
        extractor = self.TurkishSentenceExtractor.DEFAULT

    
        sentences = extractor.fromDocument(text).toArray()
        #print("sentences", sentences)
        #sentences_array = jArrayList(sentences, jObject)
        #for i, item in enumerate(sentences.toArray()):
        #    print(item)


        sentence_list =  list(map( lambda i, word :  '%s'%( word ), range(1,len(sentences)+1), sentences))

        return sentence_list

    def word_tokenize(self, sentence):
        #tokenizer: TurkishTokenizer = TurkishTokenizer.DEFAULT
        
        tokenizer = self.TurkishTokenizer.DEFAULT
        
        #self.tokenizer = self.TurkishTokenizer.builder().ignoreTypes(
        #    self.Token.Type.Punctuation,
        #    self.Token.Type.NewLine,
        #    self.Token.Type.SpaceTab
        #).build()

        words_list = []
        for i, token in enumerate(tokenizer.tokenizeToStrings(sentence).toArray()):
            words_list.append(str(token))

        return words_list

    def word_tokenize_for_sentences(self, sentences_list):
        #tokenizer = self.TurkishTokenizer.DEFAULT
        #print(tokenizer)

        tokenizer =  self.TurkishTokenizer.builder().ignoreTypes(
            self.TokenType.Punctuation,
            self.TokenType.NewLine,
            self.TokenType.SpaceTab
        ).build()

        sentences_words_list = []
        for sentence in sentences_list:
            words_list = []
            for i, token in enumerate(tokenizer.tokenizeToStrings(sentence).toArray()):
                #print(f' | Token String {i} = {token}')
                words_list.append(str(token))
            sentences_words_list.append(words_list)


        return sentences_words_list