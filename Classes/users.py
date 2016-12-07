from db_connect import connection

class user(object):
    """docstring for users."""
    def __init__(self,user_name,password,category,db,cur):
        super(users, self).__init__()
        self.user_name = user_name
        self.password = password
        self.category =category
        self.db = MySQLdb.connect= (host="localhost",user="root",passwd="andela",db="inventory_management")
        self.cur=db.cursor()

class admin(users):
    """docstring for admin and operations"""
    def __init__(self, *arg):
        self.arg = arg
    def create_admin(self,user_name,password,category):
        con=dbconnect()
        con.connection()
        add_stmt = "(INSERT INTO user (name,password,category) VALUES (%s, %s)"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        data = (self.name,self.password,self.category)

        if cur.execute(add_stmt, data)):
            return True
        else:
            return False
        #code to instancicate variable and post to database
    def retrieve_user(self,user_name,password):
        con=dbconnect()
        con.connection()
        add_stmt = "(SELECT * FROM user WHERE category=%s"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        data = (self.category)

        if cur.execute(add_stmt, data)):
            return row[0],row[1],row[2],row[3]
        else:
            return False
        # code to check database and return the users information,this is to demonstrate the addition of user privileges
    def add_employee(self,user_name,password):
        #Category Set and editable to facilitate promotions
        con=dbconnect()
        con.connection()
        category="employee"
        add_stmt = "(INSERT INTO user (name,password,category) VALUES (%s, %s)"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        data = (self.name,self.password,category)

        if cur.execute(add_stmt, data)):
            return True
        else:
            return False

class employees(users):
    """docstring for employees."""
    def __init__(self,user_name,password ):
        self.user_name = user_name
        self.password = password
        self.category='employee'
    def employee_login(self,user_name,password):
        #code to check through tabase to find employee infomation and category
        con=dbconnect()
        con.connection()
        add_stmt = "(SELECT * FROM  user WHERE name=%s AND password=%s"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        data = (self.name,self.password)

        if cur.execute(add_stmt, data)):# If a record is found matching the criteria
            return True
        else:
            return False
