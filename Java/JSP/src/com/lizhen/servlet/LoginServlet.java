package com.lizhen.servlet;
import java.io.IOException;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class LoginServlet extends HttpServlet {
	private static final long serialVersionUID = 3796888073190440543L;

//	@Override
//	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
//		String username=req.getParameter("uname");
//		String password=req.getParameter("upwd");
//		System.out.println(username);
//		System.out.println(password);
//	}

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		System.out.println("-----doGet-----");
//		String username=req.getParameter("uname");
//		String password=req.getParameter("upwd");
//		System.out.println(username);
//		System.out.println(password);
		doPost(req, resp);
	}

	@Override
	protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		System.out.println("-----doPost-----");
		String username=req.getParameter("uname");
		String password=req.getParameter("upwd");
		System.out.println(username);
		System.out.println(password);
		if (username.equals("lizhen")&&password.equals("lizhen")) {
//			resp.sendRedirect(req.getContextPath()+"/17/success.jsp");
			String forward ="/17/success.jsp";
			RequestDispatcher rd =req.getRequestDispatcher(forward);
			rd.forward(req, resp);
		}else {
//			resp.sendRedirect(req.getContextPath()+"/17/error.jsp");
			String forward ="/17/error.jsp";
			RequestDispatcher rd =req.getRequestDispatcher(forward);
			rd.forward(req, resp);
		}
	}

}
