# -*- coding: UTF-8 -*-
from retexto import ReTexto


if __name__ == '__main__':
    s = '@Edux87, i need this www.google.com | https://github.com <br> \
        <strong>UserName: çarlos </strong> \
        i\'m from Perú 😛 \
        #Friends #Text jajajajaja so fffunny  \
        loooveee thiiis 😌😎 \
        @florenciaflor19 Si!!! sé vo… 🐷JUANA🐷 \
        smile! haha jejeje jojojo jujuju jijijijajaja 😂'

    text = ReTexto(s)
    s = text.remove_html() \
            .remove_mentions() \
            .remove_tags() \
            .remove_smiles(by='SMILING') \
            .convert_emoji() \
            .convert_specials() \
            .remove_url() \
            .remove_duplicate(r='a-jp-z') \
            .remove_duplicate_vowels() \
            .remove_duplicate_consonants() \
            .remove_multispaces() \
            .remove_punctuation(by=' ') \
            .remove_nochars(preserve_tilde=True) \
            .lower() \
            .split_words(uniques=True)
    print(s)
