from get_channel import get_channel
from pytube import YouTube as YT
import pandas as pd
from search import isWordPresent

channels = ['channel/UCcgkLbQ6nDIh4slTfOsh2IQ/videos', 'c/tseriesregional', 'c/MGVDIGITALofficial/', 'channel/UCl1oDpiuEzmcg6zyxh_1Now', 'c/pandavaas']
triggers= ['garhwali', 'kumaoni', 'uttarakhandi', 'pahadi', 'UTTRAKHANDI', 'jagar', 'jaagar']
to_ign = ['lyric', 'lyrics', 'lyrical', 'videography', 'cover', 'interview', 'status', 'choreography', 'jukebox', 'full movie', 'comedy', 'sketch', 'promo', 'teaser',
         'trailer', 'official video', 'kavita', 'film', 'shooting', 'casting']


url_list = get_channel([channels[1]])
print("\n" * 5)

data = {'title': [],
        'length': [],
        'publish_date': [],
        'author': [],
        'url': []}
df = pd.DataFrame(data)

for url in url_list:
    vid = YT(url)
    title = vid.title
    print(f"Considering:  {title}")
    
    """
    for word in triggers:
        if isWordPresent(title, word):
            for rem_word in to_ign:
                if not isWordPresent(title, rem_word):
                    new_row = {'title': vid.title, 'length': vid.length, 'publish_date': vid.publish_date, 'author': vid.author, 'rating': vid.rating, 'url': url}
                    print(f"Accepted:  {title}")
                    df = df.concat(new_row)
                    break
    """
    
    for word in triggers:
        if isWordPresent(title, word):
            new_row = {'title': vid.title, 'length': vid.length, 'publish_date': vid.publish_date, 'author': vid.author, 'url': url}
            #n_row = pd.Series(new_row)
            print(f"Accepted:  {title}")
            #df = pd.concat(df, n_row)
            df = df.append(new_row, ignore_index=True)
            break
    
    for word in to_ign:
        if isWordPresent(title, word):
            print(f"Removed:  {title}")
            i = df.index[df['title'] == title]
            df.drop(i, inplace=True)
            break

print(df)
df.to_csv('t-series.csv')