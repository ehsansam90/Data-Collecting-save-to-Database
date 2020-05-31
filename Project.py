import mysql.connector

#below func is for adding to mysql file if necesserly
def add_mysql(n):
    cnx = mysql.connector.connect(user='ehsan', password='apolo11',
                                  host='127.0.0.1',
                                  database='learn')
    i = 0
    while i < n:
        name = input()
        weight = int(input())
        height = int(input())
        cursor = cnx.cursor()
        cursor.execute('INSERT INTO project VALUES(\'%s\',\'%i\',%i)' % (name, weight, height))
        cnx.commit()
        i += 1

    cnx.close()

# below code is for read from mysql file as the condition wanted
cnx = mysql.connector.connect(user='ehsan', password='apolo11',
                                  host='127.0.0.1',
                                  database='learn')
cursor=cnx.cursor()
query = 'SELECT * FROM project'
cursor.execute(query)
list_data= list()
for data in cursor:
    list_data.append(data)

list_data.sort(key = lambda i:i[1])
list_data.sort(key = lambda i :i[2], reverse = True)
for data in list_data:
    print('%s %i %i'%(data[0],data[2],data[1]))

























