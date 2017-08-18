<%@page import="com.lizhen.servlet.CheckServlet"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
<script type="text/javascript">
	function check(form){
		if(document.forms.LoginForm.uname.value==""){
			alert("enter username!");
			document.forms.LoginForm.uname.focus();
			return false;
		}
		if(document.forms.LoginForm.upwd.value==""){
			alert("enter password!");
			document.forms.LoginForm.upwd.focus();
			return false;
		}
	}
</script>
</head>
<body>
	<form action="<%= request.getContextPath() %>/LoginServlet19" method="post" name="LoginForm">
		<table border="1" cellspacing="0" cellpadding="5" bordercolor="sliver" align="center">
			<tr>
				<td colspan="2" align="center" bgcolor="#E8E8E8">用户登录</td>
			</tr>
			<tr>
				<td>用户名:</td>
				<td><input type="text" name="uname"/></td>
			</tr>
			<tr>
				<td>密码:</td>
				<td><input type="password" name="upwd"/></td>
			</tr>
			<tr>
				<td colspan="2" align="center">
					<input type="submit" value="submit" onclick="return check(this);"/>
					<input type="reset" value="reset"/>
				</td>
			</tr>
		</table>
	</form>
</body>
</html>