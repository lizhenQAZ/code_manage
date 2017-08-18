package com.lizhen.servlet;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LoginServlet20 extends HttpServlet {
	private static final long serialVersionUID = 1L;
    public LoginServlet20() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String uname= request.getParameter("uname");
		String passwd= request.getParameter("upwd");
		String returnUri= request.getParameter("return_uri");
		
		System.out.println(uname);
		System.out.println(passwd);
		System.out.println(returnUri);
		
		RequestDispatcher rd = null;
		if (uname == null || passwd == null) {
			request.setAttribute("msg", "username or password is null!!!");
			rd = request.getRequestDispatcher("/20/login.jsp");
			rd.forward(request, response);
		}else {
			if (uname.equals("李震") && passwd.equals("123456")) {
				request.getSession().setAttribute("flag", "login_success");
				if (returnUri != null) {
					rd = request.getRequestDispatcher(returnUri);
					rd.forward(request, response);
				}else {
					rd = request.getRequestDispatcher("/20/index.jsp");
					rd.forward(request, response);
				}
			}else {
				request.getSession().setAttribute("flag", "login_error");
				request.setAttribute("msg", "username or password is wrong!");
				rd = request.getRequestDispatcher("/20/login.jsp");
				rd.forward(request, response);
			}
		}
	}

}
