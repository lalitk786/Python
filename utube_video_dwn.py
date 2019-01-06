#Script to download youtube vidoes HD
#used python2

print ("Enter URL---")
from pytube import YouTube
f=raw_input()
print('Downloading.....')
YouTube(f).streams.first().download()
print ('Lalit..Your download has been completed....')
