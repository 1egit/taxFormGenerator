import database_MySQL
import task

def main():
    hostName = 'localhost'
    admin = 'root'
    password = '666894'
    dbName = 'hand'
    conn = database_MySQL.easyConnect(hostName, admin, password)
    database_MySQL.createDB(conn, dbName)
    database_MySQL.dropTable(conn, 'employees')
    database_MySQL.dropTable(conn, 'vendors')
    database_MySQL.dropTable(conn, 'expenses')
    database_MySQL.createEmployees(conn)
    database_MySQL.createVendors(conn)
    database_MySQL.createExpenses(conn)
    
    task.annualExpense(conn, 'outputs/annualExpense.csv')
    task.annualExpenseDetail(conn, 'outputs/annualExpenseDetail.csv')
    
    
    


if __name__ == '__main__':
    main()