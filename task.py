import csv

def annualExpense(db, outputFile):
    
    cursor = db.cursor()
    sql = 'SELECT vendor , form, taxID, corpType, addresses, SUM(expenses.total - expenses.balance) as serviceFee'
    sql += ' FROM vendors INNER JOIN expenses ON vendors.vendor = expenses.payee'
    sql += ' WHERE expenses.type = \'Bill\''
    sql += ' AND SUBSTRING(expenses.dueDate, 1, 4) = \'2018\''
    sql += ' AND expenses.category != \'Travel\''
    sql += ' AND expenses.category != \'Meals & Entertainment\''
    sql += ' GROUP BY vendor'

    cursor.execute(sql) 
    result = cursor.fetchall() 
#    print(result)
    column_names = [i[0] for i in cursor.description]
    fp = open(outputFile, 'w')
    myFile = csv.writer(fp, delimiter='|', lineterminator = '\n') #use lineterminator for windows
    myFile.writerow(column_names)
    myFile.writerows(result)
    fp.close()
    print('saving annaul expenses to ' + outputFile)

def annualExpenseDetail(db, outputFile):
    
    cursor = db.cursor()
    sql = 'SELECT payee, dueDate, category, transDate, type, transNum, balance, total'
    sql += ' FROM expenses INNER JOIN vendors ON vendors.vendor = expenses.payee'
    sql += ' WHERE type = \'Bill\''
    sql += ' AND SUBSTRING(dueDate, 1, 4) = \'2018\''
    sql += ' AND category != \'Travel\''
    sql += ' AND category != \'Meals & Entertainment\''
    sql += ' ORDER BY payee, dueDate'

    cursor.execute(sql) 
    result = cursor.fetchall() 

    column_names = [i[0] for i in cursor.description]
    fp = open(outputFile, 'w')
    myFile = csv.writer(fp, delimiter='|', lineterminator = '\n') #use lineterminator for windows
    myFile.writerow(column_names)
    myFile.writerows(result)
    fp.close()
    print('saving annaul expenses detail to ' + outputFile)