from pinterest_scraper import scraper as s
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import os
import requests
import config
from tqdm.auto import tqdm
try:
    from urlparse import urlparse
except ImportError:
    from six.moves.urllib.parse import urlparse
# import sys

def download_images(myinputs, mydir = "./"):
    for myinput in tqdm(myinputs):
        #http://automatetheboringstuff.com/chapter11/
        res = requests.get(myinput)
        res.raise_for_status()
        #https://stackoverflow.com/questions/18727347/how-to-extract-a-filename-from-a-url-append-a-word-to-it
        outfile = mydir + "/" + os.path.basename(urlparse(myinput).path)
        playFile = open(outfile, 'wb')
        for chunk in res.iter_content(100000):
            playFile.write(chunk)
        playFile.close()

def download_all_links(download_urls, download_dir, ph, loop=5):
    for download_url in download_urls:
        print(f"Fetching images from {download_url}...")

        # collect a list of img urls
        images = ph.runme(download_url.strip())
        images = [img.decode('utf-8') for img in images] # convert from byte to str

        # only download images that haven't been downloaded yet
        if not os.path.exists(download_dir + '/downloaded.txt'):
            f = open(download_dir + '/downloaded.txt', "w")
            f.close()

        with open(download_dir + '/downloaded.txt', "r") as f:
            downloaded_images = f.read().split('\n')
        images = list(filter(lambda img: img not in downloaded_images, images))

        print(f"{len(images)} images ready to be downloaded.")

        if (len(images) > 0):
            # save all imgs in the folder
            download_images(images, download_dir)

            # append the results in txt - one line one url
            with open(download_dir + '/downloaded.txt', "a") as f:
                f.write('\n' + '\n'.join(images))

        print(f"Successfully downloaded {len(images)} images!")
        print("-"*40)

    # Close browser when finished?
    ph.close()


if __name__ == "__main__":
    # Setup config
    options = Options()
    options.binary_location = config.firefox_exe
    profile = webdriver.FirefoxProfile()
    profile.set_preference("permissions.default.image", 2)
    browser = webdriver.Firefox(options=options, firefox_profile=profile, executable_path=config.webdriver_path)
    ph = s.Pinterest_Helper(config.pinterest_login , config.pinterest_pass, browser=browser)

    # Download now
    links = config.download_links.strip().split('\n')
    download_all_links(download_urls=links, download_dir=config.download_dir, ph=ph)

