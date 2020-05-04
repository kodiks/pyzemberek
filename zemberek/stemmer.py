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
from jnius.reflect import autoclass

class Stemmer():
    def __init__(self):
        
        self.TurkishMorphology = jnius.autoclass('zemberek.morphology.TurkishMorphology')
        self.WordAnalysis = jnius.autoclass('zemberek.morphology.analysis.WordAnalysis')
        

    def stem(self, word):
        morphology = self.TurkishMorphology.createWithDefaults()

        results = morphology.analyze(word).getAnalysisResults().toArray()

        return results
