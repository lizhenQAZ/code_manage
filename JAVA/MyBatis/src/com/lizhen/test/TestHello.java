package com.lizhen.test;
import java.io.IOException;
import java.io.Reader;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;
import com.lizhen.pojo.JikeUser;
public class TestHello {

	public static void main(String[] args) {
		String resource="com/lizhen/map/jikeUser.xml";
		Reader reader=null;
		SqlSession session;
		
		try {
			reader=Resources.getResourceAsReader(resource);
			System.out.println(reader.toString());
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		SqlSessionFactory sqlMapper=new SqlSessionFactoryBuilder().build(reader);
		session=sqlMapper.openSession();
		JikeUser temp=session.selectOne("findById", 1);
		System.out.println(temp.getUsername());
		session.close();
	}

}
