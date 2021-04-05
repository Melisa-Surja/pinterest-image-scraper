# Pinterest Image Scraper
Download all relevant images under a pin. 

It uses Firefox browser as default option. Please edit as necessary to use other browsers.

## Why This Script?
This modification is to update the original script as it's quite outdated, and to batch-download multiple links at once.

It will also create downloaded.txt in the download directory to prevent the script from downloading the same image more than once.

It also adds progress bars and other status updates while it's downloading, so you'd know that it's working.

## How to Run:
1. Please follow the instructions to install the scraper from [here](https://github.com/xjdeng/pinterest-image-scraper)
1. Edit `config_sample.py` with your information, then rename it to `config.py`
1. Run the script with this command:
```python
python my_scraper.py
```