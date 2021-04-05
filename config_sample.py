# Pinterest login info
pinterest_login = "your_email@gmail.com"
pinterest_pass = "your_password"

# Must be absolute path, relative paths don't work.
# Do not remove the "r" in the beginning, it's for string literals.
firefox_exe = r"C:/Users/USERNAME/AppData/Local/Mozilla Firefox/firefox.exe"
download_dir = r"D:/pinterest"
webdriver_path = r"D:/webdriver/geckodriver.exe"

# Put all the pin links to be downloaded here, separated by linebreaks
# Try not to download more than 5 links at once, because each link will download more than 100 images.
# The examples are BTS' photo pins
download_links = """
https://www.pinterest.com/pin/233272455688668240/
https://www.pinterest.com/pin/764626842975561105/
https://www.pinterest.com/pin/843721311438265790/
https://www.pinterest.com/pin/764626842975561105/
"""