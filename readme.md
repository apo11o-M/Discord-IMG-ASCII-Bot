# Discord IMG Enhancer Bot
---
## What is this?
Discord IMG-ASCII bot is a small discord bot written using Discord API and python that can take a command from the user, convert the image into a text output in the chat that resembles the input image using characters from the ASCII table.

## How does it work?
This bot is quite simple on how it works, here's the basic idea & concepts.
- Have an event handler that actively listens to chat to see whether the user type in the command prefix "!"
- When the event is triggered, grab the input image link, and convert it to an 2D array of ASCII characters using another script.
- return the 2D array, and construct a string with the contents in the 2D array.
- send the String as a message to the chat.

## Some Difficulties I Encountered
- The font that discord uses have the letters and characters in different width, so simply using the characters would misalign the results.
- How to bypass the markdown formats, since slashes and asterisks would accidently format our text, we want either a way to not apply markdown or simply use other characters that would not trigger the effects.
