import sqlite3

connect = sqlite3.connect('emaildb.sqlite')
cur = connect.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

filename = raw_input('Enter file name: ')
if len(filename) < 1:
    filename = 'mbox.txt'

dbhandle = open(filename)
for line in dbhandle:

    if not line.startswith('From: '):
        continue
    else:
        email = line.split()[1]
        org = email.split('@')[1]
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (org, ))

        try:
            count = cur.fetchone()[0]
            cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (org, ))
        except:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))
connect.commit()
