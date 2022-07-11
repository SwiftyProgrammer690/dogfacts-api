# DogFacts-API

DogFacts-API is an API that gives you facts about dogs that you can use in your project! Maintained by @SwiftyProgrammer on GitHub + pycharm! Open-Source contributions welcome!

# What you need

You need:
1. Python
2. `urllib.request`
3. `json`

# Usage

| Route                               | What it does                                                                                                                   |
|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| `/`                                 | Gets dog facts                                                                                                                 |
| `/reasons`                          | Get reasons to get a dog                                                                                                       |
| `/fun/coinflip`                     | Gets a random `heads` or `tails`                                                                                               |
| `/fun/diceroll`                     | Get a dice roll result                                                                                                         |
| `/dog_zen`                          | Parker the dog gives you wisdom                                                                                                |
| `/emoji`                            | Gets random dog emoji *TO SEARCH, LOOK AT ROUTE* `/search_emoji`                                                               |
| `/search_emoji/?emoji=<EMOJI_NAME>` | Searches for specific emoji. Emoji names = `Dog`, `DogFace`, and `PoodleDog`. Will return 404 error if invalid input received! |

For route `/`:
```
import urllib.request, json

# Get data from the api route "/"
def get_fact():
    url = "https://api-dogfacts.herokuapp.com/"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```
For route `/reasons`:
```
import urllib.request, json

# Get data from the api route "/reasons"
def get_reason():
    url = "https://api-dogfacts.herokuapp.com/reasons"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```
For route `/fun/coinflip`:
```
import urllib.request, json

# Get data from the api route "/fun/coinflip"
def get_flip():
    url = "https://api-dogfacts.herokuapp.com/fun/coinflip"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```
For route `/fun/diceroll`:
```
import urllib.request, json

# Get data from the api route "/fun/rolldice"
def get_dice():
    url = "https://api-dogfacts.herokuapp.com/fun/rolldice"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```
For route `/dog_zen`:
```
import urllib.request, json

# Get data from the api route "/dog_zen"
def get_quote():
    url = "https://api-dogfacts.herokuapp.com/dog_zen"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```
For Route `/emoji`:
```
import urllib.request, json

# Get data from the api route "/emoji"
def get_emoji():
    url = "https://api-dogfacts.herokuapp.com/emoji"
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```
For Route `/search_emoji/`:
```
import urllib.request, json

# Get data from the api route "/search_emoji"
def get_emoji(EMOJI_NAME):
    url = "https://api-dogfacts.herokuapp.com/search_emoji/?emoji=" + EMOJI_NAME
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read().decode()
    return data
```

New features going to be added soon!

# Help

If you are facing any difficulties with this api, please feel free to open an issue on GitHub!

# Inspiration

Inspired by meowfacts project made by wh-iterabb-it / meowfacts
Link: https://github.com/wh-iterabb-it/meowfacts

# Licence

Released under [MIT](/LICENSE) by [@SwiftyProgrammer690](https://github.com/SwiftyProgrammer690).
