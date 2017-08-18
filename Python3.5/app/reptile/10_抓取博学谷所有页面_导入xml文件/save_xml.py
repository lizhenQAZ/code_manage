import global_data
import xml.dom.minidom


def create():
    global_data.g_xml_fd = open(global_data.g_xml_filename, 'w', encoding='utf-8')


def create_dom():
    impl = xml.dom.minidom.getDOMImplementation()
    global_data.g_xml_dom = impl.createDocument(None, 'info', None)
    root = global_data.g_xml_dom.documentElement
    temp_list = global_data.g_xml_websites_list
    websites = global_data.g_xml_dom.createElement('websites')
    websites.setAttribute('id', temp_list[0])
    websites_value = global_data.g_xml_dom.createTextNode(temp_list[1])
    websites.appendChild(websites_value)
    root.appendChild(websites)


def write():
    create_dom()
    f = global_data.g_xml_fd
    global_data.g_xml_dom.writexml(f, addindent='\t', newl='\n', encoding='utf-8')


def close():
    global_data.g_xml_fd.close()


def __xml_main():
    create()
    temp_list = ['1', 'www.buxuegu.com']
    global_data.g_xml_websites_list = temp_list
    write()
    temp_list = ['1', 'www.baidu.com']
    global_data.g_xml_websites_list = temp_list
    write()
    close()


if __name__ == '__main__':
    __xml_main()
