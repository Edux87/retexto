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
    def test_remove_html(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_html(), object))

    @classmethod
    def test_remove_mentions(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_mentions(), object))

    @classmethod
    def test_remove_tags(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_tags(), object))

    @classmethod
    def test_remove_smiles(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_smiles(), object))

    @classmethod
    def test_convert_specials(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.convert_specials(), object))

    @classmethod
    def test_convert_emoji(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.convert_emoji(), object))

    @classmethod
    def test_remove_nochars(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_nochars(), object))

    @classmethod
    def test_strip_acents(self):
        text = ReTexto('perú')
        assert_true(text.strip_accents().text == 'peru')

    @classmethod
    def test_remove_nochars_2(self):
        text = ReTexto('perÚ - AÑo')
        assert_true(
            isinstance(text.remove_nochars(preserve_tilde=True), object)
        )

    @classmethod
    def test_remove_url(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_url(), object))

    @classmethod
    def test_remove_duplicate(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_duplicate(), object))

    @classmethod
    def test_remove_duplicate_vowels(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_duplicate_vowels(), object))

    @classmethod
    def test_remove_duplicate_consonants(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_duplicate_consonants(), object))

    @classmethod
    def test_remove_punctuation(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_punctuation(), object))

    @classmethod
    def test_remove_multispaces(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_multispaces(), object))

    @classmethod
    def test_remove_stopwords(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.remove_stopwords(), object))
