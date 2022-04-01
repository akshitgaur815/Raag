import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="Raag"
)

mycursor = mydb.cursor()


def get_data(row_req, list):
  myresult = []
  x = ", ".join(map(str, list))
  sql = "SELECT * FROM clean_data WHERE number NOT IN (" + x + ") ORDER BY points DESC"
  mycursor.execute(sql)
  for i in range(0, row_req):
    res = mycursor.fetchone()
    myresult.append(res)
  
  return myresult

if __name__ == '__main__':
  list = [1,2,3,4,5]
  res = get_data(20, list)
  for x in res:
    print(x)
    print("\n")