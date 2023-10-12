import mysql.connector as m
h="localhost"
u="root"
p=""
d="test"
def menu():
    print("1.Insert Record")
    print("2.Show all Record")
    print("3.Updata Record")
    print("4.Delete Record")
    print("2.Search Record")
def searchData():
    con=m.connect(host=h,user=u,password=p,database=d)
    if con.is_connected():
        cur=con.cursor()
        r=input("Enter Roll to Search:")
        qur="Select * form t1 where Roll=%s"
        val=(r,)
        cur.execute(qur,val)
        data=cur.fetchall()
        for row in data:
            print(row)
    else:
        print("Error")
def deleteData():
    con=m.connect(host=h,user=u,password=p,database=d)
    if con.is_connected():
        cur=con.cursor()
        r=input("Enter Roll to Search:")
        qur="Delete form t1 where Roll=%s"
        val=(r,)
        cur.execute(qur,val)
        print('Data Deleted!!!')
        con.commit()
        showData()
    else:
        print("Error")
def updaraData():
    con=m.connect(host=h,user=u,password=p,database=d)
    if con.is_connected():
        cur=con.cursor()
        print("Only Address Updata is allowed")
        roll=input("Enter Roll to search record:")
        address=input("Enter New Address:")
        
        qur=(address,roll)

        cur.execute(qur,val)

        print('Data Updated!!!')
        con.commit()
        showData()
    else:
        print("Error")
def insertData():
    con=m.connect(host=h,user=u,password=p,database=d)
    if con.is_connected():
        cur=con.cursor()
        roll=input("Enter Roll:")
        name=input("Enter Name:")
        address=input("Enter Address:")
        marks=int(input("Enter Mars:"))

        qur="insert into t1 values(%s,%s,%s)"
        val=(roll,name,address,marks)

        cur.execute(qur,val)

        print('Data inserted!!!')
        con.commit()
        showData()
    else:
        print("Error")
def showData():
    con=m.connect(host=h,user=u,password=p,database=d)
    if con.is_connected():
        cur=con.cursor()
        cur.execyte("select * form t1")
        data=cur.fetchall()
        print("Total Records are ",cur.rowcount)
        for row in data:
            print(row)

    else:
        print("Error")



#main
menu()
choice=int(input("Enter Choice"))
if choice==1:
    insertData()
elif choice==2:
    showData()
elif choice==3:
    updateData()
elif choice==4:
    deleteData()
elif choice==5:
    searchData()
