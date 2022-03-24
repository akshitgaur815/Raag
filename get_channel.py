from pytube import Channel
 
 
def get_channel(channel_list):
    url_list = []
    for channel in channel_list:
        c = Channel(f'https://www.youtube.com/{channel}/videos') 
        for url in c.video_urls: 
            print(url)
            url_list.append(url)
    return url_list
 
 
if __name__ == '__main__': 
    channel = input("Channel ID with 'c/' or 'channel/:  ")
    get_channel(channel)