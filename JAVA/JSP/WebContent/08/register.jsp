<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>注册信息</title>
</head>
<body>
<form action="" method="post">
<input type="text" name="username"/>
<input type="submit" value="提交"/>
</form>
<%= request.getMethod() %><br/>
<%= request.getRequestURI() %><br/>
<%= request.getProtocol() %><br/>
<%= request.getServerName() %><br/>
<%= request.getServerPort() %><br/>
<%= request.getRemoteAddr() %><br/>
<%= request.getRemoteHost() %><br/>
<%= request.getParameter("username") %><br/>
</body>
</html>