from urllib2 import urlopen

website = urlopen("https://api.twitch.tv/kraken/channels/nonamer69xd/follows")
followers = website.read()

print followers[1:1]