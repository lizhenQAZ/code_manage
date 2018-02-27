# coding=utf-8
from django.shortcuts import render
from stock.models import Info


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
