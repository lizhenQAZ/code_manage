<%@page import="javax.xml.ws.Response"%>
<%@page import="javax.print.attribute.ResolutionSyntax"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	session.invalidate();
	response.setHeader("refresh", "2;URL=welcome.jsp");
%>