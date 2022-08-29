from pytube import YouTube

link = [
    # paste link here
]


for i in link:
    yt = YouTube(i)  
    try:
        cc = yt.streams.filter(progressive = True, 
    file_extension = "mp4").first().download()
        print("Download Done:", i)
    except Exception as e:
        print("Some Error!" , str(e))
    print('Task Completed!')
