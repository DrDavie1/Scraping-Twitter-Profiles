import snscrape.modules.twitter as st
import pandas as pd

usernames = []
names = []
follower_counts = []
locations = []
descriptions = []
urls = []
data = pd.read_csv('ElonFollowing.csv')
userIds = data['users']
usersID_str = []

#converting into strings 
for i in userIds:
    usersID_str.append(str(i))

value = 0
for i in usersID_str:

	value += 1 
	print(value)
	try:
		scraper = st.TwitterUserScraper(i, isUserId = True)
		usernames.append(scraper.entity.username)
		follower_counts.append(scraper.entity.followersCount)
		names.append(scraper.entity.displayname)
		locations.append(scraper.entity.location)
	
		descriptions.append(scraper.entity.description)
    
		urls.append(scraper.entity.url)
	except:
		usernames.append("Not Found")
		follower_counts.append("Not Found")
		names.append("Not Found")
		locations.append("Not Found")
		descriptions.append("Not Found")
		urls.append("Not Found")

data = pd.DataFrame({"Name":names,"Handle":usernames,"Followers":follower_counts,"Location":locations,"Bio":descriptions,"URL":urls})
data.to_csv('UserDetails.csv')