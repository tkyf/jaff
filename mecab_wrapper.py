#encoding: utf-8

import MeCab

pos_index = 0
try:
    tagger = MeCab.Tagger('-Ochasen')
    pos_index = 3
except RuntimeError:
    tagger = MeCab.Tagger('-Ounidic')
    pos_index = 4

def tagging(src):

    """[FUNCTIONS] 文字列を受け取り， MeCab で形態素解析して、
    dict の list にして返す。
    dict は文字列中の1文字を表す。
    dict は以下の key を持つ。
      surface : 1文字の表層
      pos     : 形態素解析によって品詞
      position: 単語中の位置（I：単語の先頭または中間。 E：単語の末尾） 

    Keyword arguments:
    src       -- 文字列

    Return value:
    [dict]

    """
    tagged = tagger.parse(src)
    word_list = tagged.split(u'\n')

    character_dict_list = [] 
    for word in word_list:
        if word.startswith('EOS'):
            break
        character_dict_list += characterize(word)
    return character_dict_list

def characterize(word):
    rv = []

    d = {}
    feature = word.split(u'\t')
    d['surface'] = feature[0][0]
    d['pos']     = feature[pos_index]

    # 単語の文字数を取得
    n = len(feature[0])
    if n == 1 :
        d['position'] = 'E'
    else:
        d['position'] = 'I'

    rv.append(d)

    # 2文字以上からなる単語の場合
    if n > 1:
        for i in range(0, n - 1):
            d = {}
            d['surface'] = feature[0][i + 1]
            d['pos']     = feature[pos_index]
            if i == (n - 1):
                d['position'] = 'E'
            else:
                d['position'] = 'I'
            rv.append(d)
    return rv

