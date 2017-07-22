package com.lizhen.dao.impl;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import com.lizhen.dao.UserDao;
import com.lizhen.entity.User;

public class UserDaoImpl implements UserDao {

	@Override
	public void save(Connection conn, User user) throws SQLException {
		String insertSql="INSERT INTO user_tbl(id,name,password,email) VALUES (?,?,?,?)";
		PreparedStatement ps =conn.prepareCall(insertSql);
		ps.setLong(1, user.getId());
		ps.setString(2, user.getName());
		ps.setString(3, user.getPassword());
		ps.setString(4, user.getEmail());
		ps.execute();
	}

	@Override
	public void update(Connection conn, Long id, User user) throws SQLException {
		String updateSql="UPDATE user_tbl SET name=?, password=?, email=? WHERE id=?";
		PreparedStatement ps =conn.prepareStatement(updateSql);
		ps.setString(1, user.getName());
		ps.setString(2, user.getPassword());
		ps.setString(3, user.getEmail());
		ps.setLong(4, id);
		ps.execute();
	}

	@Override
	public void delete(Connection conn, User user) throws SQLException {
		String deleteSql="DELETE FROM user_tbl WHERE user=?";
		PreparedStatement ps =conn.prepareStatement(deleteSql);
		ps.setString(1, user.getName());
		ps.execute();
	}

}
