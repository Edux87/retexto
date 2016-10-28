# -*- coding: UTf-8 -*-


__all__ = ['ENG', 'stopwords']

ENG = [
    u'i',
    u'me',
    u'my',
    u'myself',
    u'we',
    u'our',
    u'ours',
    u'ourselves',
    u'you',
    u'your',
    u'yours',
    u'yourself',
    u'yourselves',
    u'he',
    u'him',
    u'his',
    u'himself',
    u'she',
    u'her',
    u'hers',
    u'herself',
    u'it',
    u'its',
    u'itself',
    u'they',
    u'them',
    u'their',
    u'theirs',
    u'themselves',
    u'what',
    u'which',
    u'who',
    u'whom',
    u'this',
    u'that',
    u'these',
    u'those',
    u'am',
    u'is',
    u'are',
    u'was',
    u'were',
    u'be',
    u'been',
    u'being',
    u'have',
    u'has',
    u'had',
    u'having',
    u'do',
    u'does',
    u'did',
    u'doing',
    u'a',
    u'an',
    u'the',
    u'and',
    u'but',
    u'if',
    u'or',
    u'because',
    u'as',
    u'until',
    u'while',
    u'of',
    u'at',
    u'by',
    u'for',
    u'with',
    u'about',
    u'against',
    u'between',
    u'into',
    u'through',
    u'during',
    u'before',
    u'after',
    u'above',
    u'below',
    u'to',
    u'from',
    u'up',
    u'down',
    u'in',
    u'out',
    u'on',
    u'off',
    u'over',
    u'under',
    u'again',
    u'further',
    u'then',
    u'once',
    u'here',
    u'there',
    u'when',
    u'where',
    u'why',
    u'how',
    u'all',
    u'any',
    u'both',
    u'each',
    u'few',
    u'more',
    u'most',
    u'other',
    u'some',
    u'such',
    u'no',
    u'nor',
    u'not',
    u'only',
    u'own',
    u'same',
    u'so',
    u'than',
    u'too',
    u'very',
    u's',
    u't',
    u'can',
    u'will',
    u'just',
    u'don',
    u'should',
    u'now',
    u'd',
    u'll',
    u'm',
    u'o',
    u're',
    u've',
    u'y',
    u'ain',
    u'aren',
    u'couldn',
    u'didn',
    u'doesn',
    u'hadn',
    u'hasn',
    u'haven',
    u'isn',
    u'ma',
    u'mightn',
    u'mustn',
    u'needn',
    u'shan',
    u'shouldn',
    u'wasn',
    u'weren',
    u'won',
    u'wouldn'
]

SPA = [
    u'de',
    u'la',
    u'que',
    u'el',
    u'en',
    u'y',
    u'a',
    u'los',
    u'del',
    u'se',
    u'las',
    u'por',
    u'un',
    u'para',
    u'con',
    u'no',
    u'una',
    u'su',
    u'al',
    u'lo',
    u'como',
    u'más',
    u'pero',
    u'sus',
    u'le',
    u'ya',
    u'o',
    u'este',
    u'sí',
    u'porque',
    u'esta',
    u'entre',
    u'cuando',
    u'muy',
    u'sin',
    u'sobre',
    u'también',
    u'me',
    u'hasta',
    u'hay',
    u'donde',
    u'quien',
    u'desde',
    u'todo',
    u'nos',
    u'durante',
    u'todos',
    u'uno',
    u'les',
    u'ni',
    u'contra',
    u'otros',
    u'ese',
    u'eso',
    u'ante',
    u'ellos',
    u'e',
    u'esto',
    u'mí',
    u'antes',
    u'algunos',
    u'qué',
    u'unos',
    u'yo',
    u'otro',
    u'otras',
    u'otra',
    u'él',
    u'tanto',
    u'esa',
    u'estos',
    u'mucho',
    u'quienes',
    u'muchos',
    u'cual',
    u'poco',
    u'ella',
    u'estar',
    u'estas',
    u'algunas',
    u'algo',
    u'nosotros',
    u'mi',
    u'mis',
    u'tú',
    u'te',
    u'ti',
    u'tu',
    u'tus',
    u'ellas',
    u'nosotras',
    u'vosostros',
    u'vosostras',
    u'os',
    u'mío',
    u'mía',
    u'míos',
    u'mías',
    u'tuyo',
    u'tuya',
    u'tuyos',
    u'tuyas',
    u'suyo',
    u'suya',
    u'suyos',
    u'suyas',
    u'nuestro',
    u'nuestra',
    u'nuestros',
    u'nuestras',
    u'vuestro',
    u'vuestra',
    u'vuestros',
    u'vuestras',
    u'esos',
    u'esas',
    u'estoy',
    u'estás',
    u'está',
    u'estamos',
    u'estáis',
    u'están',
    u'esté',
    u'estés',
    u'estemos',
    u'estéis',
    u'estén',
    u'estaré',
    u'estarás',
    u'estará',
    u'estaremos',
    u'estaréis',
    u'estarán',
    u'estaría',
    u'estarías',
    u'estaríamos',
    u'estaríais',
    u'estarían',
    u'estaba',
    u'estabas',
    u'estábamos',
    u'estabais',
    u'estaban',
    u'estuve',
    u'estuviste',
    u'estuvo',
    u'estuvimos',
    u'estuvisteis',
    u'estuvieron',
    u'estuviera',
    u'estuvieras',
    u'estuviéramos',
    u'estuvierais',
    u'estuvieran',
    u'estuviese',
    u'estuvieses',
    u'estuviésemos',
    u'estuvieseis',
    u'estuviesen',
    u'estando',
    u'estado',
    u'estada',
    u'estados',
    u'estadas',
    u'estad',
    u'he',
    u'has',
    u'ha',
    u'hemos',
    u'habéis',
    u'han',
    u'haya',
    u'hayas',
    u'hayamos',
    u'hayáis',
    u'hayan',
    u'habré',
    u'habrás',
    u'habrá',
    u'habremos',
    u'habréis',
    u'habrán',
    u'habría',
    u'habrías',
    u'habríamos',
    u'habríais',
    u'habrían',
    u'había',
    u'habías',
    u'habíamos',
    u'habíais',
    u'habían',
    u'hube',
    u'hubiste',
    u'hubo',
    u'hubimos',
    u'hubisteis',
    u'hubieron',
    u'hubiera',
    u'hubieras',
    u'hubiéramos',
    u'hubierais',
    u'hubieran',
    u'hubiese',
    u'hubieses',
    u'hubiésemos',
    u'hubieseis',
    u'hubiesen',
    u'habiendo',
    u'habido',
    u'habida',
    u'habidos',
    u'habidas',
    u'soy',
    u'eres',
    u'es',
    u'somos',
    u'sois',
    u'son',
    u'sea',
    u'seas',
    u'seamos',
    u'seáis',
    u'sean',
    u'seré',
    u'serás',
    u'será',
    u'seremos',
    u'seréis',
    u'serán',
    u'sería',
    u'serías',
    u'seríamos',
    u'seríais',
    u'serían',
    u'era',
    u'eras',
    u'éramos',
    u'erais',
    u'eran',
    u'fui',
    u'fuiste',
    u'fue',
    u'fuimos',
    u'fuisteis',
    u'fueron',
    u'fuera',
    u'fueras',
    u'fuéramos',
    u'fuerais',
    u'fueran',
    u'fuese',
    u'fueses',
    u'fuésemos',
    u'fueseis',
    u'fuesen',
    u'sintiendo',
    u'sentido',
    u'sentida',
    u'sentidos',
    u'sentidas',
    u'siente',
    u'sentid',
    u'tengo',
    u'tienes',
    u'tiene',
    u'tenemos',
    u'tenéis',
    u'tienen',
    u'tenga',
    u'tengas',
    u'tengamos',
    u'tengáis',
    u'tengan',
    u'tendré',
    u'tendrás',
    u'tendrá',
    u'tendremos',
    u'tendréis',
    u'tendrán',
    u'tendría',
    u'tendrías',
    u'tendríamos',
    u'tendríais',
    u'tendrían',
    u'tenía',
    u'tenías',
    u'teníamos',
    u'teníais',
    u'tenían',
    u'tuve',
    u'tuviste',
    u'tuvo',
    u'tuvimos',
    u'tuvisteis',
    u'tuvieron',
    u'tuviera',
    u'tuvieras',
    u'tuviéramos',
    u'tuvierais',
    u'tuvieran',
    u'tuviese',
    u'tuvieses',
    u'tuviésemos',
    u'tuvieseis',
    u'tuviesen',
    u'teniendo',
    u'tenido',
    u'tenida',
    u'tenidos',
    u'tenidas',
    u'tened',
    u'va',
    u'veni',
    u'vas',
    u'van',
    u'sido',
    u'viene',
    u'pe',
    u'po',
    u'pa',
    u'ahora',
    u'da',
    u'q',
    u'hace',
    u'ir',
    u'alguien',
    u'aqui',
    u'asi',
    u'pase',
    u'pasar',
    u'vayamos',
    u'iriamos',
    u'iran',
    u'vaya',
    u'id',
    u'echale',
    u'solo',
    u'sale',
    u'ido',
    u'lleva',
    u'lleve',
    u'llevar',
    u'llevarlo',
    u'llevan',
    u'sera',
    u'llevo',
    u'si',
    u'u',
    u'llevarla',
    u'llevando',
    u'hecho',
    u'llevariamos',
    u'llevaria',
    u'llevares',
    u'llevare',
    u'llevaremos',
    u'llevareis',
    u'llevaren',
    u'fuere',
    u'fueres'
    u'fuere',
    u'fueremos',
    u'terminara',
    u'fuereis',
    u'fueren',
    u'aca',
    u'voy',
    u'mas',
    u'luego',
    u'hagas',
    u've',
    u'haz',
    u'creo',
    u'sino',
    u'd',
    u'haga',
    u'alla',
    u'k',
    u'mt',
    u'm',
    u'kg',
    u'mb',
    u'ud',
    u'bg',
    u'uds',
    u'sr',
    u'sra',
    u'sras',
    u'sres',
    u'doc',
    u'dr',
    u'dra',
    u'cualquier',
    u'miss',
    u'eh',
    u'aun',
    u't',
    u'x',
    u'rt',
    u'llegue',
    u'llegar',
    u'ningun',
    u'tt',
    u'at',
    u'i',
    u'lt',
    u'vs',
    u'pd',
    u'c',
    u'porq',
    u'dm',
    u'esten',
    u'fm',
    u'xq',
    u'cp',
    u'asu',
    u'n',
    u'pue',
    u'gt',
    u'vi',
    u'ce',
    u'cd',
    u'siquiera',
    u'km',
    u'cc',
    u'am',
    u'pm',
    u'ah',
    u'ahi',
    u'ro',
    u'haganse',
    u'cuanta',
    u'er',
    u'do',
    u'to',
    u'vo',
    u'mo',
    u'amp',
    u'in',
    u'dejamos',
    u'on',
    u'h',
    u'hr',
    u'ar',
    u'sepa',
    u'hacen',
    u'hacia',
    u'darte',
    u's',
    u'hacer',
    u'haces',
    u'ht',
    u'gral',
    u'vao',
    u'vamo',
    u'ops',
    u'im',
    u'pto',
    u'lat',
    u'p',
    u'ii',
    u'iii',
    u'iv',
    u'v',
    u'xi',
    u'hice',
    u'nu',
    u'oh',
    u'tl',
    u'rts',
    u'tambien',
    u'lon',
    u'tb',
    u'l',
    u'by',
    u'dl',
    u'r',
    u'gs',
    u'xd',
    u'g',
    u'iba',
    u'j',
    u'ge',
    u'alli',
    u'tanta',
    u'hrs',
    u'ing',
    u'ls',
    u'it',
    u'ande',
    u'pq',
    u'vez',
    u'dia',
    u'segun',
    u'deberia',
    u'oe',
    u'etc',
    u'ft',
    u'dio',
    u'di',
    u'ke',
    u'dice',
    u'and',
    u'puedo',
    u'habre',
    u'serla',
    u'dos',
    u'ser',
    u'pues',
    u'hoy',
    u'san',
    u'pasa',
    u'todas',
    u'gran',
    u'deje',
    u'supe',
    u'vayas',
    u'sigo',
    u'cosa',
    u'siga',
    u'hizo',
    u'hazte',
    u'seran',
    u'vemos',
    u'estan',
    u'puso',
    u'tal',
    u'dan',
    u'vendra',
    u'tan',
    u'ta',
    u'echarle',
    u'nadie',
    u'yendo',
    u'dieron',
    u'haciendome',
    u'tres',
    u'cuatro',
    u'aquellos',
    u'cabe',
    u'na',
    u'abrir',
    u'unas',
    u'irse',
    u'den',
    u'decir',
    u'ok',
    u'sali',
    u'das',
    u'venia',
    u'parar',
    u'cu',
    u'jr',
    u'cruc',
    u'tener',
    u'pts',
    u'int',
    u'float',
    u'dira',
    u'goes',
    u'date',
    u'lado',
    u'dsps',
    u'dps',
    u'unl',
    u'nop',
    u'ac',
    u'cumplid',
    u'solta',
    u'sube',
    u'sobar',
    u'volve',
    u'algun',
    u'aver',
    u'conmigo',
    u'tws',
    u'xfavor',
    u'fabor',
    u'pal',
    u'hacias',
    u'echan',
    u'tenian',
    u'ant',
    u'dime',
    u'ix',
    u'aser',
    u'eligen',
    u'acs',
    u'casi',
    u'toy',
    u'haciendo',
    u'hallan',
    u'cabo',
    u'sigue',
    u'total',
    u'totales',
    u'tras',
    u'toda',
    u'verlos',
    u'pueden',
    u'vuelve',
    u'oye',
    u'par',
    u'digan',
    u'veia',
    u'debe',
    u'puede',
    u'doy',
    u'veces',
    u'dejo',
    u'an',
    u'tenes',
    u'aunque',
    u'llegan',
    u'visto',
    u're',
    u'fin',
    u'mire',
    u'tenia',
    u'ten',
    u'sigues',
    u'abran',
    u'seria',
    u'serlo',
    u'prox',
    u'mismo',
    u'haber',
    u'quedo',
    u'tomes',
    u'mismas',
    u'ver',
    u'haciamos',
    u'darse',
    u'ven',
    u'mio',
    u'ha'
]


def stopwords(lang=None):
    if lang == 'eng':
        return ENG
    elif lang == 'spa':
        return SPA
    return ENG + SPA
