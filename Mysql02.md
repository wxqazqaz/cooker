#MySql02
##复习
###数据库相关
1. 查看所有数据库
	
	show databases;
2. 创建数据库
	
	create database db2 character set utf8;

3. 查看单个数据库

	show create database db2;

4. 删除数据库

	drop database db2;

5. 使用数据库

	use db2;


##表相关sql
1. 查询所有表 
	
	show tables;

2. 创建表
	create database db2;
	use db2;
	create table item(id int,title varchar(20),
						price int,num int,
						createdate date);
3. 查看表两种方式

	show create table item;
	desc item;

4. 修改表名
	rename table item to t_item;

5. 修改引擎和字符集

	alter table t_item engine=innodb charset=utf8;
6. 添加字段 修改字段(2种) 删除字段

	alter table t_item add category varchar(20);
	alter table t_item modify category varchar(10);
	alter table t_item change category cat varchar(20);
	alter table t_item drop cat;
7. 删除表
	
	drop table t_item;

##数据相关

1. 插入数据
	insert into t_item values(1,'苹果电脑',9888,2,'2018-03-22','电脑');
	insert into t_item (id,title,price) values(2,'华为手机',3888);
2. 查询数据
	select * from t_item;
	select title from t_item;
3. 修改数据
	update t_item set num=100 where id=2;
4. 删除数据
	delete from t_item where id=2;
练习:
1. 创建t_emp(员工表) 字段有:id name salary dept(部门名字),joindate(入职日期)
	create table t_emp(id int,name varchar(10),salary int,dept varchar(10),joindate date);
2. 插入 刘关张和取经四人组7个人 刘关张部门为 三国部 取经的四个人为 取经部 其它数据随意
	insert into t_emp values
	(1,'悟空',3000,'取经部','2008-11-20'),
	(2,'八戒',4000,'取经部','2008-11-21'),
	(3,'沙僧',5000,'取经部','2008-11-22'),
	(4,'唐僧',6000,'取经部','2008-11-23'),
	(5,'刘备',9000,'三国部','2008-11-24'),
	(6,'关羽',7000,'三国部','2008-11-25'),
	(7,'张飞',1000,'三国部','2008-11-26');
3. 修改刘备工资为2000
	update t_emp set salary=2000 where id=5;
4. 修改唐僧名字为 玉帝哥哥
	update t_emp set name='玉帝哥哥' where id=4;
5. 在表的name字段后面添加一个age字段
	alter table t_emp add age int after name;
6. 修改三国部的所有人年龄为55
	update t_emp set age=55 where dept='三国部';
7. 修改工资小于5000的年龄为18
	update t_emp set age=18 where salary<5000;
###乱码问题
1. 数据库字符集 要设置utf8
2. 表的字符集 设置为utf8
windows系统的命令行里 有些版本是gbk的编码格式
可以通过set names gbk;的方式把mysql接收到数据时的解码格式设置为gbk,这个位置的gbk 和数据库还有表的utf8没有关系
在windows系统中修改mysql默认的数据库编码:
1. 找到安装文件中的my.ini的配置文件 在里面添加如下代码:
character-set-server=utf8
2. 添加完之后 尽量重启下电脑
###eclipse里面写sql
1.先下载mysql驱动包
		mysql-connector-java-5.1.6.jar
2.window->show view ->other->Data Management->Data Source Exploer 和 SQL Results  Open
3.在Data Source Exploer选项卡里面的 DataBaseConnections上右键 new
4.选择MYSQL
5.点击下拉箭头右侧的加号 
6.选择 5.1  点击JarList  clear All
7.点击 add jar在弹出窗口中 找到下载的 jar文件 然后OK
8.修改URL /后面的内容  改成自己电脑上数据库的名字
9.输入密码 没有密码则空着
10.点击test Connection  如果显示 Ping Successed则点击finish
11.在大桶上面右键 Open SQL...
12.type 中选择 mysql5.1 Name中选择 New Mysql
Database中选择 database  在最右侧如果显示Connected则可以开始写sql语句

###自定义代码块
可以把常用但又复杂的代码 自定义成模板代码
步骤:
1. window->preference->然后搜索temp 找到datasource里面的templates 
2.点击右侧new   
###主键及自增
主键特点:非空并唯一
    create table t1(id int primary key,age int);
    desc t1;
    select * from t1;
    insert into t1 values(null,22);
    insert into t1 values(1,22);
    insert into t1 values(1,11);
自增约束: auto_increment
		create table t2
		(id int primary key auto_increment,age int);
自增约束通常和主键约束同时使用,此时主键可以赋值为null,
-自增规则:从最大值基础上+1
-每张表只能有一个字段为自增字段
###非空
	-not null
    create table t3(id int primary key auto_increment, age int not null);
    desc t3;
    insert into t3 values (null,3);
    select * from t3;
	-以下代码会出错:
    insert into t3 values (null,null);
###注释
-给表添加字段的时候可以给表的字段添加注释

    create table t5(id int comment '用户的id',age int comment '用户的年龄');
    show create table t5;

###数据的冗余 rongyu
	当表内的数据出现大量重复时称为数据的冗余,可以通过拆分表的形式避免或降低冗余的可能性
###练习：
	1. 创建部门dept(id 主键并自增,name 非空)和员工emp表(id,name,deptid)
	2. 创建分类category(id 主键并自增,name 非空)和商品item表(id,title,price,categoryid)
	3. 分别往四张表中添加几条数据 
-部门和员工
    auto_increment,name varchar(10) not null);
    insert into dept values(null,'财务部'),
    (null,'研发部'),(null,'市场部');
    create table emp(id int primary key 
    auto_increment,name varchar(10),deptid int);
    insert into emp values(null,'小猫',1),
    (null,'小狗',2),(null,'大牛',3);
    select * from emp;
-分类和商品
	create table category(id int primary key 
    auto_increment,name varchar(10) not null);
    insert into category values(null,'电脑'),
    (null,'手机'),(null,'文具');
    create table item(id int primary key 
    auto_increment,title varchar(10),
    categoryid int,price int);
    insert into item values(null,'戴尔电脑',1,3433),
    (null,'苹果手机',2,9888),(null,'铅笔',3,2);
    select * from item;

##事务
-数据库中sql语句执行的最小单元,
不能分割执行事务内的sql语句
-mysql的自动提交属性默认是开启的,如果需要使用事务功能
需要关闭自动提交

-显示当前自动提交的状态
	show variables like '%autocommit%';
-关闭自动提交 显示 off 说明没有问题
	set autocommit=0;
创建user表字段 id 主键自增 name money
插入数据 超人200块钱    蝙蝠侠205
		create table user(id int primary key auto_increment,name varchar(20),money int);
		insert into user values(null,'超人',200),(null,'蝙蝠侠',205);
1.先把自动提交 关闭
		set autocommit=0;
2.让超人+100;
	update user set money=300 where id=1;
3.此时可以开启另外一个窗口 验证超人的钱有没有+100,因为开启了事务,此次操作还没有commit所以只在内存中+100所以新窗口的数据并没有改变
4.让蝙蝠侠-100;
	update user set money=105 where id=2;
然后立即执行提交命令
	commit;
执行commit之后内存中的多次操作会同时更新到数据库中
5.此时去另外一个窗口验证,因为已经提交到了数据库所以新窗口中的数据也发生了改变

rollback:回滚到初始状态
测试:先把蝙蝠侠的5块变成6块 然后 查看 然后rollback再查看
savepoint s1(标识) :设置保存点
测试:先把蝙蝠侠5变成6 然后设置保存点s1 然后从6变7
如果直接rollback 则回到5 如果rollback to s1则回到6块
rollback to s1;

回顾: 查看自动提交状态 show variables like '%autocommit%' 修改状态 set autocommit=0/1 
begin 起始点   savepoint设置回滚点 commit提交
rollback 和 rollback to XXX;

## SQL分类
### 数据定义语言 DDL
-Data Definition Language:数据定义语言
常见命令 create alter drop truncate
不支持事务 
### 数据操纵语言 DML
-Data Manipulation Language:数据操作语言
常见命令:insert update delete (select)
支持事务
### 数据查询语言 DQL
-Data Query Language:数据查询语言
常见命令:select   
-也属于DML

### TCL 
-Transaction Control Language:事务控制语言
常见命令:begin commit rollback savepoint
###DCL
-Data Control Language:数据控制语言
给用户分配权限相关的sql语言
DDL DML DQL TCL DCL
### 数据库数据类型
### 整数
int(m): 4字节   m代表现实长度,当现实的数据长度小于m值时会补0 **一定要结合zerofill使用**
			m=10    0000012321
测试:
		create table t_int (num int(10) zerofill);
		insert into t_int values (18);
		select * from t_int;
bigint:8字节
###浮点数
double(m,d):m代表数据的总长度,d代表小数点后面的位数
56.234   5,3
decimal(m,d):m代表数据的总长度,d代表小数点后面的位数
涉及高精度运算时使用decimal 通常涉及钱的地方使用decimal
###字符串
char(20):固定长度 存abc 占20长度 执行效率高 最大255
varchar(20):可变长度 存abc 占3长度 节省空间 最大65535,但是超过255建议使用text
text:可变长度 最大65535

### 日期
-date:只能存年月日
-time:只能存时分秒
-datetime:年月日时分秒 默认值null 最大值9999-12-31
-timestamp:年月日时分秒 默认值是当前时间 最大时间2038-01-19
  案例：创建表t，字段d1 date，d2 time,d3 datetime,d4 timestamp
		create table t(d1 date,d2 time,d3 datetime,d4 timestamp);
	insert into t values('2008-8-8',null,null,null);
	insert into t values(null,'12:06:35','2008-08-12 14:30:22',null);

回顾:
1. 主键 自增
	primary key auto_increment
2. 非空  
	not null
3. 字段的注释
	comment '注释内容'
4. 冗余
5. 事务:数据库执行sql的最小单元
	begin commit rollback savepoint
	show variables like '%autocommit%'
	set autocommit=0/1;
6. sql分类

-ddl 数据定义语言 不支持事务 create alter drop truncate
-dml 数据操作语言 支持事务 insert update delete 
	select(dql)
-dql 数据查询语言 select
-tcl 事务控制语言 begin commit rollback savepoint
-dcl 数据控制语言 分配用户权限相关

7. 数据类型
整数:int(10) zerofill  bigint
浮点数: double decimal(m,d) 
字符串:char(20)固定长度 255 varchar(20) 可变 最大65535  text 可变 65535
日期: date time datetime timestamp

回顾:
1.数据库相关
show databases
show create database db1;
create database db2 character set utf8;
drop database db1;
2.表相关
show tables;
show create table t1;
desc t1;
create table t1(id int,name varchar(10));
rename table t1 to t2;
alter table t1 add age int;
alter table t1 engine=innodb charset=gbk;
alter table t1 change age newAge int;
alter table t1 modify newAge int after id;
alter table t1 drop newAge;
drop table t1;

数据相关:
