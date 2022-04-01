import glob

song_dir = "/home/akshit/Music/Rama_Cassetes/"

for name in glob.glob(song_dir + "*.mp3"):
    print(name)