package com.lizhen.filter;

import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;

@WebFilter("/FilterOne")
public class FilterOne implements Filter {

    public FilterOne() {
    	System.out.println("-----FilterOne构造函数-----");
    }
	
	public void init(FilterConfig fConfig) throws ServletException {
    	System.out.println("-----FilterOne初始化方法-----");
	}

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		System.out.println("-----开始执行FilterOne doFilter方法-----");
		chain.doFilter(request, response);
		System.out.println("-----结束执行FilterOne doFilter方法-----");
	}
	
	public void destroy() {
		System.out.println("-----FilterOne销毁方法-----");
	}
}
