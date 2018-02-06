from django.test import TestCase


# 引入模型类模块
from .models import *


# 1.插入数据
datas = [
    ('社会新闻', '驾照被扣男子以跳河相相逼要求归还 被拘留十日 ', '近日，铜川市交警支队第一大队黄堡中队民警在对过往大货车进行交通违法路查时，发现一辆大货车存在抛撒载运物情况，交警立即将大车拦停，在对货车司机进行纠正与处罚期间，遭到该司机多次阻挠执法，甚至还以跳河对交警进行威胁。最终，该司机被处以行政拘留10日处罚。', ),
    ('地方新闻', '最受求职者欢迎城市 深圳排第三 ', '秋季求职期，全国最受求职者欢迎的城市中，深圳排行第三。智联招聘昨日公布的秋季，全国排名第三。基金/证券/期货/投资的平均月薪最高，为11623元。', ),
    ('军事新闻', '中国远程火箭炮夜间齐射犹如流星雨 A300实力雄厚达导弹水平 ', '中国火箭炮技术已经处在世界领先地位，在历次演习中频频亮相的解放军远程火箭炮，让任何对手都不敢轻视，并且中国火箭炮精确打击目标能力堪比某些短程导弹。', ),
]
for data in datas:
    # 插入新闻分类数据
    news_cag = NewsCategory()
    news_cag.cag_name = data[0]
    news_cag.save()

    # 插入新闻详情数据
    news_info = NewsInfo()
    news_info.news_title = data[1]
    news_info.news_content = data[2]
    news_info.news_category = news_cag
    news_info.save()


# # 2.修改数据
# news_info = NewsInfo.objects.get(id=1)
# print(news_info)
# news_info.news_title = "国际新闻"
# news_info.save()


# # 3.查询数据
# # 查询所有数据
# news_info = NewsInfo.objects.all()
# print(news_info)
# for index, item in enumerate(news_info):
#     print('第', index+1, '条数据', '  ---  ', '新闻标题', ': ', item.news_title, ' 新闻内容', ': ', item.news_content)

# # 查询指定数据
# news_info = NewsInfo.objects.get(pk=1)
# print(news_info)
# print('指定pk=1的数据', '  ---  ', '新闻标题', ': ', news_info.news_title, ' 新闻内容', ': ', news_info.news_content)


# 4.删除数据
# news_info = NewsInfo.objects.get(pk=1)
# print(news_info)
# news_info.delete()
# print('删除pk=1的数据', '  ---  ', '新闻信息对象', ': ', NewsInfo.objects.all())
