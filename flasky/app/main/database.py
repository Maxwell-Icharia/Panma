import sqlite3 as lite

con = lite.connect('database.db')
cur = con.cursor()

def addAdmin():
	IDnumber = raw_input("Enter your id number here: ")
	name = raw_input("Enter your name here: ")
	contactinfo = raw_input("Enter your contact number: ")
	workarea = raw_input("Please specify area of work: ")
	status = raw_input("Enter whether rejected or approved: ")
	comment = raw_input("Enter your comment on the work done by the staff: ")

	with con:

		con.execute("CREATE TABLE IF NOT EXISTS admin(adminNameID REAL, Name TEXT, ContactInfo REAL, Facility TEXT, RepaircaseStatus TEXT, Comment TEXT)")
		cur.execute("INSERT INTO admin(adminNameID, Name, ContactInfo, Facility, RepaircaseStatus, Comment) VALUES (?, ?, ?, ?, ?, ?)",
			(IDnumber, name, contactinfo, workarea, status, comment))

		print ("Table(s) created successfully!")
		con.commit()

def addStaff():
	IDnumber = raw_input("Enter your id number here: ")
	name = raw_input("Enter your name here: ")
	contactinfo = raw_input("Enter your contact number: ")
	specificarea = raw_input("Please specify area of work: ")
	repaircase = raw_input("Enter whether rejected or approved: ")
	report = raw_input("Enter your comment on the work done by the staff: ")

	with con:

		con.execute("CREATE TABLE IF NOT EXISTS staff(staffNameID REAL, StaffName, ContactInfo REAL, Specification TEXT, RepairCase TEXT, Report TEXT)")

		cur.execute("INSERT INTO staff(staffNameID, StaffName, ContactInfo, Specification, RepairCase, Report) VALUES (?, ?, ?, ?, ?, ?)",
			(IDnumber, name, contactInfo, specificarea, repaircase, report))

		print ("Data inserted successfully!")

		con.commit()
		con.close()
		cur.close()


if __name__ == "__main__":
    addAdmin().run(debug=True)