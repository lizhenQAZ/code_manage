# coding: utf-8
def clip(text, max_len=80):
    """在max_len前面或后面的第一个空格处截断文本"""
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


def tag(name, *content, cls=None, **attrs):
    """生成一个或多个HTML标签"""
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
    else:
        attr_str = ''
    if content:
        return '\n'.join('<%s%s>%s</%s>' % (name, attr_str, c, name) for c in content)
    else:
        return '<%s%s />' % (name, attr_str)
if __name__ == '__main__':
    print(clip.__defaults__)
    print(clip.__code__)  # doctest: +ELLIPSIS
    print(clip.__code__.co_varnames)
    print(clip.__code__.co_argcount)
    print()
    from inspect import signature
    sig = signature(clip)
    print(sig)  # doctest: +ELLIPSIS
    print(str(sig))
    for name, param in sig.parameters.items():
        print(param.kind, ':', name, '=', param.default)
    print()
    sig = signature(tag)
    my_tag = {'name': 'img', 'title': 'Sunset Boulevard', 'src': 'sunset.jpg', 'cls': 'framed'}
    bound_args = sig.bind(**my_tag)
    print(bound_args)
    for name, value in bound_args.arguments.items():
        print(name, '=', value)
    del my_tag['name']
    try:
        bound_args = sig.bind(**my_tag)
    except Exception as e:
        print(e)
