#!/usr/bin/env python
# coding:utf-8

def jaff(str1, str2):
    import mecab_wrapper
    import alignment.align

    a = alignment.align.align(str1, str2)
    m = mecab_wrapper.tagging(str1)
    pos_alignment = pos_align(a, m)
    
    return (pos_alignment)

def pos_align(alignment, tags, blank="\t", delimiter="\t"):
    base_string = alignment[0] 
    target_string = alignment[1] 


    for i, c in enumerate(base_string):
        if c == blank:
            tags.insert(i, None)

    base_word_list = []
    target_word_list = []
    pos_list = []
    base_word = ''
    target_word = ''

    for j, (base_char, target_char, tag) in enumerate(zip(base_string, target_string, tags)):
        base_word += base_char
        target_word += target_char
        if tag is None:
            pass
        elif  tag['position'] == 'E':
            base_word = base_word.replace(blank, "")
            target_word = target_word.replace(blank, "")
            base_word_list.append(base_word)
            target_word_list.append(target_word)
            pos_list.append(tag['pos'])
            base_word = ''
            target_word = ''

    if target_word != "":
        target_word_list[-1] += target_word

    return delimiter.join(base_word_list), delimiter.join(target_word_list), delimiter.join(pos_list)

def main():
    import sys

    if len(sys.argv) != 3:
        print("Usage: $ python jaff.py base_string target_string")
        sys.exit()

    base = sys.argv[1]
    target = sys.argv[2]

    jaff(base, target)


if __name__ == "__main__":
    main()
