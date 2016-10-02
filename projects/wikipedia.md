### Random Wikipedia Article
If you've been to Wikipedia, you may have noticed that there is a link to a random article on the left side of the screen. While it can be fun to see what article you get taken to, sometimes it would be nice to see the name of the article so you can skip it if it sounds boring. Luckily, Wikipedia has an API that allows us to do so [Click here](https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json).
However, there is a dilemma. Since Wikipedia has articles about topics from all over the world, some of them have special characters in the title. For example, the article about the spanish painter [Erasto Cortés Juárez](https://en.wikipedia.org/wiki/Erasto_Cort%C3%A9s_Ju%C3%A1rez) has é and á in it. If you look at this specific article's [API](https://en.wikipedia.org/w/api.php?action=query&prop=info&pageids=39608394&inprop=url&format=json), you will see that the title is "Erasto Cort\u00e9s Ju\u00e1rez" and that the \u00e9 and \u00e1 are replacing the two previously mentioned letters. (For information about what this is, start by checking out the first half of [this page](https://docs.python.org/2/howto/unicode.html) in the documentation). To make your program work, you're going to have to handle this problem somehow.
- Create a program that pulls titles from the official Wikipedia API and then asks the user one by one if he or she would like to read about that article.
- Example:
  - If the first title is Reddit, then the program should ask something along the lines of "Would you like to read about Reddit?" If the user says yes, then the program should open up the article for the user to read.
  - HINT: Click [here](https://en.wikipedia.org/wiki?curid=39608394) to see how the article's ID can be used to access the actual article.
- Subgoals:
  - As mentioned before, do something about the possibility of unicode appearing in the title.
  - Whether you want your program to simply filter out these articles or you want to actually turn the codes into readable characters, that's up to you.
  - Make the program pause once the user has selected an article to read, and allow him or her to continue browsing different article titles once finished reading.
  - Allow the user to simply press ENTER to be asked about a new article.

##### Solutions
