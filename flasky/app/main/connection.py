conn = sqlite3.connect('database.db')
print ("Connection successful!")
c = conn.cursor()


c.close()
conn.close()
