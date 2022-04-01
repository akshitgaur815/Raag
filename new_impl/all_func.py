import mysql.connector
import glob
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import os
from test import down_song

store_loc = '/home/akshit/Music/raag/'

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

def get_mp3(song_dir):
    return glob.glob(song_dir + "*.mp3")

"""
def down_song(url, dest):
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=dest)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
    print(new_file)
    return new_file
"""


"""
if __name__ == '__main__':
    filename = down_song('https://www.youtube.com/watch?v=BAc2Pwyw_UM', './songs/cache')
    play_song(filename)
"""

if __name__ == '__main__':
    down_song('barkha.mp3', 'https://www.youtube.com/watch?v=BAc2Pwyw_UM')