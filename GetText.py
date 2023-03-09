def get_text_list():
  file_loc = "L:\Code\AutomaticVideoMaker\\redditId.json"
  import json
  with open (file_loc,"r") as file:
    data = json.load(file)

  del json
  
  import praw
  
   
  reddit_read_only = praw.Reddit(client_id=data["client_id"],         # your client id
                                 client_secret=data["client_secret"],      # your client secret
                                 user_agent=data["user_agent"])        # your user agent
  
  del data,file_loc

  subreddit = reddit_read_only.subreddit("pettyrevenge")
  Post_Text_list = []
  for posts in subreddit.top(limit = 3):
      
    Post_Text_list.append(posts.selftext)
  return(Post_Text_list)
