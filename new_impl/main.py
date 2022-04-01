from test import down_song
import mysql.connector
import glob

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


down_song('./barkha.wav', 'https://www.youtube.com/watch?v=BAc2Pwyw_UM')
import pygame
pygame.init()
pygame.mixer.init()
sound = pygame.mixer.music.load("./barkha.wav")
pygame.mixer.music.set_volume(0.9)   # Now plays at 90% of full volume.
pygame.mixer.music.play()
pygame.event.wait()