<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>注册信息处理</title>
</head>
<body>
<jsp:useBean id="user" class="com.lizhen.entity.UseEntity"></jsp:useBean>
<jsp:setProperty property="username" name="user"/>
<jsp:setProperty property="password" name="user"/>
<jsp:getProperty property="username" name="user"/>
<jsp:getProperty property="password" name="user"/>
</body>
</html>