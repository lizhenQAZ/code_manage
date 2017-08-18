<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>hello beginner!</title>
</head>
<body>
<!-- this is body -->
<!-- today is <%= new java.util.Date().toString() %> -->
JAVA输出表达式<%="hello world" %>
<br/>
<%!
	String str = "hello beginner";
%>
<%
	/* this is body */
	//String str = "hello beginner";
	out.println(str);
%>
<br/>
<br/>
<a href="<%= request.getContextPath() %>/20/hello.jsp">hello.jsp</a>
</body>
</html>