import pymysql
from faker import Faker


def insertData(host0,port0,user0,password0,db0,charset0):
    conn = pymysql.connect(host=host0, port=port0, user=user0, password=password0, db=db0,charset=charset0)

    cursor = conn.cursor()

    cursor.execute("truncate table student")

    fake = Faker("zh-CN")

    for i in range(40):
        cursor.execute(f'''insert into student(name,gender,birthday) values('{fake.name()}','{fake.random_int()%2}','{fake.date_between(start_date="-39y", end_date="-20y")}')''')
        # cursor.execute(f'''insert into customer(cname,gender,birthday,cellphone,email,profession) values('{fake.name()}','{"男" if fake.random_int()%2 == 1 else "女"}','{fake.date_between(start_date="-39y", end_date="-20y")}','{fake.phone_number()}','{fake.email()}','{fake.job()}')''')
        # cursor.execute(f'''insert into purchase_record(purchase_order_id,date_time) values('{i+1}','{fake.date_time_between(start_date="-2y", end_date="now", tzinfo=None)}')''')
        # cursor.execute(f'''insert into client(name,phone_num) values('{fake.company()}','{fake.phone_number()}')''')
        # cursor.execute(f'''insert into client_address(address) values('{fake.address()}')''')
        # cursor.execute(f'''insert into store(address) values('{fake.address()}')''')

    conn.commit()
    cursor.close() 
    conn.close()



insertData("localhost",3306,"root","123","stage2","utf8")
# fake = Faker("zh-CN")
# print(fake.email())
# for i in range(20):
#     print( "男" if fake.random_int()%2 == 1 else "女")


# random_int()# 随机数字，默认0~9999，可以通过设置min,max来设置
# random_number()# 随机数字，参数digits设置生成的数字位数
# fake.date_time_between(start_date="-1y", end_date="now", tzinfo=None)
# fake.company()
# fake.address()
# fake.job()
# phone_number()
# fake.simple_profile() #随机个人信息

