import sqlite3 as lite
import sys

con = lite.connect('test.db')

with con:

cur = con.cursor()
con.execute("CREATE TABLE IF NOT EXISTS admin(adminNameID REAL, Name TEXT, Contact REAL, Facility TEXT, Request TEXT, Date REAL, Status TEXT, Approved TEXT, Rejected TEXT, Comment TEXT)")
con.execute("CREATE TABLE IF NOT EXISTS staff(staffNameID REAL, ContactInfo REAL, Specification TEXT, RepairCase TEXT, Report TEXT)")

print ("Table(s) created successfully!")

cur.execute("INSERT INTO admin VALUES(1,'Ivy', +254701511738, 'Leisure', ?, ?, ?, ?, ?, ?)")
cur.execute("INSERT INTO admin VALUES(2,'Austin', +254716586854, 'Resource', ?, ? ,?, ?, ?, ?)")
cur.execute("INSERT INTO admin VALUES(3,'Boni', +254712846939, 'Laundry', ?, ?, ?, ?, ?, ?)")
cur.execute("INSERT INTO admin VALUES(4,'Charlie', +254714479529, 'Entertainment', ?, ?, ?, ?, ?, ?)")
cur.execute("INSERT INTO staff VALUES(11,'Fawaz', +254725320720, 'LeisurePerson1', ?, ?)")
cur.execute("INSERT INTO staff VALUES(22,'David', +256781916689, 'ResourcePerson1', ?, ?)")
cur.execute("INSERT INTO staff VALUES(33,'Michael', +254702914761, 'LaundryPerson1', ?, ?)")
cur.execute("INSERT INTO staff VALUES(44,'Bob', +254723799217, 'EntertainmetPerson1', ?, ?)")

