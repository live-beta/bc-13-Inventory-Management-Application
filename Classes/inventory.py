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

        #Delets and item from  a list using the item_id
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        rmv_stmt=("DELETE FROM inventory where itemid= '%s'" %(item_id))
        cur.execute(rmv_stmt)
        db.commit()
        if rmv_stmt:
            return True
        else:
            return False
        db.close()

    def list_item(self):
        #Listing all the items in an inventory
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        list_stmt=("SELECT * FROM inventory")
        results= cur.fetchall()
        return results
        db.close()

    def check_type_item(self):
        #quering using unique id
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        #add_stmt = "SELECT * FROM user WHERE password=?",(password)
        #add_stmt += add_stmt.format(password)
        #data = ('password':password)
        #if cur.execute("SELECT * FROM user WHERE password = ?",(password)):
        #    return row[0],row[1],row[2],row[3]
        #else:
        #    return False
        cur.execute("SELECT * FROM inventory WHERE productcode='%d'" %(productcode))
        results=cur.fetchall()
        if results:
            return results
        else:
            print "Dear User, It seems like the number you have entered is not relevant please try again"
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
        cur.execute("SELECT * FROM inventory WHERE itemid='%d'" %(item_id))
        results=cur.fetchall()
        if results:
            return results
        else:
            print "Dear User, It seems like the number you have entered is not relevant please try again"
        db.close()

    def compute_value(self):
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()

        # Computing the sum of all the values in the inventory table
        cur.execute("SELECT * SUM(cost) as value_sum FROM inventory")
        value_sum= cur.execute("SELECT SUM(cost) as value_sum FROM inventory")
        print value_sum
        db.close()

obj=itemconsole()
#itemname = raw_input('Enter Item Name')
#description =raw_input('Enter Description')
#cost= raw_input('Cost')
#productcode=raw_input('productcode')
#obj.add_item(itemname,description,cost,productcode)
del_value= raw_input('id to be deleted')
del_value=int(del_value)

print obj.remove_item(del_value)
