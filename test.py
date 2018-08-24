# -*- coding: UTF-8 -*-
from retexto import ReTexto


if __name__ == '__main__':
    s = '@Edux87, i need this www.google.com | https://github.com <br> \
        <strong>UserName: çarlos </strong> \
        i\'m from Perú 😛 \
        FeLiZ aÑo NuEVo \
        #Friends #Text jajajajaja so fffunny  \
        loooveee thiiis 😌😎 \
        @florenciaflor19 Si!!! sé vo… 🐷JUANA🐷 \
        smiles! hahaha jejeje jojojo jujuju jijijijajaja 😂'
    text = ReTexto(s)
    s = text.remove_html() \
            .lower() \
            .remove_mentions() \
            .remove_tags() \
            .remove_smiles(by='smiling') \
            .remove_url() \
            .remove_duplicate(r='a-km-qs-y') \
            .remove_duplicate_vowels() \
            .remove_duplicate_consonants() \
            .remove_multispaces() \
            .remove_punctuation(by=' ') \
            .convert_emoji() \
            .remove_nochars(preserve_tilde=True) \
            .remove_stopwords() \
            .split_words()
    print(s)
    s = 'San Juan de Lurigancho ¿Por qué es una mala idea destruir un complejo \
        verde y deportivo para levantar un hospital? El barrio Enrique \
        Montenegro en San Juan de Lurigancho (SJL) sin dinero'
    text = ReTexto(s)
    s = text.remove_html() \
            .lower() \
            .remove_nochars(preserve_tilde=True) \
            .remove_stopwords() \
            .split_words()
    print(s)
    s = 'Que buen Año! mi PerÚ'
    text = ReTexto(s)
    s = text.remove_html() \
            .lower() \
            .remove_nochars(preserve_tilde=True) \
            .remove_stopwords()

    print(s.text)
    s = 'Cantó, señalÓ, Mirá, Pí'
    text = ReTexto(s)
    s = text.strip_accents()
    print(s.text)
