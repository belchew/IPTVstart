l1 = 'https://www.seir-sanduk.com/?player=1&id=hd-star-crime-hd&pass='
l2 = 'https://www.seir-sanduk.com/?player=1&id=hd-star-channel-hd&pass='
l3 = 'https://www.seir-sanduk.com/?player=1&id=hd-star-life-hd&pass='
l4 = 'https://www.gledaitv.live/watch-tv/44/kino-nova-online'
l5 = 'https://www.seir-sanduk.com/?player=1&id=hd-nova-news-hd&pass='
l6 = 'https://www.seir-sanduk.com/?player=1&id=hd-78-tv-hd&pass='
l7 = 'https://www.seir-sanduk.com/?player=1&id=hd-travel-channel-hd&pass='
l8 = 'https://www.seir-sanduk.com/?player=1&id=hd-24-kitchen-hd&pass='
l9 = 'https://www.gledaitv.live/watch-tv/4/the-voice-online'
l10 = 'https://www.gledaitv.live/watch-tv/39/planeta-folk-online'
l11 = 'https://www.gledaitv.live/watch-tv/40/planeta-hd-online'
l12 = 'https://www.gledaitv.live/watch-tv/41/city-tv-online'

import pyautogui
from time import sleep
from DrissionPage import ChromiumPage
p = ChromiumPage()
pyautogui.hotkey('ctrl', 't')
pyautogui.write('chrome-extension://hkbifmjmkohpemgdkknlbgmnpocooogp/data/interface/index.html?tab')
pyautogui.press('enter')
p.get(l1)
sleep(2)
p.get(l2)
sleep(2)
p.get(l3)
sleep(2)
p.get(l4)
sleep(2)
p.get(l5)
sleep(2)
p.get(l6)
sleep(2)
p.get(l7)
sleep(2)
p.get(l8)
sleep(2)
p.get(l9)
sleep(2)
p.get(l10)
sleep(2)
p.get(l11)
sleep(2)
p.get(l12)
pyautogui.hotkey('ctrl', 's')
sleep(1)
pyautogui.press('enter')
sleep(1)
pyautogui.press('enter')
#pyautogui.hotkey('alt', 'f4')
i = p.get_frame('@src^https://challenges.cloudfire.com/cdn-cgi')
e = i('.mark')
sleep(3)
e.click()