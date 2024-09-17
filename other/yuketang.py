# To accomplish the online course,I write these coding.


import time
import webbrowser
import pyautogui
import webbrowser

# Read URLs from the file
urls = [
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082485",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082486",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082487",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082488",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082489",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082490",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082491",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082492",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082493",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082494",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082495",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082496",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082497",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082498",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082499",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082500",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082501",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082502",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082503",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082504",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082505",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082506",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082507",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082508",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082509",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082510",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082511",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082512",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082513",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082514",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082515",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082516",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082517",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082518",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082519",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082520",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082521",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082522",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082523",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082524",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082525",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082526",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082527",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082528",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082529",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082530",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082531",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082532",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082533",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082534",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082535",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082536",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082537",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082538",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082539",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082540",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082541",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082542",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082543",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082544",
    "https://nwu.yuketang.cn/pro/lms/BZ5jVPfsBHp/23296954/video/52082545",
]

# Function to open URLs in order
def open_urls():
    for url in urls:
        # print(url)
        # Open the URL in the default web browser
        webbrowser.open(url)
        # Wait for a moment to ensure the page loads
        time.sleep(5)
        
        # Move the mouse to the center of the screen and click
        screen_width, screen_height = pyautogui.size()
        pyautogui.moveTo(screen_width / 2, screen_height / 2, duration=1)
        time.sleep(3)  # Wait for 3 seconds before clicking
        pyautogui.click()

        # Move the mouse to (853, 644) after 10 seconds
        time.sleep(10)
        pyautogui.moveTo(853, 644, duration=1)

        # Move the mouse to (853, 467) after 5 seconds
        time.sleep(5)
        pyautogui.moveTo(853, 467, duration=1)

        # Wait for 20 minutes before opening the next URL
        time.sleep(1200)

if __name__ == "__main__":
    open_urls()
