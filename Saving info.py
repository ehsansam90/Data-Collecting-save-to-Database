import mysql.connector
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
#defining a func for testing the correct format of email
def check(email):
    if(re.search(regex,email)):
        return True
    else:
        return False

#a loop for importin user and pass into mysql
while True:

    username = input('Username: ')
    password = input('Password: ')

    if check(username) == True:
        cnx = mysql.connector.connect(user='root', password='apolo11',
                                      host='127.0.0.1',
                                      database='project')
        cursor = cnx.cursor()
        cursor.execute('INSERT INTO project VALUES(\'%s\',\'%s\')' % (username, password))
        cnx.commit()
        cnx.close()
        break
    else:
        print('\nCorrect type of email is: expression@string.string\n')































