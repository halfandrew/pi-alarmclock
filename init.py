#!/usr/bin/python

from subprocess import call
import sys
import re
import urllib
import feedparser


def outputToAudio(source):

   # Encode our query
   query = urllib.urlencode({
     'src' : source,
     'hl' : 'en-us', #language en-gb, en-au, en-ca, en-us
     'r' : '-2', #reading speed
     'f' : '24khz_16bit_stereo' #audio format
   })
   # Use mpg123 to play the resultant MP3 file from Voice RSS
   #call(["mpg123","-q","http://api.voicerss.org/?key=8934147f4bfd423387f511a176edafc4&" + query])
   call(["mpg123", "http://api.voicerss.org/?key=8934147f4bfd423387f511a176edafc4&" + query])
   return;


   # BBC World News
try: 
    rss = feedparser.parse('http://feeds.bbci.co.uk/news/world/rss.xml')

    newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  ' 

# print newsfeed
    newsfeed = newsfeed.encode('utf-8')

# Today's news from BBC
    news = 'And now, The latest stories from the World section of the BBC News.  ' + newsfeed
    
except rss.bozo:
    news = 'Failed to reach BBC News'

outputToAudio(news)

#BBC Football
try: 
    rss = feedparser.parse('http://feeds.bbci.co.uk/sport/0/football/rss.xml?edition=uk')

    newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  ' 

# print newsfeed
    newsfeed = newsfeed.encode('utf-8')

# Today's news from BBC
    football = 'And now, The latest stories from BBC Football.  ' + newsfeed
    
except rss.bozo:
    football = 'Failed to reach BBC News'

outputToAudio(football)
