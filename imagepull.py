import requests
import praw
reddit = praw.Reddit(client_id='2yorWXA62-FR7Q', client_secret="AaB5-mNodK2rqtJl2gQKb6AwZ04",
                     password='jcsm2009', user_agent='vote_predictor',
                     username='myers_1091')

# # Output score for the first 256 items on the frontpage
sublist = 'me_irl+dankmemes+meirl+2meirl4meirl'
outdir = 'imagedump/'
for submission in reddit.subreddit(sublist).top('week',limit=10):
	#print(submission.title)
	id = submission.id
	domain = str(submission.domain)
	if domain == 'i.redd.it' or domain == 'imgur.com':
		url = submission.url
		ext = url[len(url)-3:len(url)]
		filename = url.split('/')[-1]
		r = requests.get(url,allow_redirects=True)
		open(outdir+filename,'wb').write(r.content)
		
	# for top_level_comment in submission.comments:
	# 	print(top_level_comment.body)
