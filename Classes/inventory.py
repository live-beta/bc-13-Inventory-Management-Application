import MySQLdb
import time
#from db_connet import dbconnect
#from users import user
#bc-12-Twitter-Sentiment-Analysis/twitter_cmd.py -check that out so that you can learn how doc ops work
class itemconsole:
    """class for all console operations"""
    def __init__(self):
        pass
        """
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
        """
    def add_item(self,itemname,description,cost,productcode): # Item variables (id,name,description,total amount,cost per item, date added,check status)
        #add_stmt += add_stmt.format(self.name,self.description,self.cost,self.status, datetime.date(2012, 3, 23))
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        date_added=time.time()
        status="Available"
        cur.execute("INSERT INTO inventory (itemname,description,cost,productcode,dateinfo,status) VALUES ('%s','%s','%s','%s','%s','%s')" %(itemname,description,cost,productcode,date_added,status))
        db.commit()
        db.close()

    def remove_item(self,item_id):
        rmv_stmt=("DELETE FROM inventory where item_id= '%s'" %(item_id))
        db.commit()
        if rmv_stmt:
            return True
        else:
            return False

    def add_itemn(self): # Item variables (id,name,description,total amount,cost per item, date added,check status)

        add_status = self.cur.execute("""INSERT INTO inventory (name,description,cost)
                                         VALUES(:name,:description,:cost)""",
                                         {'name':self.name,'description':self.description,'cost':self.cost}) # Id and date should add to database automatically
        if add_status:
            return True
        else:
            return False

        db.close()

    def remove_item(self):

        remove_status= self.cur.execute("""DELETE FROM inventory WHERE itemid = :itemid""",
                                           {'itemid':self.item_id})
        if remove_status:
            return True
        else:
            return False
        db.close()

    def list_item(self):

        #Query to return the entire inventory
        self.cur.execute("SELECT * FROM inventory")
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]
        db.close()

    def check_item(self):

        #quering using unique id
        self.cur.execute("""SELECT * FROM inventory WHERE itemid = :item_id""",
                            {'item_id': self.item_id})
        for row in self.cur.fetchall():

            print row[0],row[0],row[0],row[0],row[0]

        db.close()

    def view_item_by_id(self,item_id):

        #quering to view all items of specific uniqe code e.g data of all android phones
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        #add_stmt = "SELECT * FROM user WHERE password=?",(password)
        #add_stmt += add_stmt.format(password)
        #data = ('password':password)
        #if cur.execute("SELECT * FROM user WHERE password = ?",(password)):
        #    return row[0],row[1],row[2],row[3]
        #else:
        #    return False
        cur.execute("SELECT * FROM inventory WHERE itemid='%s'" %(item_id))
        results=cur.fetchall()
        if results:
            return results
        else:
            print "Dear User, It seems like the number you have entered is not relevant please try again"


    def search_item(self):
        # implementing a binary search

        self.cur.execute("""SELECT itemname,description FROM inventory WHERE itemcode= :itemcode""",
                            {'itemcode': self.item_code})
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]

        db.close()

    def compute_value(self):

        # Computing the sum of all the values in the inventory table
        self.cur.execute("SELECT SUM(cost) as value_sum FROM inventory")

        print value_sum
        db.close()

obj=itemconsole()
#itemname = raw_input('Enter Item Name')
#description =raw_input('Enter Description')
#cost= raw_input('Cost')
#productcode=raw_input('productcode')
#obj.add_item(itemname,description,cost,productcode)
print obj.view_item_by_id(0)
