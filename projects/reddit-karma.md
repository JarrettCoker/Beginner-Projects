### Compare Recent reddit Karma
Since we're all redditors here, let's make something dealing with reddit. If you go to a user's profile and add .json to the end of it, you can get the all sorts of Json data about the user (think of Json as a giant dictionary of smaller dictionaries and lists). For example, if I go to my own profile and view it's Json data, it would look like this[1]. At first it might look intimidating, but if you break it down, you can see it's just one giant dictionary with all sorts of information about my latest posts.
- Create a program that gets information about two different users, and then sees whose most recent post received the most karma.
- The program should then print out which user received more karma, and what the difference was.
- This is a pretty open project, so I encourage you to take it further by adding more features if you find it interesting.
- Remember - Elements in a list are referenced by their index numbers while entries in a dictionary are referenced by their keys.
- Subgoals:
  - Allow the user to put in the name of two different users when the program first begins.
  - If one of the names of the users does not exist (because of a spelling error), print out a message saying so.
  - Allow the user to keep comparing other users until the program is closed.
  - Display the amount of upvotes and downvotes each user received for their posts.
  - Not sure how to turn json data into usable python data? Check [this](http://www.pythonforbeginners.com/python-on-the-web/parse-json-objects-in-python/) out.

####N.B.
According to [Reddit API](https://github.com/reddit/reddit/wiki/API) 

>"Many default User-Agents (like "Python/urllib" or "Java") are drastically limited to encourage unique and descriptive user-agent strings."

Which means that, more often than not, you will be getting Error 429 (Too many requests). You can try mitigating this with a try/except but that won't be optimal as it can hang for a good minute or two as it will only make things worse.

What you need to do is specify a header in your http request:
```python
  header = { 'User-Agent' : 'A simple descriptive header' }
  req = urllib2.Request(url, headers=header)
  #then use urllib2.urlopen(req) however you want
```

Make sure **NOT** to copy the User-Agent headers of browsers or popular reddit-bots as it will result in ban. [[1]](https://github.com/reddit/reddit/wiki/API)



##### Solutions
- [RustyHook](https://github.com/RustyHook/reddit-karma/blob/master/reddit_karma.py)
