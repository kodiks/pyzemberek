# coding=utf-8
import os
from os.path import join

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(PROJECT_ROOT)

ZEMBEREK_PATH = join(BASE_DIR, 'zemberek', 'bin', 'zemberek-full-0.17.1.jar')

import jnius_config

# jnius_config.add_options('-Xrs', '-Xmx4096')
if not jnius_config.vm_running:
    jnius_config.set_classpath(ZEMBEREK_PATH)

import jnius


class Normalizer():
    def __init__(self, look_up_root, lm_file_path):
        """
        Init class for Normalizer.
        It resolves related Java classes and initialize equivalent Python classes.

        You should first tokenize sentences like in example_normalize.py.

        You can find the baseline lookup files and language model here:
        https://drive.google.com/drive/folders/1tztjRiUs9BOTH-tb1v7FWyixl-iUpydW

        Args:
            look_up_root (str): The directory path includes helper files for normalization process.
            lm_file_path (str): The file path of 2-gram language model.

        Returns:
            None.

        Raises:
            ValueError: If given paths are not valid.
        """
        if not os.path.isdir(look_up_root):
            raise ValueError(f'The given path for look_up_root is not valid: {look_up_root}')

        if not os.path.isfile(lm_file_path):
            raise ValueError(f'The given path for lm_file_path is not valid: {lm_file_path}')

        self.__resolve_classes__()

        lookupRoot = self.PathClass.get(look_up_root)
        lmFile = self.PathClass.get(lm_file_path)
        morphology = self.TurkishMorphologyClass.createWithDefaults()
        self.TurkishSentenceNormalizer = self.TurkishSentenceNormalizerClass(morphology, lookupRoot, lmFile)

    def __resolve_classes__(self):
        """
        Get related Java classes.

        Args:
            None.
        Returns:
            None.
        Raises:
            None.
        """
        self.TurkishSentenceNormalizerClass = jnius.autoclass('zemberek.normalization.TurkishSentenceNormalizer')
        self.TurkishMorphologyClass = jnius.autoclass('zemberek.morphology.TurkishMorphology')
        self.PathClass = jnius.autoclass('java.nio.file.Paths')

    def normalize(self, sentence):
        """
         Normalize given sentence and return normalized sentence.

         Args:
             sentence (str): The raw sentence need to be normalized.

         Returns:
             - (str): The normalized sentence.

         Raises:
             None.
         """
        return self.TurkishSentenceNormalizer.normalize(sentence)