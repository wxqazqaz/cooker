import pymysql.cursors
db = pymysql.Connect(host = 'localhost', port = 3306, user='root', passwd = '321', db = 'python.1', charset = 'utf8' )
cursor = db.cursor()
class Studentsys():
    message = []

    def add_info(self):
        self.student={}
        name= input("请添加学生姓名：")
        qq = int(input("请添加学生10位QQ号码："))
        wechat = input("请添加学生微信号：")
        if len(str(qq)) == 10:
            # self.student['姓名'] = name
            # self.student['QQ'] = qq
            # self.student['微信'] = wechat
            # self.message.append(self.student)
            sql = "insert into student(name,QQ,wex) values('%s',%s,'%s')"
            data = (name,qq,wechat)
            cursor.execute(sql % data)
            db.commit()
            print('成功添加', cursor.rowcount, '条学生信息')
            
        else:
            print("QQ号输入错误！！！")
        
    def del_info(self):
        del_name = input('请输入要删除的学生名字：')
        Studentsys.find_info(self,del_name)
        if cursor.rowcount >= 1:
            sql = "DELETE FROM student WHERE  name = '%s'"
            cursor.execute(sql % del_name)
            db.commit()
            print('成功删除', cursor.rowcount, '条学生信息')



        # for i in self.message:
        #     if del_name == i['姓名']:  
        #         self.message.remove(i)
        #         t += 1
        # if t == 0:
        #     print('输入的学生姓名不存在！')
        # else:
        #     print("已删除！")
        
    # 修改数据
    def alter_info(self):
        old_name = input('请输入要修改的学生姓名：')
        Studentsys.find_info(self,old_name)
        if cursor.rowcount >= 1:
            new_name = input('\n请输入修改后的学生姓名：')
            new_qq = int(input('请输入修改后的10位的QQ号：'))
            new_wex = input('请输入修改后的微信号：')
            if len(str(new_qq)) == 10:
                sql = "UPDATE student SET name = '%s' where name = '%s'"
                data= (new_name,old_name)
                cursor.execute(sql % data)
                sql = "UPDATE student SET   QQ = '%s' where name= '%s'"
                data = (new_qq,new_name)
                cursor.execute(sql % data)
                sql = "UPDATE student SET wex = '%s' where name= '%s'"
                data = (new_wex,new_name)
                cursor.execute(sql % data)
                db.commit()
                print('修改成功！！！')
            else:
                print("QQ号输入错误！！！")
            
        # for i in self.message:
        #     if old_name == i['姓名']:
        #         i['姓名'] = input('学生姓名：')
        #         i['QQ'] = input('QQ号码：')
        #         i['微信'] = input('微信号：')
        #         t += 1
        #         break
        #     if t == 0:
        #         print('输入的学生姓名不存在！')
        #     else:
        #         print("已修改！")
        
    def find_info(self,find_name):
        sql = "SELECT * FROM student WHERE name = '%s' "
        cursor.execute(sql % find_name)
        for row in cursor.fetchall():
            print('''姓名：\tQQ：\t\t微信号：\t''')
            for i in row:
                print(f'{i}\t',end='')
            
        # for i in self.message:
        #     if find_name == i['姓名']:
        #         t+=1
        #         for key in i:
        #            print(f'{key}:{i[key]}\t',end='')
        #     break
        # if t == 0:
        #     print('输入的学生姓名不存在！') 

    def show_info(self):
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        print ("姓名：\tQQ号：\t\t微信号：")
        for row in results:
            n = row[0]
            q = row[1]
            w = row[2]
            print('%-5s %10s %13s' % (n,q,w))

    def menu(self):
        print('''\n学生管理系统：
                 1.添加学生信息
                 2.删除学生信息
                 3.修改学生信息
                 4.查找学生信息
                 5.显示学生信息
                 6.退出''')
        a = int(input('请选择：'))
        S=Studentsys()
        if a == 1:
            S.add_info()
            S.menu()
        elif a == 2:
            S.del_info()
            S.menu()
        elif a ==3:
            S.alter_info()
            S.menu()
        elif a == 4:
            find_name = input('请输入要查找的学生姓名：')
            S.find_info(find_name)
            S.menu()
        elif a == 5:
            S.show_info()
            S.menu()
        elif a == 6:
            db.close()
            exit
        else:
            S.menu()

S=Studentsys()
S.menu()





# cursor.execute("DROP TABLE IF EXISTS student")
# sql = """CREATE TABLE student (
#          name  CHAR(20) NOT NULL,
#          QQ INT,  
#          wex int )"""
 
# # cursor.execute(sql)



