<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>response03</title>
</head>
<body>
<%
	Cookie myCookie=new Cookie("lizhen","123");
    myCookie.setMaxAge(3600);
    response.addCookie(myCookie);
%>
</body>
</html>