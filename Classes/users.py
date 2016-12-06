class users(object):
    """docstring for users."""
    def __init__(self,user_name,password,category):
        super(users, self).__init__()
        self.user_name = user_name
        self.password = password
        self.category =category
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

class itemconsole(users):
    """class for all console operations"""
    def __init__(self,*args):
        #inherit variables from users class and instanciate item variables (id,name,decription, total amount
        #cost per item, date added, checkin status
        self.user_name= user_name
        self.category= category
        self.item_id = item_id
        self.name= name
        self.description= decription
        self.total_amount= total_amount
        self.cost_per_item = cost_per_item
        self.date_added= date_added
        self.checkin_status= checkin_status

    def add_item(*args): # Item variables (id,name,description,total amount,cost per item, date added,check status)
        pass
    def remove_item(*args):
        pass
    def list_item(*args):
        pass
    def check_item(*args):
        pass
    def view_item_by_id(*args):
        pass
    def search_item(self,*args):
        pass
    def compute_value(self,*args):
        pass
