import os
import random
import string
import json
import sqlite3

conn = sqlite3.connect('dummydata.db')

cur = conn.cursor()

print('connected to db')

random.seed = (os.urandom(1024))

emailsEnd = ['@Gmail.com','@Yahoo.com','@sky.net','@sharklasers.com','@Hotmail.co.uk','@hotmail.com','@email.net','@freemail.com']
postcodes = ['SE','SW','S','N','NE','NW']
Fnames = json.loads(open('Fnames.json').read())
Lnames = json.loads(open('Lnames.json').read())
roads = json.loads(open('roads.json').read())
lasts = Lnames
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
charsletters = string.ascii_letters
custID = 1

for name in Fnames:
	lastName = str(''.join(random.choice(lasts)))
	fullName = str(name + ' ' + lastName)
	Add1 = str(random.randint(1,300)) + ', ' +''.join(random.choice(roads))
	Add2 = str(' ')
	Add3 = str(' ')
	postCode = str((random.choice(postcodes)) + str(random.randint(1,20)) + ' ' + str(random.randint(1,9)) + str(random.choice(charsletters)) + (random.choice(charsletters))).upper()
	telNo = str('+4400000111222')
	name_extra = str(''.join(random.choice(string.digits)))
	emailAt = str(''.join(random.choice(emailsEnd)))
	email = str( name.lower() + name_extra + emailAt)
	query = ('INSERT INTO customers (FirstName,LastName,Email,Addr1,Addr2,Addr3,Postcode,TelNo) VALUES ("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}" )').format(name,lastName, email, Add1, Add2, Add3, postCode, telNo)
	conn.execute(query)
	print('inserting data for', fullName, email)
	custID = custID + 1

conn.commit()
conn.close()

