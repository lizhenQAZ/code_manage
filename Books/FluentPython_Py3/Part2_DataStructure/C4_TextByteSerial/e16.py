# coding: utf-8
import unicodedata
import string


# 把拉丁基字符中所有的变音符号删除
def shave_marks_latin(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base:
            continue  # 忽略拉丁基字符上的变音符号
        keepers.append(c)
        # 如果不是组合字符，那就是新的基字符
        if not unicodedata.combining(c):
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved)

if __name__ == '__main__':
    order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
    print(shave_marks_latin(order))
    Greek = 'Zέφupoς, Zéfiro'
    print(shave_marks_latin(Greek))
