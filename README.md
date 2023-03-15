# AI_Video_Maker
A program that makes videos from Reddit automatically

I have written code that:

1) Gets some text from Reddit (You need to specify which subreddit)

2) Turns it to TTS (Text-To-Speech)

3) Uses the TTS, a looping background, a transition and an outro (which all need to be specified) in order to render a video.


Current Problems:

- The way the program "guesses" when to transition to the next block of text is done in a stupid way.
It transitions every 60 seconds (1 minute) and shows to the screen at most 150 words!

- It takes too long to render.

Thank you for reading!!
