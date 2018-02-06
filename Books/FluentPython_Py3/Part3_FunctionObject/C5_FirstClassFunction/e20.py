# coding: utf-8
from inspect import signature
# 提取函数签名中注解


def clip(text: str, max_len: 'int > 0'=80) -> str:
    """在max_len前面或后面的第一个空格处截断文本
    """
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            space_after = text.rfind(' ', max_len)
            if space_after >= 0:
                end = space_after
    if end is None:  # 没找到空格
        end = len(text)
    return text[:end].rstrip()
if __name__ == '__main__':
    sig = signature(clip)
    print(sig.return_annotation)
    for param in sig.parameters.values():
        note = repr(param.annotation).ljust(13)
        print(note, ':', param.name, '=', param.default)
