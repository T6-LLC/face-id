from selenium import webdriver
from retinaface import RetinaFace
from deepface import DeepFace
import matplotlib.pyplot as pp
import glob
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(
    r"C:\Users\Matthew.Jurewicz\Downloads\chromedriver_win32\chromedriver.exe")
driver.get('https://www.google.com/search?q=matthew+jurewicz&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj689zh75n4AhWKmYQIHSXDBZsQ_AUoAnoECAEQBA&biw=1280&bih=649&dpr=1.5')
elem = driver.find_element_by_tag_name('body')
im = None
while driver.get_screenshot_as_base64() != im:
    im = driver.get_screenshot_as_base64()
    driver.save_screenshot('im.png')
    for x in RetinaFace.extract_faces('im.png', align=False):
        out = DeepFace.verify(x, 'test.jpg', enforce_detection=False)
        if out['verified']:
            pp.imsave(
                'Match' + str(len(glob.glob('Match*.png')) + 1) + '.png',
                x
            )
    elem.send_keys(Keys.PAGE_DOWN)