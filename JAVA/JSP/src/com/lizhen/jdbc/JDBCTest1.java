package com.lizhen.jdbc;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
public class JDBCTest1 {
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
	public static void insert() {
		Connection conn=getConnection();
		try {
			String sql = "INSERT INTO user_tbl(id,name,password,email)" +
						 "VALUES('3','Tom','123456','tom@gmail.com')";
			Statement st = conn.createStatement();
			int count = st.executeUpdate(sql);
			System.out.println("查询到了"+count+"次");
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void update() {
		Connection conn=getConnection();
		try {
			String sql = "UPDATE user_tbl SET email='tom@126.com' where name='Tom'";
			Statement st = conn.createStatement();
			int count = st.executeUpdate(sql);
			System.out.println("更新了"+count+"次");
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void delete() {
		Connection conn=getConnection();
		try {
			String sql = "DELETE FROM user_tbl where name='Tom'";
			Statement st = conn.createStatement();
			int count = st.executeUpdate(sql);
			System.out.println("删除了"+count+"次");
			conn.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	public static void main(String[] args) {
//		insert();
//		update();
		delete();
	}
}