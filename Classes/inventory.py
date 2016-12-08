import MySQLdb
import time


class Item_console:
    """class for all console operations"""

    def __init__(self):
        pass

    def add_item(self,itemname, description,cost, productcode,status):
        # Adding an item's details to the database so that they can be manipulated
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        date_added = time.time()
        cur.execute("INSERT INTO inventory (itemname,description,cost,productcode,dateinfo,status) VALUES('%s','%s','%s','%s','%s','%s')" % (itemname, description,cost, productcode,date_added,status))
        db.commit()
        db.close()

    def remove_item(self, item_id):
        # Removes Specific File by item_id
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        rmv_stmt = ("DELETE FROM inventory where itemid= '%s'" % (item_id))
        cur.execute(rmv_stmt)
        db.commit()
        if state:
            return "You have successfully deleted record %d", item_id
        else:
            return "Unable To Delete Record"
        db.close()

    def list_export(self, item_id):

        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        result = cur.execute("SELECT * FROM inventory")
        with open(inventory,"a") as f:
            f.write(result)
        pass
        # Exporting all the details in the inventory to a CSV file

    def item_check_out(self, item_id):
        # Check an Item out of the database

        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        status = "Checked-Out"
        cur.execute("UPDATE inventory SET status='%s' where itemid= '%s'" % (status, item_id))
        db.commit()
        db.close

    def item_check_in(self, item_id):
        # Returning an Item to warehouse
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        status = "Available"
        cur.execute("UPDATE inventory SET status='%s' where itemid= '%s'" % (status, item_id))
        db.commit()
        db.close
        pass
        # Checks in items that were initially checked out. By Item id

    def list_item(self):
        # Listing all the items in an inventory
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
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

        print options

        db.close()

    def view_type_item(self, item_code):
        # quering using unique id
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        cur.execute("SELECT * FROM inventory WHERE productcode='%d'" % (productcode))
        results = cur.fetchall()
        if results:
            return results
        else:
            print
            "It seems like the number you have entered is not relevant please try again"
        db.close()

    def item_search(self, item_id):

        # quering to view all items of specific uniqe code e.g data of all android phones
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db="inventory_management")
        cur = db.cursor()
        cur.execute("SELECT * FROM inventory WHERE itemid='%d'" % (item_id))
        results = cur.fetchall()
        if results:
            return results
        else:
            print
            "Dear User, It seems like the number you have entered is not relevant please try again"
        db.close()

    def compute_value(self):
        # Computing the sum of all the values in the inventory table
        db = MySQLdb.connect(host="localhost", user="root", passwd="andela", db = "inventory_management")
        cur = db.cursor()
        value_sum = cur.execute("SELECT SUM(cost) as value_sum FROM inventory")
        return value_sum
        db.close()
