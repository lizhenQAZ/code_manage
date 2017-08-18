<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Login error</title>
</head>
<body>
Login error!<br/>
<%= request.getParameter("uname") %><br/>
<%= request.getParameter("upwd") %><br/>
<a href='<%= request.getContextPath() %>/17/Login.jsp'>return to login interface</a>
</body>
</html>