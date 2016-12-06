from users import user
#bc-12-Twitter-Sentiment-Analysis/twitter_cmd.py -check that out so that you can learn how doc ops work
class itemconsole(user):
    """class for all console operations"""
    def __init__(self,*args):
        #inherit variables from users class and instanciate item variables (id,name,decription, total amount
        #cost per item, date added, checkin status
        self.db = MySQLdb.connect= (host="localhost",user="root",passwd="andela",db="inventory_management")
        self.cur=db.cursor()
        self.user_name= user_name
        self.category= category
        self.item_id = item_id
        self.name= name
        self.description= decription
        # self.total_amount= total_amount, this will be instanciatd and used in the respective fuction
        self.cost_per_item = cost_per_item
        self.date_added= date_added
        self.checkin_status= checkin_status
        self.itemcode = itemcode

    def add_item(self,*args): # Item variables (id,name,description,total amount,cost per item, date added,check status)
        add_stmt = ("INSERT INTO inventory (itemname,description, cost,date) VALUES (%s, %s, %s)"
        data = (self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        if cursor.execute(add_stmt, data)):
            return True
        else:
            return False

    def remove_item(*args):
        rmv_stmt=("DELETE FROM  inventory where item_id=")
        self.cur.execute("DELETE FROM inventory WHERE item_id=self.item_id")

    def list_item(self,*args):
        #Query to return the entire inventory
        self.cur.execute("SELECT * FROM inventory")
        for row in self.cur.fetchall():
            print row[0],row[0],row[0],row[0],row[0]
        db.close()

    def check_item(self,*args):
        #quering using unique id
        self.cur.execute("SELECT * FROM inventory WHERE itemid = self.item_id ")
        for row in self.cur.fetchall():
            print row[0],row[0],row[0],row[0],row[0]
        db.close()

    def view_item_by_id(self,*args):
        #quering to view all items of specific uniqe code e.g data of all android phones
        self.cur.execute("SELECT * FROM inventory WHERE itemid = self.item_code")
        for row in self.cur.fetchall():
            print row[0],row[0],row[0],row[0],row[0]
        db.close()

    def search_item(self,*args):
        # implementing a binary search
        self.cur.execute("SELECT itemname,description FROM inventory WHERE itemcode=self.item_code ")
        for row in self.cur.fetchall():
            print row[0],row[0],row[0],row[0],row[0]
        db.close()

    def compute_value(self,*args):
        # Computing the sum of all the values in the inventory table
        self.cur.execute("SELECT SUM(cost) as value_sum FROM inventory")
            print value_sum
        db.close()
