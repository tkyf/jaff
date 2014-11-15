#encoding: utf-8
import MeCab

pos_index = 0
try:
    tagger = MeCab.Tagger('-Ochasen')
    pos_index = 3
except RuntimeError:
    tagger = MeCab.Tagger('-Ounidic')
    pos_index = 4


class MorphedChar:
    """[CLASSES] 形態素解析された一つの文字を表す．
    この文字は品詞と単語中での位置を持つ
    """
    def __init__(self, surface, pos, position):
        """[FUNCTIONS] 文字の表層、品詞、単語内での位置を受け取り格納する

        Keyword arguments:
        sruface -- surface of charactor : unicode
        pos     -- surface of word      : unicode
        position -- position of charactor in word. :unicode
                    B: begin of word. I: inter of word.

        例： surface  : 人
             pos      : 名詞
             position : B
        """

        self.surface = surface
        self.pos = pos
        self.position = position  # B:先頭，I:文中


def tagging(src):
    """[FUNCTIONS]文字列を受け取り，MeCabで形態素解析して、
    MorphedCharのリストにして返す

    Keyword arguments:
    src       -- 文字列

    Return value:
    [MorphedChar]

    """
    morphed = tagger.parse(src)

    splited = morphed.split(u'\n')

    cs = []
    for L in splited:
        if L.startswith(u'EOS'):
            break
        feature = L.split(u'\t')
        cs.append(MorphedChar(feature[0][0], feature[pos_index], u'B'))

        n = len(feature[0])
        # 2文字以上からなる単語の場合
        if n > 1:
            for i in range(0, n - 1):
                cs.append(MorphedChar(feature[0][i+1], feature[pos_index], u'I'))
    return cs
