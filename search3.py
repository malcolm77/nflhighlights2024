from youtubesearchpython import VideosSearch

videosSearch = VideosSearch('Highlights NFL 2024', limit = 20)

# print('<h1>NFL Highlights</h1>', file=open('/var/www/html/nfl.html', 'w'))

for i in range(10):
    title = videosSearch.result()['result'][i]['title']
    link = videosSearch.result()['result'][i]['link']
    posted = videosSearch.result()['result'][i]['publishedTime']
    # print ( "%s %s ( %s )" % (title,link,posted) )
    print ( "<a href='%s'> %s ( %s ) </a><br>" % (link,title,posted) )

    #with open('/var/www/html/nfl.html', 'a') as f:
      #print ( "<a href='%s'> %s ( %s ) </a><br>" % (link,title,posted), file=f )
      # print('Filename:', filename, file=f)  # Python 3.x
