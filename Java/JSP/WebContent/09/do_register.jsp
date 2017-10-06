<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% 
	String username=request.getParameter("username");
	String skills="";
	String[] skillArr=request.getParameterValues("skills");
	
	if(skillArr !=null && skillArr.length>0){
		for(String skill : skillArr){
			skills = skills + skill + " ";
		}
	}
	request.setAttribute("username", username);
	request.setAttribute("skills", skills);
%>
<jsp:forward page="welcome.jsp"></jsp:forward>