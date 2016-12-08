import MySQLdb
import time
#from db_connet import dbconnect
#from users import user
#bc-12-Twitter-Sentiment-Analysis/twitter_cmd.py -check that out so that you can learn how doc ops work
class itemconsole:
    """class for all console operations"""
    def __init__(self):
        pass

    def add_item(self,itemname,description,cost,productcode):
        # Adding an item's details to the database so that they can be manipulated.
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        date_added=time.time()
        status="Available"
        cur.execute("INSERT INTO inventory (itemname,description,cost,productcode,dateinfo,status) VALUES ('%s','%s','%s','%s','%s','%s')" %(itemname,description,cost,productcode,date_added,status))
        db.commit()
        db.close()

    def remove_item(self,item_id):
        #Removes Specific File by item_id
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

    def list_export(self, item_id):
        # Exporting all the details in the inventory to a CSV file
    def item_check_out(self,item_id):
        # Checks out the item from the warehouse database.
    def item_check_in(self,item_id):
        # Checks in items that were initially checked out. By Item id

    def list_item(self):
        #Listing all the items in an inventory
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        list_stmt=("SELECT * FROM inventory")
        results= cur.fetchall()
        return results
        db.close()

    def view_type_item(self,item_code):
        #quering using unique id
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        cur.execute("SELECT * FROM inventory WHERE productcode='%d'" %(productcode))
        results=cur.fetchall()
        if results:
            return results
        else:
            print "Dear User, It seems like the number you have entered is not relevant please try again"
        db.close()

    def item_search(self,item_id):

        #quering to view all items of specific uniqe code e.g data of all android phones
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
        cur.execute("SELECT * FROM inventory WHERE itemid='%d'" %(item_id))
        results=cur.fetchall()
        if results:
            return results
        else:
            print "Dear User, It seems like the number you have entered is not relevant please try again"
        db.close()
    def search_query(self,item_code):
        # Finds Items with productcode and availability
        
    def compute_value(self):
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()

        # Computing the sum of all the values in the inventory table
        cur.execute("SELECT * SUM(cost) as value_sum FROM inventory")
        value_sum= cur.execute("SELECT SUM(cost) as value_sum FROM inventory")
        print value_sum
        db.close()

obj=itemconsole()
del_value= raw_input('id to be deleted')
del_value=int(del_value)

print obj.remove_item(del_value)
