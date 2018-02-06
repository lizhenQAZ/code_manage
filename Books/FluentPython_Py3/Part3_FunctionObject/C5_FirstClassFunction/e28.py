# coding: utf-8
# functools.partial绑定多个参数


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
    print(tag)
    from functools import partial
    picture = partial(tag, 'img', cls='pic-frame')
    print(picture(src='wumpus.jpeg'))
    print(picture)
    print(picture.func)
    print(picture.args)
    print(picture.keywords)
