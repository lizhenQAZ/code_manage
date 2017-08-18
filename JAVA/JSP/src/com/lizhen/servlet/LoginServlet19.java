package com.lizhen.servlet;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
public class LoginServlet19 extends HttpServlet {
	private static final long serialVersionUID = 1L;
    public LoginServlet19() {
        super();
    }
    
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request, response);
	}
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("-----doPost-----");
		String username=request.getParameter("uname");
		String password=request.getParameter("upwd");
		System.out.println(username);
		System.out.println(password);
		if (username.equals("李震")&&password.equals("123456")) {
			String forward ="/19/success.jsp";
			RequestDispatcher rd =request.getRequestDispatcher(forward);
			rd.forward(request, response);
		}else {
			String forward ="/19/error.jsp";
			RequestDispatcher rd =request.getRequestDispatcher(forward);
			rd.forward(request, response);
		}
	}

}
