# 'Marvel'lous PLAY

## Do you know this Marvel comic character?

The main aim of this project/Game is to learn about APIs get, comfortable with retrieving data from APIs and authenticating ourselves using an API key

[Marvel API](https://developer.marvel.com/) is a super fun API to play with Marvel characters, series, movies and of course Marvel comics

By understanding the code and forking it, you can learn about

- [Rest APIs](https://www.freecodecamp.org/news/how-to-use-rest-api/), python [requests module](https://pypi.org/project/requests/)
- [tkinter](https://docs.python.org/3/library/tkinter.html) module to create GUI using python
- Python [classes, objects and functions](https://docs.python.org/3/tutorial/classes.html)

In the code, I retrieved marvel characters and their images using the requests module and populated the full dictionary which in turn I used to develop the game

You can get your own api key from [Marvel API](https://developer.marvel.com/) and populate keys.py file with key and hash to retrive your own data from API

please follow the below authentication process for the key and its relevant md5 hash:

Authentication for Server-Side Applications
Server-side applications must pass two parameters in addition to the apikey parameter:

 - ts - a timestamp (or other long string which can change on a request-by-request basis)

   **you can use ts = 1**
   
 - hash - a md5 digest of the ts parameter, your private key and your public key (e.g. md5(ts+privateKey+publicKey)

   Generate md5 hash [here](https://www.md5.cz/) by placing ts+privateKey+publicKey in the input field

For example, a user with a public key of "1234" and a private key of "abcd" could construct a valid call as follows: 

http://gateway.marvel.com/v1/public/comics?ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150

(The hash value is the md5 digest of **1abcd1234**)

**Contributing**

Please follow the code of conduct when contributing to this project.
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

**Author**    

Herald

**License**

This project is licensed under the MIT License - see the LICENSE file for details

**Acknowledgments**

Thank you to the **Marvel API** for providing character data

Thank you to the **John Capobianco** for introducing Marvel API to me


Last but not least **HAVE FUN** and **FEEL FREE TO FORK THE CODE** to develop your own application