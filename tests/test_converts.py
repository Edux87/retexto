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
    def test_convert_specials(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.convert_specials(), object))

    @classmethod
    def test_convert_emoji(self):
        text = ReTexto(SAMPLE)
        assert_true(isinstance(text.convert_emoji(), object))
