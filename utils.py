import requests
import os

cookies = {"session": os.getenv("AOC_SESSION")}


def get_input(day: int):
    res = requests.get(
        f"https://adventofcode.com/2021/day/{day}/input", cookies=cookies
    )
    return res.text
