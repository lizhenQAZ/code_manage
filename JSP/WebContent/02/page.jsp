<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
    import ="java.util.ArrayList,java.util.LinkedList"
    errorPage ="handle_error.jsp"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	ArrayList arrayList = new ArrayList();
	arrayList.add(1);
	arrayList.add(2);
	
	LinkedList linkedList = new LinkedList();
	linkedList.add(1);
	linkedList.add(2);
	
	int a =10;
	int b =0;
	System.out.print(a/b);
%>

</body>
</html>