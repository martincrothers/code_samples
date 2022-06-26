# This project is not yet fully completed, but is functional

# Password Generator in Python
This project is a password generator in the theme of the XKCD comic [Password Strength](https://xkcd.com/936/)

There could be offensive words in the dictionary (word list) referenced by the application.  I simply grabbed a word list from the internet. I deleted the offensive words I could think of, though I'm certain that wasn't thorough enough. Be forewarned this may generate an offensive word or phrase.

This requires a non-standard library: [termcolor](https://pypi.org/project/termcolor/){:target="\_blank"}, as the console output is printed with color to make readability easier for the user running the program.

This application will prompt you for:
- The minimum number of words you want in your passphrase,
- The minimum charater count,
- What character you want to place between words,
- If you want each word captalized,
- If you want a number appended to the end of the phrase.