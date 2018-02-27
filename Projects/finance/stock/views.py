from django.shortcuts import render
from .models import *
from django.http import HttpResponse


def index(request):
    # 查询数据库
    info_list = Info.objects.all()
    html = ''''''
    html_template = '''
        <tr>
            <td>%d</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
            </td>
        </tr>
    '''
    # print(info_list)
    for info in info_list:
        # print(info.id)
        html += html_template % (info.id, info.code, info.short, info.chg, info.turnover, info.price, info.highs,
                                 info.time, info.code)
    content = html
    return render(request, 'index.html', locals())


def center(request):
    focus_list = Focus.objects.all()
    html = ''''''
    html_template = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/stock/update/%s/"> <span class="glyphicon
                glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
    '''
    # print(focus_list)
    for focus in focus_list:
        # print(focus.id)
        html += html_template % (focus.focus_info.code, focus.focus_info.short, focus.focus_info.chg,
                                 focus.focus_info.turnover, focus.focus_info.price, focus.focus_info.highs,
                                 focus.note_info, focus.focus_info.code, focus.focus_info.code,)
    content = html
    return render(request, 'stock/center.html', locals())


def add(request, param):
    # 判断是否已经关注成功
    ret = Info.objects.get(code=param).focus_set.all()
    # print(ret)
    if ret:
        print("已经关注，无需加入")
        return HttpResponse("已经关注，无需加入")
    focus = Focus()
    print(Info.objects.get(code=param).id)
    # 这是属性
    focus.focus_info_id = Info.objects.get(code=param).id
    focus.save()
    print("关注成功")
    return HttpResponse("关注成功")


def delete(request, param):
    # 判断是否已经关注成功
    ret = Info.objects.get(code=param).focus_set.all()
    print(ret)
    ret.delete()
    print("取消关注成功")
    return HttpResponse("取消关注成功")


def update(request, param):
    code = param
    if request.GET.get('message', ''):
        focus = Focus.objects.get(focus_info__code=code)
        print(focus)
        focus.note_info = request.GET.get('message')
        print(focus.note_info)
        focus.save()
        print("修改成功")
        return HttpResponse("修改成功")
    note_info = Focus.objects.get(focus_info__code=code).note_info
    print(locals())
    return render(request, 'stock/update.html', locals())
