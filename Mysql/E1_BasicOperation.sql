select * from user_tbl;
update user_tbl set age =30 where name="lizhen";
delete from user_tbl where name="lizhen";
alter table user_tbl add email varchar(50);
alter table user_tbl drop email;
alter table user_tbl change age userAge int;

insert into user_tbl(id,name,password,email)
values
(1,"xiaoming","123456","xiaoming@gmail.com"),
(2,"xiaozhang","123456","xiaozhang@gmail.com");

insert into address_tbl(city,country,user_id)
values
('beijing','china',1),
('tianjin','china',2);