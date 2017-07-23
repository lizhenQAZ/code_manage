package com.lizhen.filter;

import java.io.IOException;
import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;

@WebFilter("/FilterTwo")
public class FilterTwo implements Filter {

    public FilterTwo() {
    	System.out.println("-----FilterTwo构造函数-----");
    }

	public void init(FilterConfig fConfig) throws ServletException {
    	System.out.println("-----FilterTwo初始化方法-----");
	}

	public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
		System.out.println("-----开始执行FilterTwo doFilter方法-----");
		chain.doFilter(request, response);
		System.out.println("-----结束执行FilterTwo doFilter方法-----");
	}
	
	public void destroy() {
		System.out.println("-----FilterTwo销毁方法-----");
	}

}
