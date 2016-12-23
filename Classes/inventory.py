import MySQLdb
import time
import sys
import csv


class Item_console:
    """class with methods that manipulate the inventory management data """

    def __init__(self):
        pass

    def add_item(self, itemname, description, cost, productcode, status):
        """
        Adding an item's details to the database so that they can be manipulated
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        date_added = time.time()
        cur.execute(
            "INSERT INTO inventory (itemname,description,cost,productcode,dateinfo,status) VALUES('%s','%s','%s','%s','%s','%s')" % (
            itemname, description, cost, productcode, date_added, status))
        db.commit()
        db.close()

    def remove_item(self, item_id):
        """
        Method that removes an Item from the Inventory's database
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        rmv_stmt = ("DELETE FROM inventory where itemid= '%s'" % (item_id))
        cur.execute(rmv_stmt)
        db.commit()
        
        return "You have successfully deleted record %s", item_id
        
        db.close()

    def list_export(self, item_id):
        """
        Method that exports all the contents of an Inventory database to a CSV data file
        """

        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        result = cur.execute("SELECT * FROM inventory")
        
        with open(inventory, "a") as f:
            f.write(result)
        pass
       
    def item_check_out(self, item_id):
        """
        Method that checks out an item from the inventory 
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        status = "Checked-Out"
        cur.execute("UPDATE inventory SET status='%s' where itemid= '%s'" % (status, item_id))
        db.commit()
        db.close

    def item_check_in(self, item_id):
        """
        Returning an Item to warehouse inventory
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        status = "Available"
        cur.execute("UPDATE inventory SET status='%s' where itemid= '%s'" % (status, item_id))
        db.commit()
        db.close
        pass
    
    def list_item(self):
        """
         Listing all the items in the warehouse inventory
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        list_stmt = ("SELECT * FROM inventory")
        cur.execute(list_stmt)
        results = cur.fetchall()
        options = list()
        for row in results:
            print("{} {} {} {} {} {} {} ").format(
                str(row[0]),
                str(row[1]),
                str(row[2]),
                str(row[3]),
                str(row[4]),
                str(row[5]),
                str(row[6]),
            )

        print
        options

        db.close()

    def view_type_item(self, product_code):
        """ 
        Querying Database using unique item_id
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        cur.execute("SELECT * FROM inventory WHERE productcode='%s'" % (product_code))
        results = cur.fetchall()
        
        return results
        db.close()

    def item_search(self, item_id):
        """
        Quering to view all items of specific uniqe code e.g data of all android phones
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        cur.execute("SELECT * FROM inventory WHERE itemid='%s'" % (item_id))
        results = cur.fetchall()
        if results:
            return results
        else:
            print
            "It seems like the number you have entered is not relevant please try again"
        db.close()

    def compute_value(self):
        """
        Computing the sum of all the values in the inventory table
        """
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        value_sum = cur.execute("SELECT SUM(cost) as value_sum FROM inventory")
        return value_sum
        db.close()

    def export_data(self):
        db = MySQLdb.connect(host="localhost", user="root", passwd="julaikumi", db="inventory_management")
        cur = db.cursor()
        cur.execute("SELECT * FROM inventory")
        results=cur.fetchall()

        c= csv.writer(open("data.csv","wb"))
        for row in results:
            c.writerow(row)
        db.close()
