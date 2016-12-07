import MySQLdb

from db_connect import dbconnect

class admin(object):
    """docstring for admin and operations"""
    def __init__(self):
        pass

        #user.__init__(self,user_name,password,category)
        #self.arg = arg
        #self.category=category
        #self.user_name=user_name
        #self.password=password

    def create_admin(self,user_name,password,category):
        con=dbconnect()
        con.connection()
        cur.db.cursor()

        add_stmt = "(INSERT INTO user (name,password,category) VALUES (%s, %s)"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        data = (self.name,self.password,self.category)

        if cur.execute(add_stmt, data):
            return True
        else:
            return False
        #code to instancicate variable and post to database
    def retrieve_user(self,uname):
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        #add_stmt = "SELECT * FROM user WHERE password=?",(password)
        #add_stmt += add_stmt.format(password)
        #data = ('password':password)
        #if cur.execute("SELECT * FROM user WHERE password = ?",(password)):
        #    return row[0],row[1],row[2],row[3]
        #else:
        #    return False
        cur.execute("SELECT * FROM user WHERE name='%s'" %(uname))
        results=cur.fetchall()
        print results
    # code to check database and return the users information,this is to demonstrate the addition of user privileges
    def add_employee(self,user_name,password):
        #Category Set and editable to facilitate promotions
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        category= "employee"
        cur.execute("INSERT INTO user (name,password,category) VALUES ('%s','%s','%s')" %(user_name,password,category))
        db.commit()
        db.close()
        #category="employee"
        #add_stmt = "(INSERT INTO user (name,password,category) VALUES (%s, %s)"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        #data = (self.name,self.password,category)

        #if cur.execute(add_stmt, data):
        #    return True
        #else:
        #    return False

class employees(object):
    """docstring for employees."""
    def __init__(self):
        pass
        #self.user_name = user_name
        #self.password = password
        #self.category='employee'
    def employee_login(self,user_name,password):
        #code to check through tabase to find employee infomation and category
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        #con=dbconnect()
        #con.connection()
        cur.execute("SELECT * FROM user WHERE name='%s' AND password='%s'" %(user_name,password))
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        result = cur.fetchall()

        if result:# If a record is found matching the criteria
            return True
        else:
            return False

obj=employees()
user_name = raw_input("Enter User Name")
user_password=raw_input("Enter Password")

print "login", obj.employee_login(user_name,user_password)

#print "You Have successfully Added ", obj.retrieve_user(user_name)
