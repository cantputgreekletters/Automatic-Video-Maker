def get_text_list(s:str,n:int):

  #Edit your details in this file
  file_loc = "reddit_account.json"
  import json
  #Opens the file and gets the data
  with open (file_loc,"r") as file:
    data = json.load(file)

  del json
  

  import praw
  
  #Connects to reddit
  reddit_read_only = praw.Reddit(client_id=data["client_id"],         # your client id
                                 client_secret=data["client_secret"],      # your client secret
                                 user_agent=data["user_agent"])        # your user agent
  
  del data,file_loc

  #Gets the text from the top section of the specified subbreddit
  subreddit = reddit_read_only.subreddit(s)
  del options
  Post_Text_list = []
  for posts in subreddit.top(limit = n):
      
    Post_Text_list.append(posts.selftext)
  return(Post_Text_list)
#Returns all the text from all the posts