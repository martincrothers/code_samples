# Password Generator in Python
This project is a password generator in the theme of the XKCD comic [Password Strength](https://xkcd.com/936/)

## Completion Level: Good Enough for Initial Publishing
This project is not yet fully completed, but is functional. It still requires some PEP compliances, additional error handling, updating function comments, and other such cleanup. It does work though in all the scenarios I tested it for.

## Notes
### Offensive Words Possible
There could be offensive words in the dictionary (word list) referenced by the application.  I simply grabbed a word list from the internet. I deleted the offensive words I could think of, though I'm certain that wasn't thorough enough. Be forewarned this may generate an offensive word or phrase.

### Requires Non-Standard Library Package
This requires a non-standard library package: [termcolor](https://pypi.org/project/termcolor/), as the console output is printed with color to make readability easier for the user running the program.

### How it works
- This is a terminal application.
- IT will prompt you for:
    - The minimum charater count you want in your passphrase,
    - The minimum number of words,
    - What character you want to place between words,
    - If you want the first letter of each word captalized or not,
    - If you want a number appended to the end of the phrase or not.

After it creates a passphrase matching your specification, it prints it.