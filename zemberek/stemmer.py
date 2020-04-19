# coding=utf-8
import os
from os.path import join


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
ZEMBEREK_PATH = join(ROOT_DIR, 'bin', 'zemberek-full-0.17.1.jar')

import jnius_config
#jnius_config.add_options('-Xrs', '-Xmx4096')
if not jnius_config.vm_running:
    jnius_config.set_classpath(ZEMBEREK_PATH)

import jnius
from jnius.reflect import autoclass

class Stemmer():
    def __init__(self):
        
        self.TurkishMorphology = jnius.autoclass('zemberek.morphology.TurkishMorphology')
        self.WordAnalysis = jnius.autoclass('zemberek.morphology.analysis.WordAnalysis')
        

    def stem(self, word):
        morphology = self.TurkishMorphology.createWithDefaults()

        results = morphology.analyze(word).getAnalysisResults().toArray()

        return results
