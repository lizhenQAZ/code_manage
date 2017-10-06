<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Login error</title>
<style type="text/css">
body{
	color: #000;
	font-size: 14px;
	margin: 20px auto;
}

#messege{
	text-align: center;
}
</style>
</head>
<body>
<div id="messege">
	Login error!<br/>
	<%= request.getParameter("uname") %><br/>
	<%= request.getParameter("upwd") %><br/>
	<a href='<%= request.getContextPath() %>/18/login.jsp'>return to login interface</a>
</div>
</body>
</html>