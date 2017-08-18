<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>session示例</title>
</head>
<body>
<%= session.getId() %><br/>
<%= new java.util.Date(session.getCreationTime()).toString() %><br/>
<%= new java.util.Date(session.getLastAccessedTime()).toString() %><br/>
<%= session.getMaxInactiveInterval() %><br/>
</body>
</html>