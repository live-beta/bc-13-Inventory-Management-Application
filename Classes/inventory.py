from db_connet import dbconnect
from users import user
#bc-12-Twitter-Sentiment-Analysis/twitter_cmd.py -check that out so that you can learn how doc ops work
class itemconsole:
    """class for all console operations"""
    def __init__(self,user_name,password,category,db,cur):
        #inherit variables from users class and instanciate item variables (id,name,decription, total amount
        #cost per item, date added, checkin status
        super(user_name,password,category,db,cur)
        #self.db = MySQLdb.connect= (host="localhost",user="root",passwd="andela",db="inventory_management")
        #self.cur=db.cursor()
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


    def add_item(self): # Item variables (id,name,description,total amount,cost per item, date added,check status)
        con = dbconnect()
        con.connection()
        add_stmt = "(INSERT INTO inventory (itemname,description, cost,date) VALUES (%s, %s, %s)"
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        data = (self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        if cur.execute(add_stmt, data)):
            return True
        else:
            return False
        db.close
    def remove_item(self):
        con = dbconnect()
        con.connection()
        rmv_stmt=("DELETE FROM  inventory where item_id=")
        if cur.execute("DELETE FROM inventory WHERE item_id=:id",{self.item_id}):
            return True
        else:
            return False

    def add_item(self): # Item variables (id,name,description,total amount,cost per item, date added,check status)
        con = dbconnect()
        con.connection()
        add_status = self.cur.execute("""INSERT INTO inventory (name,description,cost)
                                         VALUES(:name,:description,:cost)""",
                                         {'name':self.name,'description':self.description,'cost':self.cost}) # Id and date should add to database automatically
        if add_status:
            return True
        else:
            return False

        db.close()

    def remove_item(self):
        con = dbconnect()
        con.connection()
        remove_status= self.cur.execute("""DELETE FROM inventory WHERE itemid = :itemid""",
                                           {'itemid':self.item_id})
        if remove_status:
            return True
        else:
            return False
        db.close()

    def list_item(self):
        con = dbconnect()
        con.connection()
        #Query to return the entire inventory
        self.cur.execute("SELECT * FROM inventory")
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]
        db.close()

    def check_item(self):
        con = dbconnect()
        con.connection()
        #quering using unique id
        self.cur.execute("""SELECT * FROM inventory WHERE itemid = :item_id""",
                            {'item_id': self.item_id})
        for row in self.cur.fetchall():

            print row[0],row[0],row[0],row[0],row[0]

        db.close()

    def view_item_by_id(self):
        con = dbconnect()
        con.connection()
        #quering to view all items of specific uniqe code e.g data of all android phones
        self.cur.execute("""SELECT * FROM inventory WHERE itemcode = :item_code""",
                            {'itemcode': self.item_code})
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]

        db.close()

    def search_item(self):
        # implementing a binary search
        con = dbconnect()
        con.connection()
        self.cur.execute("""SELECT itemname,description FROM inventory WHERE itemcode= :itemcode""",
                            {'itemcode': self.item_code})
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]

        db.close()

    def compute_value(self):
        con = dbconnect()
        con.connection()
        # Computing the sum of all the values in the inventory table
        self.cur.execute("SELECT SUM(cost) as value_sum FROM inventory")

            print value_sum
        db.close()
