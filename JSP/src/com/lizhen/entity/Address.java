package com.lizhen.entity;

public abstract class Address extends IdEntity {
	private String city;
	private String country;
	private int userId;
	public String getCity() {
		return city;
	}
	public void setCity(String city) {
		this.city = city;
	}
	public String getCountry() {
		return country;
	}
	public void setCountry(String country) {
		this.country = country;
	}
	public int getUserId() {
		return userId;
	}
	public void setUserId(int userId) {
		this.userId = userId;
	}
	@Override
	public String toString() {
		return "Address [city=" + city + ", country=" + country + ", userId=" + userId + ", id=" + id + "]";
	}
}
