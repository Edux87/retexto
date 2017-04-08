# -*- coding: UTF-8 -*-
from nose.tools import assert_equals, assert_true
from unittest import TestCase
from retexto import ReTexto


SAMPLE = '@Edux87, i need this www.google.com | https://github.com <br> \
    <strong>UserName </strong> \
    i\'m from Perú 😛 \
    #Friends #Text jajajajaja so fffunny  \
    loooveee thiiis 😌 \
    @florenciaflor19 Si!!! sé vo… 🐷JUANA🐷 \
    this is my smiles jejeje jojojo jujuju jijijijajaja 😂'


class RemoversTest(TestCase):
    @classmethod
    def test_lower(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.lower(), object))

    @classmethod
    def test_split_words_uniques(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.split_words(uniques=True), object))

    @classmethod
    def test_split_words(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.split_words(), object))

    @classmethod
    def test_pipe(self):
        text = ReTexto(SAMPLE).remove_html() \
            .remove_mentions() \
            .remove_tags() \
            .remove_smiles(by='SMILING') \
            .convert_specials() \
            .convert_emoji() \
            .remove_nochars(preserve_tilde=True) \
            .remove_url() \
            .remove_duplicate(r='a-jp-z') \
            .remove_duplicate_vowels() \
            .remove_duplicate_consonants() \
            .remove_punctuation() \
            .remove_multispaces() \
            .lower() \
            .split_words(uniques=True)

        assert_true(isinstance(text, object))
