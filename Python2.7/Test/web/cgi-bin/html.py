#!/usr/bin/python
def start_response(resp="text/html"):
    return 'Content-type: '+resp+'\n\n'
def start_form(url='',form_type="GET"):
    return '<form action="'+url+'" method="'+form_type+'">'
def end_form(submit_msg="Submit"):
    return '<p></p><input type="submit" value="' +submit_msg+'">'
def input_label(name,placeholder="",value="",readonly=None):
    if readonly is None:
        return '<input type="text" value="'+value+'" name="'+name+'" placeholder="'+placeholder+'">'
    else:
        return '<input type="text" value="'+value+'" name="'+name+'" placeholder="'+placeholder+'" readonly="'+readonly+'">'
def context(word):
    return  word
def start_div(align,style):
    return '<div align="'+align+'" style="'+style+'">'
def end_div():
    return '</div>'
def img(src):
    return '<img src="'+src+'">'