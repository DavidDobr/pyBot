# This is an overview of future bot functionality

## Getting an uber

* set up Uber API, get a token

```python
location_dict =
{work: [lat, lon],
 home: [lat, lon],
grig: [lat, lon],
yandex: [lat, lon]
}

def user_choice_location():
    """
    present the user with choice from location_dict.keys
    """
    present choice
    get answer
    return location_dict(key)

def call_an_uber():
    #
    START = user_choice_location()
    END = user_choice_location()

BOT_BUTTONS =  ['FROM HOME TO WORK',
                'FROM WORK TO HOME',
                'CUSTOM']
```
### ToDo (additional functionality)
* [__essential__] show expected UberX fare in button text
* display expected fare for X, Comfort, Black
* get current location
* if close to existing location tag, choose it as start
* [__maybe__] implement custom location search from WITHIN telegram

## I'm home
* send "I'm home" message to parents
* append location
* [__maybe__] implement via an android home button

## Another Feature
