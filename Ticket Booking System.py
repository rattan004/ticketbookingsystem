import pandas as pd
def db():
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost",user="root",password="password")
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS AIR_INDIA")
    mycursor.execute("USE AIR_INDIA")
    print("DATABASE CREATED")
db()
def table_1():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="password",database="AIR_INDIA")
    mycursor=mycon.cursor()
    t1="CREATE TABLE IF NOT EXISTS USER_DATA(FIRST_NAME VARCHAR(50),LAST_NAME VARCHAR(50), USERNAME VARCHAR(50),PASSWORD VARCHAR(50),PHONE_NO VARCHAR(20),DOB DATE,AGE INT(3))"
    mycursor.execute(t1)
    print("TABLE USER DATA CREATED")
table_1()
def table_2():
    import mysql.connector
    mycon=mysql.connector.connect(host="localhost",user="root",password="password",database="AIR_INDIA")
    mycursor=mycon.cursor()
    t2="CREATE TABLE IF NOT EXISTS TICKETS(NAME VARCHAR(100),PHONE_NO VARCHAR(20),AGE INT(3),GENDER VARCHAR(20),START VARCHAR(50),END VARCHAR(50),DATE DATE)"
    mycursor.execute(t2)
    print("TABLE TICKETS CREATED")
table_2()

from tabulate import tabulate
def menu():
    ch=""
    while ch=="":
        
        maintab=[['WELECOME TO AIR_INDIA RESERVATION SYSTEM'],['1.SIGN IN TO EXISTING ACCOUNT'],['2.CREATE A NEW ACCOUNT'],['3.DELETE AN EXISTING ACCOUNT'],['4.EXIT RESERVATION SYSTEM']]
        print(tabulate(maintab,headers="firstrow",tablefmt="grid"))
        ch1=int(input('ENTER NUMBER:'))
        if ch1==1:
            print("TAKING YOU TO THE SIGN-IN PAGE")
            a=ch1check()
            if a==True:
                main()
            else:
                continue
        elif ch1==2:
            print("TAKING YOU TO THE SIGN-UP PAGE")
            a=ch2check()
            if a==True:
                main()
            else:
                continue
        elif ch1==3:
            print("TAKING YOU TO THE ACCOUNT-DELETION PAGE")
            c=ch3check()
            if c==True:
                print('ACCOUNT DELETED')
                continue
            else:
                print('YOUR PASSWAORD OR USER_NAME IS INCORRECT')
                continue
        elif ch1==4:
            print('THANK YOU')
            break
        else:
            print('ERROR 404:PAGE NOT FOUND')
            break

# CH1==1
def ch1check():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    user=input('ENTER USERNAME:')
    passw=input('ENTER PASSWORD:')
    try:
        s1="SELECT USERNAME FROM USER_DATA WHERE PASSWORD='{}'".format(passw)
        c1="SELECT FIRST_NAME,LAST_NAME FROM USER_DATA WHERE PASSWORD='{}'".format(passw)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        
        data1=list(data1)
        name=data1[0]+" "+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)[0]
        if data==user:
            print('WELCOME BACK',name.upper())
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')

#CH1==2
def ch2check():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    Fname=input("ENTER YOUR FIRST NAME:")
    Lname=input("ENTER YOUR LAST NAME:")
    user=input('ENTER YOUR USERNAME:')
    passw=input('ENTER YOUR PASSWORD:')
    repass=input('RE-ENTER YOUR PASSWORD:')
    ph=input("ENTER YOUR PHONE NUMBER:")
    print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
    gen=input('ENTER YOUR GENDER:')
    datep=str(input('ENTER DATE(DD/MM/YYYY):'))
    day=datep[0:2]
    month=datep[3:5]
    year=datep[6:]
    dob=year+"/"+month+"/"+day
    age=input('ENTER YOUR AGE:')
    gen1={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION','m':'MALE','f':'FEMALE','n':'NOT TO MENTION'}
    if passw==repass:
        try:
            st="INSERT INTO USER_DATA VALUES('{}','{}','{}','{}','{}','{}','{}','{}')".format(Fname,Lname,user,passw,ph,gen1[gen],dob,age)
            cursor.execute(st)
            print('WELCOME',Fname,Lname)
            return True
        except:
            print('AN ERROR OCCURED')
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
#CH1==3
def ch3check():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    try:
        s1="SELECT PASSWORD FROM USER_DATA WHERE USERNAME='{}'".format(a)
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==b:
             s1="SELECT PASSWORD FROM USER_DATA WHERE USERNAME='{}'".format(a)
             c1="SELECT FIRST_NAME,LAST_NAME FROM USER_DATA WHERE USERNAME='{}'".format(a)
             cursor.execute(c1)
             data1=cursor.fetchall()[0]
             data1=list(data1)
             data1=data1[0]+' '+data1[1]
             cursor.execute(s1)
             data=cursor.fetchall()[0]
             data=list(data)
             if data[0]==b:
                 x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
                 s1="SELECT FIRST_NAME,LAST_NAME,PHONE_NO,GENDER,DOB,AGE FROM USER_DATA WHERE USERNAME='{}'".format(a)
                 cursor.execute(s1)
                 data=cursor.fetchall()[0]
                 data=list(data)
                 trial=[['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE'],data]
                 print(tabulate(trial, headers='firstrow', tablefmt='grid'))
                 print('IS THIS YOUR ACCOUNT')
                 vi=int(input('1-YES 2-NO\nENTER NUMBER: '))
                 if vi==1:
                     b1="DELETE FROM USER_DATA WHERE USERNAME='{}'".format(a)
                     cursor.execute(b1)
                     s1="delete from TICKETS where PHONE_NO='{}'".format(data[2])
                     cursor.execute(s1)
                     return True
                 elif vi==2:
                     print('SORRY,RETRY')
                 else:
                     print('ERROR 404:PAGE NOT FOUND')
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
#MAIN
def main():
    ke=""
    while ke=="":
        mta=[['1.TICKET BOOKING'],['2.TICKET CHECKING'],['3.TICKET CANCELLING'],['4.ACCOUNT DETAILS'],['5.LOG OUT']]
        print(tabulate(mta,tablefmt="grid"))
        ch=int(input('ENTER NUMBER:'))
        if ch==1:
            ticket_booking()
        elif ch==2:
            ticket_checking()
        elif ch==3:
            ticket_cancelling()
        elif ch==4:
            acc_details()
        elif ch==5:
            print('THANK YOU')
            break
        else:
            print('WRONG INPUT')
#TICKET_BOOKING
def ticket_booking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    phno=str(input("ENTER YOUR PHONE NUMBER: "))
    s1="SELECT FIRST_NAME,LAST_NAME,PHONE_NO,GENDER,DOB,AGE FROM USER_DATA WHERE PHONE_NO='{}'".format(phno)
    cursor.execute(s1)
    data=cursor.fetchall()[0]
    data=list(data)
    trial=[['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE'],data]
    print(tabulate(trial, headers='firstrow', tablefmt='grid'))
    print("ARE THE ABOVE GIVEN DETAILS CORRECT?\n1.YES\n2.NO")
    yorn=int(input("ENTER NUMBER: "))
    if yorn==1:
        fr=input('ENTER YOUR STARTING LOCATION:')
        to=input('ENTER YOUR DESTINATION LOCATION:')
        datep=str(input('ENTER DATE(DD/MM/YYYY):'))
        day=datep[0:2]
        month=datep[3:5]
        year=datep[6:]
        date=year+"/"+month+"/"+day
        nm=data[0]+" "+data[1]
        s1="insert into TICKETS values('{}',{},{},'{}','{}','{}','{}')".format(nm,data[2],data[5],data[3],fr,to,date)
        cursor.execute(s1)
        print('BOOKED SUCCESSFULLY')
    elif yorn==2:
        print("TAKING YOU TO MANUAL DETAIL FILLING PAGE")
        nm=input('ENTER YOUR NAME:')
        phno=input('ENTER YOUR PHONE NUMBER:')
        age=int(input('ENTER YOUR AGE:'))
        print(' M=MALE','\n','F=FEMALE','\n','N=NOT TO MENTION')
        gender=input('ENTER YOUR GENDER:')
        Gender=gender.upper()
        fr=input('ENTER YOUR STARTING LOCATION:')
        to=input('ENTER YOUR DESTINATION LOCATION:')
        datep=str(input('ENTER DATE(DD/MM/YYYY):'))
        day=datep[0:2]
        month=datep[3:5]
        year=datep[6:]
        date=year+"/"+month+"/"+day
        a={'M':'MALE','F':'FEMALE','N':'NOT TO MENTION'}
        v=a[Gender]
        s1="insert into TICKETS values('{}',{},{},'{}','{}','{}','{}')".format(nm,phno,age,v,fr,to,date)
        cursor.execute(s1)
        print('BOOKED SUCCESSFULLY')
    else:
        print("ERROR 404: PAGE NOT FOUND")
#TICKET_CHECKING
def ticket_checking():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    
    phno=int(input('ENTER YOUR PHONE NUMBER:'))
    ss="SELECT COUNT(*) FROM TICKETS WHERE PHONE_NO={}".format(phno)
    cursor.execute(ss)
    data=cursor.fetchall()
    data=str(data)
    n=data[2:3]
    n=int(n)
    i=0
    if n==0:
        print("NO TICKET EXISTS")
    while n>i:
        try:
            w=i+1
            s1="SELECT * FROM TICKETS WHERE PHONE_NO='{}'".format(phno)
            cursor.execute(s1)
            data=cursor.fetchall()[i]
            Data=list(data)
            print("TICKET",w)
            a=[['NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE'],Data]
            print(tabulate(a, headers="firstrow", tablefmt="grid"))
            print("")
        except:
            print('TICKET DOES NOT EXISTS')
    i=i+1
#TICKET_CANCELLING
def ticket_cancelling():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    phno=input('ENTER YOUR PHONE NUMBER:')
    ss="SELECT COUNT(*) FROM TICKETS WHERE PHONE_NO={}".format(phno)
    cursor.execute(ss)
    data=cursor.fetchall()
    data=str(data)
    n=data[2:3]
    n=int(n)
    i=0
    if n==0:
        print("NO TICKETS FOUND")
    while n>i:
        try:
            w=i+1
            s1="SELECT * FROM TICKETS WHERE PHONE_NO='{}'".format(phno)
            cursor.execute(s1)
            data=cursor.fetchall()[i]
            Data=list(data)
            print("TICKET",w)
            a=[['NAME','PHONE NUMBER','AGE','GENDER','STARTING POINT','DESTINATION','DATE'],Data]
            print(tabulate(a, headers="firstrow", tablefmt="grid"))
            print("DO YOU WANT TO DELETE THIS TICKET?(1.YES 2.NO) :")
            yorn=int(input("ENTER NUMBER: "))
            if yorn==1:
                s1="DELETE FROM TICKETS WHERE START='{}'AND END='{}'".format(data[4],data[5])
                cursor.execute(s1)
                print('TICKET CANCELLED')
                i=i+1
            elif yorn==2:
                print("TICKET NOT CANCELLED")
                i=i+1
            else:
                print("ERROR 404: PAGE NOT FOUND")
        except:
            print("THERE WAS AN ERROR, PLEASE RETRY")
    
#ACC_DETAILS
def acc_details():
    import mysql.connector
    mycon=mysql.connector.connect(host='localhost',user='root',passwd='password',database='AIR_INDIA')
    cursor=mycon.cursor()
    mycon.autocommit=True
    a=input('USER NAME:')
    b=input('PASS WORD:')
    
    try:
        s1="SELECT PASSWORD from USER_DATA WHERE USERNAME='{}'".format(a)
        c1="SELECT FIRST_NAME,LAST_NAME FROM USER_DATA WHERE USERNAME='{}'".format(a)
        cursor.execute(c1)
        data1=cursor.fetchall()[0]
        data1=list(data1)
        data1=data1[0]+' '+data1[1]
        cursor.execute(s1)
        data=cursor.fetchall()[0]
        data=list(data)
        if data[0]==b:
            x=['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE']
            s1="SELECT FIRST_NAME,LAST_NAME,PHONE_NO,GENDER,DOB,AGE FROM USER_DATA WHERE USERNAME='{}'".format(a)
            cursor.execute(s1)
            data=cursor.fetchall()[0]
            data=list(data)
            a=[['FIRST NAME','LAST NAME','PHONE NUMBER','GENDER','DATE OF BIRTH','AGE'],data]
            print(tabulate(a,headers="firstrow",tablefmt="grid"))
            
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
    
menu()
