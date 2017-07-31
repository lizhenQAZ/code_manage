#!/usr/bin/python
import cgi,cgitb
from html import *
form1=cgi.FieldStorage()

NUM1=form1.getvalue("NUM1")
NUM2=form1.getvalue("NUM2")
result=None

if not NUM1 is None and not NUM2 is None:
    NUM1=int(NUM1)
    NUM2=int(NUM2)
    result=NUM1+NUM2

print start_response()
print start_div('center','margin-top:40px;')
print img('../add.jpg')
print end_div()
print start_div('center','margin-top:60px;')
print start_form()
print input_label("NUM1","adder1")
print '+'
print input_label("NUM2","adder2")
print '='
if result is None:
    print input_label("result","result","","readonly")
else:
    print input_label("result1", "result-1", str(result), "readonly")
print end_form()
print end_div()