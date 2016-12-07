from users import user

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
        self.total_amount= total_amount
        self.cost_per_item = cost_per_item
        self.date_added= date_added
        self.checkin_status= checkin_status
        self.itemcode = itemcode

    def add_item(self): # Item variables (id,name,description,total amount,cost per item, date added,check status)
        add_status = self.cur.execute("""INSERT INTO inventory (name,description,cost)
                                         VALUES(:name,:description,:cost)""",
                                         {'name':self.name,'description':self.description,'cost':self.cost}) # Id and date should add to database automatically
        if add_status:
            return True
        else:
            return False

    def remove_item(self):
        remove_status= self.cur.execute("""DELETE FROM inventory WHERE itemid = :itemid""",
                                           {'itemid':self.item_id})
        if remove_status:
            return True
        else:
            return False

    def list_item(self):
        #Query to return the entire inventory
        self.cur.execute("SELECT * FROM inventory")
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]

    def check_item(self):
        #quering using unique id
        self.cur.execute("""SELECT * FROM inventory WHERE itemid = :item_id""",
                            {'item_id': self.item_id})
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]

    def view_item_by_id(self):
        #quering to view all items of specific uniqe code e.g data of all android phones
        self.cur.execute("""SELECT * FROM inventory WHERE itemcode = :item_code""",
                            {'itemcode': self.item_code})
        for row in self.cur.fetchall():
            print row[0],row[1],row[2],row[3],row[4]

    def search_item(self):
        # implementing a binary search
        self.cur.execute("""SELECT itemname,description FROM inventory WHERE itemcode= :itemcode""",
                            {'itemcode': self.item_code})
        for row in self.cur.fetchall():
            print row[1],row[2],row[3],row[4],row[5]

    def compute_value(self):
        # Computing the sum of all the values in the inventory table
        self.cur.execute("SELECT SUM(cost) as value_sum FROM inventory")
            print value_sum
