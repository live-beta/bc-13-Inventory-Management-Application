import MySQLdb
class dbconnect:
    """docstring for ."""
    def __init__(self):
        super(, self).__init__()


    def connection():
        db = MySQLdb.connect(host="localhost",user="root",passwd="andela",db="inventory_management")
        cur=db.cursor()
