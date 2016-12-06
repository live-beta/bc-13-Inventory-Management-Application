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
        #code to instancicate variable and post to database
    def retrieve_user(self,user_name,password):
        # code to check database and return the users information,this is to demonstrate the addition of user privileges
    def add_employee(self,user_name,password):
        #Category Set and editable to facilitate promotions
class employees(users):
    """docstring for employees."""
    def __init__(self,user_name,password ):
        self.user_name = user_name
        self.password = password
        self.category='employee'
    def employee_login(self,user_name,password):
        #code to check through tabase to find employee infomation and category
        return login_status
    def employee_console(self,employee_login):# calling the loin function
        if login_status == True:
            # load the user login console
        else:
            print "login unsuccessful"
