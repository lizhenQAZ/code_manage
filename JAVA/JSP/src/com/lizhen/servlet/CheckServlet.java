package com.lizhen.servlet;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.lizhen.entity.User;
import com.lizhen.service.CheckUserService;

/**
 * Servlet implementation class CheckServlet
 */
@WebServlet("/CheckServlet")
public class CheckServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private CheckUserService cku=new CheckUserService();
    public CheckServlet() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		doPost(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String uname=request.getParameter("uname");
		String passwd=request.getParameter("upwd");
		RequestDispatcher rd =null;
		String forward=null;
		if (uname ==null || passwd==null) {
			request.setAttribute("msg", "username or password is null");
			rd=request.getRequestDispatcher("/18/Login.jsp");
			rd.forward(request, response);
		}else {
			User user=new User();
			user.setName(uname);
			user.setPassword(passwd);
			boolean bool=cku.check(user);
			if (bool) {
				forward="/18/success.jsp";
			}else {
				request.setAttribute("msg", "username or password is wrong");
				forward="/18/error.jsp";
			}
				rd=request.getRequestDispatcher(forward);
				rd.forward(request, response);
		}
	}

}
