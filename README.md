# DogFacts-API

DogFacts-API is an API that gives you facts about dogs that you can use in your project! Maintained by @SwiftyProgrammer on GitHub + pycharm! Open-Source contributions welcome!

# What you need

You need:
1. Python
2. `urllib.request`
3. `json`

# Usage

| Route           | What it does                     |
|-----------------|----------------------------------|
| `/`             | Gets dog facts                   |
| `/reasons`      | Get reasons to get a dog         |
| `/fun/coinflip` | Gets a random `heads` or `tails` |
| `/fun/diceroll` | Get a dice roll result           |
| `/dog_zen`      | Parker the dog gives you wisdom  |
| `/emoji`        | IN BETA TESTING                  |

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
Route `/emoji` is being tested

New features going to be added soon!

# Inspiration

Inspired by meowfacts project made by wh-iterabb-it / meowfacts
Link: https://github.com/wh-iterabb-it/meowfacts

# Licence

Released under [MIT](/LICENSE) by [@SwiftyProgrammer690](https://github.com/SwiftyProgrammer690).
