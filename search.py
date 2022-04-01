import youtube_dl
from youtube_search import YoutubeSearch as YS
from playsound import playsound as ps
import threading

store_loc = '/home/akshit/Music/raag/'

def remove_punc(test_str):
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
 
    # Removing punctuations in string
    # Using loop + punctuation string
    for ele in test_str:
        if ele in punc:
            test_str = test_str.replace(ele, "")
    
    return test_str

def isWordPresent(sentence, word):
     
    sentence = sentence.lower()
    sentence = remove_punc(sentence)
    word = word.lower()
    # To break the sentence in words
    s = sentence.split(" ")
 
    for i in s:
        i = i.lower()
        # Comparing the current word
        # with the word to be searched
        if (i == word):
            return True
    return False


def search(prompt):
    max_n = 5
    results = YS(prompt, max_results=max_n).to_dict()

    ids = []
    names = []
    channels = []
    duration = []
    views = []
    publish_time = []
    triggers= ['garhwali', 'kumaoni', 'uttarakhandi', 'pahadi', 'UTTRAKHANDI']
    to_ign = ['lyric', 'lyrics', 'lyrical', 'videography', 'cover', 'interview', 'status', 'choreography', 'jukebox', 'full movie', 'comedy', 'sketch']

    for i in range(0, max_n):
        """
        print(i)
        print(results[i]['id'])
        print(results[i]['title'])
        print(results[i]['channel'])
        print("\n")
        """
        for word in triggers:
            if (isWordPresent(results[i]['title'], word)):
                ids.append(results[i]['id'])
                names.append(results[i]['title'])
                channels.append(results[i]['channel'])
                duration.append(results[i]['duration'])
                views.append(results[i]['views'])
                publish_time.append(results[i]['publish_time'])
                break
    
    #print(ids, names)

    for n_rem in to_ign:
        for name in names:
            if (isWordPresent(name, n_rem)):
                i = names.index(name)
                names.remove(name)
                ids.remove(ids[i])
                print("Name removed:  " + name)
                print("For " + n_rem)
                
    
    #print(ids, names)

    """
    new_names = []
    new_ids = []

    for name in names:
        if (isWordPresent(name, prompt)):
            new_names.append(name)
    
    for name in new_names:
        i = names.index(name)
        new_ids.append(ids[i])

    print(new_ids, new_names)        
    """


    return ids, names, channels, duration, views, publish_time


def down(x, ids, names):
    for i in range(x, len(ids)):
        id = ids[i]
        name = names[i]
        url = "https://www.youtube.com/watch?v=" + id
        print(url)
        filename = store_loc + name + ".mp3"
        print(filename + "\n")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': filename,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
                }]
            }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

def play(names):
    for i in range(0, len(names)):
        name = names[i]
        filename = store_loc + name + ".mp3"
        ps(filename)

if __name__ == '__main__':
    prompt = input("Search: ")
    ids, names, _, _, _, _ = search(prompt)

    down(0, [ids[0]], [names[0]])

    dwn = threading.Thread(target=down, args=(1, ids, names,))
    pl = threading.Thread(target=play, args=(names,))

    dwn.start()
    pl.start()