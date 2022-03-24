from string import ascii_lowercase as al
import pickle
from search import search
import pandas as pd

def permutation_atindex(_int, _set, length):
    """
    Return the permutation at index '_int' for itemgetter '_set'
    with length 'length'.
    """
    items = []
    strLength = len(_set)
    index = _int % strLength
    items.append(_set[index])

    for n in range(1,length, 1):
        _int //= strLength
        index = _int % strLength
        items.append(_set[index])

    return items

class PermutationIterator:
    """
    A class that can iterate over possible permuations
    of the given 'iterable' and 'length' argument.
    """

    def __init__(self, iterable, length):
        self.length = length
        self.current = 0
        self.max = len(iterable) ** length
        self.iterable = iterable

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.max:
            raise StopIteration

        try:
            return permutation_atindex(self.current, self.iterable, self.length)
        finally:
            self.current   += 1


"""
x = ""
aln = " " + al
prompts = []
count = 0
times_done = 0
for e in PermutationIterator(aln, 30):
    #print ("".join(e))
    x = "".join(e)
    print(x)
    count += 1
    prompts.append(x)
    if count == 20000000:
        times_done += 1
        filename = "prompts" + str(times_done) + ".ob"
        with open(filename, "wb") as fp:
            pickle.dump(prompts, fp)
        count = 0
        print("saving.....")
        prompts = []

n_fn = "prompts" + str(times_done + 1) + ".ob"
with open(n_fn, "wb") as fp:
    pickle.dump(prompts, fp)
"""

def createSeries (series_list):
    
  # create a series
  series_list = pd.Series(series_list)
    
  return series_list

x = ""
aln = " " + al
ids, names, channels, duration, views, publish_time = [], [], [], [], [], []
count = 0
times_done = 0

for e in PermutationIterator(aln, 20):
    #print ("".join(e))
    x = "".join(e)
    print(x)
    count += 1
    blanks = 0
    for i in range(0, len(x)):
        if x[i] == " ":
          blanks += 1
    if not blanks == len(x):
        x = x.strip()

        if len(x) > 3:

            try:
                id, name, channel, duration_1, view, publish_time_1 = search(x)
            except:
             id, name = [], []
            ids += id
            names += name
            channels += channel
            duration += duration_1
            views += view
            publish_time += publish_time_1

            print(ids, names)

            if count == 1000000:
                ids = createSeries(ids)
                names = createSeries(names)
                channels = createSeries(channels)
                duration = createSeries(duration)
                views = createSeries(views)
                publish_time = createSeries(publish_time)

                data = {"id": ids,
                        "title": names,
                        "channel": channels,
                        "duration": duration,
                        "views": views,
                        "publish_time": publish_time}
            
                df = pd.concat(data, axis=1)

                df.to_csv('songs.csv', mode='a', index=False, header=False)

                print("saving.....")
                ids, names, channels, duration, views, publish_time = [], [], [], [], [], []

ids = createSeries(ids)
names = createSeries(names)
channels = createSeries(channels)
duration = createSeries(duration)
views = createSeries(views)
publish_time = createSeries(publish_time)

data = {"id": ids,
        "title": names,
        "channel": channels,
        "duration": duration,
        "views": views,
        "publish_time": publish_time}
            
df = pd.concat(data, axis=1)
df.to_csv('songs.csv', mode='a', index=False, header=False)

print("saving.....")