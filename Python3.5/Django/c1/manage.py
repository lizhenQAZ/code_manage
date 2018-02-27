#!/usr/bin/env python
"""
功能：
1.渲染模板：
    1.render(request, 'news/template.html', locals())
    2.template = loader.get_template("news/template.html")
      context = {"title": "军事新闻", 'content': "大战一触即发"}
      new_template = template.render(context)
      return HttpResponse(new_template)
2.查询同一对象的所有数据：NewsCategory.objects.all()
3.查询一对多的所有数据：
    cag = NewsCategory.objects.get(pk=cag_id)
    news_list = cag.newsinfo_set.all()
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "c1.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
