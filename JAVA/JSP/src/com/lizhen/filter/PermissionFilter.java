package com.lizhen.filter;
import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
public class PermissionFilter implements Filter {
    public PermissionFilter() {
    }
	public void init(FilterConfig fConfig) throws ServletException {
	}
	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		HttpServletRequest req =(HttpServletRequest)request;
		HttpServletResponse resp =(HttpServletResponse)response;
		String servletPath = req.getServletPath();
		HttpSession session = req.getSession();
		String flag=(String)session.getAttribute("flag");
		if (servletPath !=null && servletPath.equals("/20/index.jsp") || 
		    servletPath.equals("/20/login.jsp") || servletPath.equals("/LoginServlet20")) {
			chain.doFilter(request, response);
		}else {
			if (flag!=null &&flag.equals("login_success")) {
				chain.doFilter(request, response);
			}else if (flag !=null && flag.equals("login_error")) {
				req.setAttribute("msg", "login fail....");
				req.setAttribute("return_uri", servletPath);
				RequestDispatcher rd=request.getRequestDispatcher("/20/login.jsp");
				rd.forward(req, resp);
			}
			else {
				req.setAttribute("msg", "never login....");
				req.setAttribute("return_uri", servletPath);
				RequestDispatcher rd=request.getRequestDispatcher("/20/login.jsp");
				rd.forward(req, resp);
			}
		}
		
	}
	public void destroy() {
	}
}
