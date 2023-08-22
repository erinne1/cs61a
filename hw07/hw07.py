import re


def match_time(text):
    """
    >>> match_time("At 07:23AM, I woke up and had some coffee.")
    True
    >>> match_time("I looked at my phone at 12:22 to check the weather.")
    True
    >>> match_time("At 05:24PM, I had sesame bagels with cream cheese.")
    True
    >>> match_time("At 23:59 I was sound asleep.")
    True
    >>> match_time("After, the clocked turned to 00:00.")
    True
    >>> match_time("Mix water in a 1:2 ratio with chicken stock.")
    False
    >>> match_time("At work, I pinged 127.0.0.1:80.")
    False
    >>> match_time("The tennis score was 40:30.")
    False
    """
    return bool(re.search("(([0-1][0-9])|([2][0-3]))[\:][0-5][0-9]" , text))


# military hours: first digit: 0 OK
#01, 19, 23 (is max) 

#normal hours: first digit: 

