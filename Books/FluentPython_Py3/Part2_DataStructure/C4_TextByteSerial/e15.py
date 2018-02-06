# coding: utf-8
# 去掉全部组合记号
import unicodedata
# 去掉全部变音符号


def shave_marks(txt):
    norm_txt = unicodedata.normalize('NFD', txt)
    shaved = ''.join(c for c in norm_txt if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', shaved)
if __name__ == '__main__':
    order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
    print(shave_marks(order))
    Greek = 'Zέφupoς, Zéfiro'
    print(shave_marks(Greek))
