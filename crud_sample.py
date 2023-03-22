import pymysql;
from prettytable import PrettyTable;

def showdata():
    conn = pymysql.connect(host='localhost' , user='root' , password= '', db = 'tcet');
    cur = conn.cursor();
    cur.execute("Select * FROM students");
    output = cur.fetchall()
    table = PrettyTable(['ID' ,'Name','Age','City']);
    for user in output:
        table.add_row([user[0], user[1], user[2], user[3]]);
    print(table);

def insertdata():
    conn = pymysql.connect(host='localhost' , user='root' , password='',db='tcet');
    Name = input("Enter the Name: ");
    Age = input("Enter Your age: ");
    City = input("Enter your city : ");
    sql = "INSERT INTO students (ID , Name , Age , City) VALUES (NULL, '"+Name+"','"+Age+"','"+City+"')";
    cur = conn.cursor()
    cur.execute(sql);
    conn.commit();
    showdata();
    

def updatedata():
    conn = pymysql.connect(host='localhost' , user='root' , password='' , db='tcet');
    ID = input("Enter the ID : ");
    Name = input("Enter The Name :");
    Age = input("Enter the Age");
    City = input("Enter the city: ")
    sql = "UPDATE students SET Name ='"+Name+"' ,Age = '"+Age+"' ,City= '"+City+"' WHERE ID = '"+ID+"'";
    cur = conn.cursor()
    cur.execute(sql);
    conn.commit();
    showdata();


def deletedata():
    conn = pymysql.connect(host='localhost', user='root', password ='' , db='tcet');
    ID = input("Enter the Id to delete : ");
    sql = "DELETE FROM students WHERE ID = '"+ID+"'";
    cur = conn.cursor()
    cur.execute(sql);
    conn.commit();
    showdata();

option=None
while option !=0:
    print("\n***** SELECT DATA *****\n")
    print("1. Show Data")
    print("2. Insert Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("0. Exit")

    option=int(input("Select your option : "))
    if option <5:
        if option==1:
            showdata()
        elif option==2:
            insertdata()
        elif option==3:
            updatedata()
        elif option==4:
            deletedata()
        elif option==0:
            print("Thankyou ! have a nice day")
    else:
        print("Invalid Selection")
