import sys
import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb

def easyConnect(hostName, admin, password):
    try:
        db = MySQLdb.connect(hostName , admin , password)
        print('connecting datababase: ' + hostName + '.' + admin + ' ### OK')
        return db
    except:
        print('connecting datababase: ' + hostName + '.' + admin + ' ### FAIL')
        sys.exit()

def createDB(db, dbName):
    try:
        cursor = db.cursor()
        cursor.execute('drop database if exists ' + dbName)
        cursor.execute('create database ' + dbName)
        cursor.execute('show databases')
        msg = cursor.fetchall()
        if dbName in msg[0]:
            print('creating database: ' + dbName + ' ### OK')
            cursor.execute('use ' + dbName)
    except:
        print('creating database: ' + dbName + ' ### FAIL')
        sys.exit()

def dropTable(db, TableName):
    cursor = db.cursor()
    cursor.execute('drop table if exists ' + TableName)
#     cursor.execute('show tables')
#     data = cursor.fetchall()
#     print(data)

def createEmployees(db):
    try:
        cursor = db.cursor()
        sql = 'create table employees'
        sql += ' (id integer auto_increment primary key,firstName varchar(255),lastName varchar(255),dateOfBirth date,dateOfHire date,cell varchar(255),email varchar(255),title varchar(255),workstate varchar(255),addresses varchar(255))'
        cursor.execute(sql)
        print('creating table: employees ### OK')
    except:
        print('creating table: employees ### FAIL')
        sys.exit()
    
    try:
        with open('data/employees.csv') as a:
            a.readline()
            for line in a:
                line = line[:-1].split('|')
                firstname = line[1]
                lastname = line[2]
                dob = line[3]
                doh = line[4]
                phone = line[5]
                email = line[6]
                title = line[7]
                state = line[8]
                address = line[9]
                val = (firstname, lastname, dob, doh, phone, email, title, state, address)
                sql = "INSERT INTO employees (firstName, lastName, dateOfBirth, dateOfHire, cell, email, title, workstate, addresses)"
                sql += " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, val)
        print('importing data from employees.csv to table: employees ### OK')
        db.commit()
    except:
        print('importing data from employees.csv to table: employees ### FAIL')
        sys.exit()

def createVendors(db):
    try:
        cursor = db.cursor()
        sql = 'create table vendors '
        sql += ' (id integer auto_increment primary key, vendor varchar(255), form varchar(255), taxID varchar(255), corpType varchar(255), addresses varchar(255))'
        cursor.execute(sql)
        print('creating table: vendors ### OK')
    except:
        print('creating table: vendors ### FAIL')
        sys.exit()
        
    try:
        with open('data/vendors.csv') as a:
            a.readline()
            for line in a:
                line = line[:-1].split('|')
                vendor = line[0]
                form = line[1]
                taxID = line[2]
                corpType = line[3]
                address = line[4]        
                val = (vendor, form, taxID, corpType, address)
#                 print(val)
                sql = "INSERT INTO vendors (vendor, form, taxID, corpType, addresses)"
                sql += " VALUES (%s, %s, %s, %s, %s)"
                cursor.execute(sql, val)
        print('importing data from vendors.csv to table: vendors ### OK')
        db.commit()
    except:
        print('importing data from vendors.csv to table: vendors ### FAIL')
        sys.exit()

def createExpenses(db):
    try:
        cursor = db.cursor()
        sql = 'create table expenses'
        sql += ' (id integer auto_increment primary key, transDate date, type varchar(255), transNum varchar(255), payee varchar(255), category varchar(255), dueDate varchar(255), balance decimal(19,2), total decimal(19,2))'
        cursor.execute(sql)
        print('creating table: expenses ### OK')
    except:
        print('creating table: expenses ### FAIl')
        sys.exit()
        
    try:
        with open('data/expenses.csv') as a:
            a.readline()
            a.readline()
            for line in a:
                line = line[:-1].split('|')
                transDate = line[0]
                transType = line[1]
                transNum = line[2]
                payee = line[3]
                category = line[4]
                dueDate = line[5]
                balance = line[6]
                total = line[7]
                val = (transDate, transType, transNum, payee, category, dueDate, balance, total)
#                 print(val)
                sql = "INSERT INTO expenses (transDate, type, transNum, payee, category, dueDate, balance, total)"
                sql += " VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql, val)
        print('importing data from expenses.csv to table: expenses ### OK')
        db.commit()
    except:
        print('importing data from expenses.csv to table: expenses ### FAIL')
        sys.exit()