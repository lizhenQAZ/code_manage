package com.lizhen.entity;

import java.io.Serializable;

public class UseEntity implements Serializable{
	private String username;
	private String password;
	public UseEntity() {
		super();
	}
	public String getUsername() {
		return username;
	}
	public void setUsername(String username) {
		this.username = username;
	}
	public String getPassword() {
		return password;
	}
	public void setPassword(String password) {
		this.password = password;
	}
}
