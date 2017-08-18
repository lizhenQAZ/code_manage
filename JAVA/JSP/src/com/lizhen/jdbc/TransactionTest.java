package com.lizhen.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class TransactionTest {
	public static Connection getConnection() {
		Connection conn=null;
		try {
			Class.forName("com.mysql.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/jsp_db?useSSL=false","root","root");
		} catch (Exception e) {
			e.printStackTrace();
		}
		return conn;
	}
	public static void insertUserData() {
		Connection conn=getConnection();
		try {
			String sql = "INSERT INTO user_tbl(id,name,password,email)" +
						 "VALUES('3','Tom','123456','tom@gmail.com')";
			Statement st = conn.createStatement();
			int count = st.executeUpdate(sql);
			System.out.println("用户表插入了"+count+"次");
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void insertAddressData() {
		Connection conn=getConnection();
		try {
			String sql = "INSERT INTO address_tbl(id,city,country,user_id)" +
						 "VALUES('1','shanghai','china','10')";
			Statement st = conn.createStatement();
			int count = st.executeUpdate(sql);
			System.out.println("地址表插入了"+count+"次");
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {
		insertUserData();
		insertAddressData();
	}

}
