package com.lizhen.test;

import java.sql.Connection;

import com.lizhen.dao.UserDao;
import com.lizhen.dao.impl.UserDaoImpl;
import com.lizhen.entity.User;
import com.lizhen.util.ConnectionFactory;

public class UserDaoTest {

	public static void main(String[] args) {
		Connection conn=null;
		try {
			conn=ConnectionFactory.getInstance().makeConnection();
			conn.setAutoCommit(false);
			
			UserDao userDao=new UserDaoImpl();
			User tom=new User();
			tom.setId((long)10);
			tom.setName("Tom");
			tom.setPassword("123456");
			tom.setEmail("tom@qq.com");
			userDao.save(conn, tom);
			
			conn.commit();
		} catch (Exception e) {
			System.out.println(e);
			e.printStackTrace();
			try {
				conn.rollback();
			} catch (Exception e2) {
				System.out.println(e2);
				e2.printStackTrace();
			}
			finally {
				try {
					if (null != conn) {
						conn.close();
					}
				} catch (Exception e3) {
					e3.printStackTrace();
				}
			}
		}
	}

}
