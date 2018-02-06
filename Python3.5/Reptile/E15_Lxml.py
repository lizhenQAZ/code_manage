#coding:utf-8

from lxml import etree


text = ''' <div> <ul> 
                <li class="item-1"><a href="link1.html"></a></li> 
                <li class="item-1"><a href="link2.html">second item</a></li> 
                <li class="item-inactive"><a href="link3.html">third item</a></li> 
                <li class="item-1"><a href="link4.html">fourth item</a></li> 
                <li class="item-0"><a href="link5.html">fifth item</a> 
         </ul> </div> '''
html = etree.HTML(text)
# print (type(html))
# print (dir(html))
# print (etree.tostring(html))

# text_list = html.xpath('//li[@class="item-1"]/a/text()')
# link_list = html.xpath('//li[@class="item-1"]/a/@href')
# for data in zip(text_list,link_list):
#     print (data)

node_list = html.xpath('//li[@class="item-1"]/a')
# print (type(node_list[0]))
for  node in node_list:
    text = node.xpath('./text()')[0] if len(node.xpath('./text()')) > 0 else None
    link = node.xpath('./@href')[0]
    print (text,link)
