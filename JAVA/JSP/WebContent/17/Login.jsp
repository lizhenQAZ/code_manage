<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>login page</title>
</head>
<body>
	<form action="<%= request.getContextPath() %>/LoginServlet" method="get">
	<input type="text" name="uname"/><br/>
	<input type="password" name="upwd"/><br/>
	<input type="submit" value="Login"/>
	<input type="reset" value="Reset"/>
	</form>
</body>
</html>