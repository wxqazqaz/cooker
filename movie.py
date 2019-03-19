import pymysql
import getpass 
db = pymysql.Connect(host = 'localhost', port = 3306, user='root', passwd = '321', db = 'python.1', charset = 'utf8' )
cursor = db.cursor()
# # 创建电影票表：
# cursor.execute("DROP TABLE IF EXISTS cinema")
# sql = """CREATE TABLE cinema (
#          num int primary key auto_increment,
#          name  CHAR(20) NOT NULL,
#          director  char(8) NOT NULL,  
#          star char(8) NOT NULL,
#          duration int NOT NULL,
#          time time not null,
#          price int NOT NULL,
#           poll  int not null)"""
# cursor.execute(sql)

# # 插入数据：
# name = ['流浪地球','星际穿越','功夫之王','地球最后的夜晚']
# director = ['郭帆','诺兰',' 周星驰 ','毕赣']
# star = ['吴京','安妮·海瑟薇','周星驰','汤唯']
# duration = ['120','120','125','95']
# time = ['10:00','15:30','11:20','18:30']
# price = [80,85,75,75]
# poll= [5,3,2,4,1]
# for i in range(4):
#     sql = "insert into cinema(name,director,star,duration,time,price,poll) values('%s','%s','%s','%s','%s',%s,%s)"
#     data = (name[i],director[i],star[i],duration[i],time[i],price[i],poll[i])
#     cursor.execute(sql % data)
#     db.commit()
#     print('成功添加', cursor.rowcount, '条学生信息')

      #电影
class Movie():
            #电影票属性：名称 ， 导演   主演  时长 上映时间  价格
    def __init__ (self,name,director,star,duration,time,price,poll):
        self._name = name 
        self._director = director 
        self._star = star 
        self._duration = duration 
        self._time = time
        self._price = price
        self._poll = poll 
    #添加上映电影
    def add_movie(self):
        try:
            sql = "insert into cinema (name,director,star,duration,time,price,poll) values ('%s','%s','%s','%s','%s',%s,%s)"
            data = (self._name,self._director,self._star,self._duration,self._time,self._price,self._poll)
            cursor.execute(sql % data)
            db.commit()
            print('成功添加', cursor.rowcount, '场',self._name,'电影！！')
        except:
            print('信息添加错误！')
            db.rollback()
            
    #电影院
class Cinema(Movie):
    
    def __init__(self):
        self.m = [] #已选择的 不用刷新
        self.w = [] # 已购买电影票名称，时间 放映厅，座位号a,b 购买完后刷新
        self.bi = [] 
        self.t = 0

    def show(self):
        self.t = 0
        sql = "SELECT * FROM cinema"
        cursor.execute(sql)
        results = cursor.fetchall()
        tplt = "{0:{8}<6}\t{1:{8}<6}\t\t\t{2:{8}<6}\t\t{3:{8}<6}\t\t\t{4:{8}<6}\t{5:{8}<6}\t{6:{8}<6}\t{7:{8}<6}"
        print(tplt.format("编号：", "名称：", "导演：","主演：","时长：","播放时间：","价格：",'余票：', chr(12288)))
        tplt1 = "{0:{8}<6}\t{1:{8}<6}\t\t\t{2:{8}<6}\t\t{3:{8}<6}\t\t\t{4:{8}<6}\t\t{5:{8}<6}\t{6:{8}<6}\t{7:{8}<6}"
        for row in results:
            self.t += 1
            self.bi.append(row[0])
            l1= []
            l=[]
            l = [row[1],row[2],row[3],row[4],row[5],row[6],row[7]]
            for i in l:
                a = f'{i}'
                if i == row[7]:
                    a += ' 张'
                elif i == row[6]:
                    a += ' ￥'
                elif i == row[4]:
                    a += ' min'
                l1.append(a)
            print(tplt1.format(self.t,l1[0],l1[1],l1[2],l1[3],l1[4],l1[5],l1[6],chr(12288)))
            print()


    # 选择电影
    @classmethod
    def Ticket(cls,number):
        if number >=1 and number <= c.t:
            try:
                sql = 'select * from cinema where num = %s '
                cursor.execute(sql % c.bi[number-1])# 显示选中的电影
                for row in cursor.fetchall():
                    print(f'编号：{number}\t\t名称:{row[1]}\t\t导演：{row[2]}\t主演：{row[3]}\t时长：{row[4]} min\t播放时间：{row[5]}\t价格：{row[6]}￥\t票数：{row[7]} 张')
                    db.commit()
                    number1 = row[0]
                    n = (row[1]) 
                    t = (row[5])
            except:
                print('查询错误！！')
                db.rollback()
            u = int(input(''' 
                请选择播放的影厅类型：
                1.vip大保健
                2.3D放映厅
                3.MAX播放厅
                4.返回\n
            '''))# 选择播放厅类型
            if u == 4:
                c.menu2()
            else:
                l = ['vip大保健','3D放映厅','MAX播放厅']
                c.w += [n,t,l[u-1]]
                c.w1 = c.w
                try:
                    sql1 = 'UPDATE cinema SET poll = poll - 1 WHERE num = %s'
                    cursor.execute(sql1 % number1)
                    db.commit()
                except:
                    print('修改错误！！')
                    db.rollback()
                try:
                    sql2 = 'delete from cinema where poll = 0'
                    cursor.execute(sql2)
                    db.commit()
                except:
                    print('删除错误！！')
                    db.rollback()
                print('选票成功！！')
        else:
            number = int(input('输入错误，请重新输入：'))
            c.Ticket(number)
        c.bi = []

    #选择座位号
    def Seat(self):
        self.printer()
        a = int(input('请输入要选择座位的排数：'))
        b = int(input('请输入要选择座位的列数：'))
        if a not in list(range(1,9)) or b not in list(range(1,11)):
                print('输入错误！请重新输入！！')
                self.Seat()
        else:
            self.w += [a,b]
            for k in self.m:
                if self.w == k:
                    print('已有人选购！！请重新选择！！')
                    self.w.pop()
                    self.w.pop()
                    self.Seat()
                    break
        self.w.pop()
        self.w.pop()
        c = input('确定使用当前的座位号吗？ Y确定, 其它任一键从新选择:')
        if c == 'Y': # 确定选择 打印电影票
            print()
            print(f'''
            --------电影票-------
            电影名称:{self.w[0]} 
            {a} 排， {b}号
            ----放映厅：{self.w[2]}
            播放时间:{self.w[1]}
            ------------------------
                    ''')
            self.w += [a,b]
            self.m.append(self.w)
        else:
            self.Seat()
        self.w = []
        self.menu2()

    # 打印座位表
    def printer(self):
        t = 0
        print('''00 01 02 03 04 05 06 07 08''')
        for i in range(1,11):
            if i < 10:
                print(f' {i}',end = '')
            elif i == 10:
                print(f'{i}',end = '')
            for j in range(8-t):  
                t = 0
                for s  in  self.m:
                    if self.w[0] == s[0] and self.w[2] == s[2] and s[4] == j+1 and s[3] == i:
                        print('  @',end = '') 
                        t += 1
                if t == 1:
                    continue
                else:
                    print('  +',end = '')
            print()

    #管理员菜单
    def menu1(self):
        a = input('''
            1.添加电影
            2.后退
            3.退出\n\n
            请选择：
            ''')
        if a == '1':
            name = input("请输入电影名称：")
            director = input('请输入导演：')
            star = input('请输入主演：')
            duration = input('请输入电影时长：')
            time = input('请输入上映时间：')
            price = input('请输入价格：')
            while True:
                poll =int(input('请输入票数(10票以内)：'))
                if   poll >= 1  and poll <= 10:
                    m = Movie(name,director,star,duration,time,price,poll)
                    m.add_movie()
                    c.menu1()
                    break
                else:
                    print('票数输入错误！！请重新输入')
                    continue
        elif a == '2':
            c.menu()
        elif a == '3':
            db.close()
            exit('退出系统！！！')
        else:
            c.menu1()
    #购票菜单
    def menu2(self):
        b = input('''
        ---------------欢迎来到太平洋电影城---------------
                            1.购票
                            2.后退
                            3.退出\n\n
                            请选择：''')
        if b == '1': 
            c.show()
            number = int(input('请选择需要观看的电影编号：\n'))
            c.Ticket(number)
            c.Seat()
        elif b == '2':
            c.menu()
        elif b == '3':
            db.close()
            exit('退出系统！！！')
        else:
            c.menu2()

    #系统主菜单
    def menu(self):
        p = input('''
        ------------电影院购票系统---------------------
                    1.管理员
                    2.影迷
                    3.退出\n\n
                    请选择：''')
        if p == '1':
            t = 3
            while t <= 3:
                ma = int(getpass.getpass('请输入密码：'))
                if ma == 321:
                    c.menu1()
                    break
                elif t == 1:
                    exit('账户已锁死！！')
                else:
                    t -= 1
                    print(f'输入错误！！ 还剩{t}次机会！')
        elif p == '2':
            c.menu2()
        elif p == '3':
            db.close()
            exit('退出系统！！')
        else:
            c.menu()
           
c = Cinema()
c.menu()


