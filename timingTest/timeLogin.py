from playwright.sync_api import Page, sync_playwright
import random 
import string
import numpy as np

## GLOBALS
allowed_chars = string.ascii_lowercase + " "
css_selector = "input[aria-label=Password]"

def check_password(psw) -> str:

    box.fill(psw)
    box.press('Enter')
    return page.locator(".stAlert").inner_text()

def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_viewport_size({"width": 640, "height": 480})
    page.goto("http://localhost:8501")
    box = page.locator(css_selector)
    
    pswds = ["bad","bad2","thepass"]
    for psw in pswds:
        print(psw, check_password(psw))
    

# def crack_length(user, max_len=32, verbose=False) -> int:
#     trials = 2000
#     times = np.empty(max_len)
#     for i in range(max_len):
#         i_time = timeit.repeat(stmt='check_password(user, x)',
#                                setup=f'user={user!r};x=random_str({i!r})',
#                                globals=globals(),
#                                number=trials,
#                                repeat=10)
#         times[i] = min(i_time)

#     if verbose:
#         most_likely_n = np.argsort(times)[::-1][:5]
#         print(most_likely_n, times[most_likely_n] / times[most_likely_n[0]])

#     most_likely = int(np.argmax(times))
#     return most_likely

