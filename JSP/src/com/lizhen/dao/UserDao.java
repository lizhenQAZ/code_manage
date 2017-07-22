package com.lizhen.dao;

import java.sql.Connection;
import java.sql.SQLException;

import com.lizhen.entity.User;

public interface UserDao {
	public void save(Connection conn,User user) throws SQLException;
	public void update(Connection conn,Long id,User user) throws SQLException;
	public void delete(Connection conn,User user) throws SQLException;
}
