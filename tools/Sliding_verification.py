#Pillow
from PIL import Image, ImageEnhance
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
#opencv-python
import cv2
import numpy as np
from io import BytesIO
import time
import requests



class CrackSlider():
    """
    通过浏览器截图，识别验证码中缺口位置，获取需要滑动距离，并模仿人类行为破解滑动验证码
    """

    def __init__(self):

        # 实际地址
        self.url = 'https://buff.163.com/account/login?back_url=/user-center/asset/%3F'
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        self.zoom = 1

    def open(self):
        self.driver.get(self.url)

    def get_pic(self):
        time.sleep(2)
        target = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_bg-img')))
        template = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'yidun_jigsaw')))
        target_link = target.get_attribute('src')
        template_link = template.get_attribute('src')
        target_img = Image.open(BytesIO(requests.get(target_link).content))
        template_img = Image.open(BytesIO(requests.get(template_link).content))
        target_img.save('target.jpg')
        template_img.save('template.png')
        size_orign = target.size
        local_img = Image.open('target.jpg')
        size_loc = local_img.size
        self.zoom = 320 / int(size_loc[0])

    def get_tracks(self, distance):
        print(distance)
        #距离
        distance += 20
        v = 0
        t = 0.2
        #前进轨迹
        forward_tracks = []
        #现在
        current = 0
        mid = distance * 3 / 5
        while current < distance:
            if current < mid:
                a = 2
            else:
                a = -3
            s = v * t + 0.5 * a * (t ** 2)
            v = v + a * t
            current += s
            forward_tracks.append(round(s))

        back_tracks = [-3, -3, -2, -2, -2, -2, -2, -1, -1, -1]
        return {'forward_tracks': forward_tracks, 'back_tracks': back_tracks}

    def match(self, target, template):
        img_rgb = cv2.imread(target)
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(template, 0)
        run = 1
        w, h = template.shape[::-1]
        print(w, h)
        res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

        # 使用二分法查找阈值的精确值
        L = 0
        R = 1
        while run < 20:
            run += 1
            threshold = (R + L) / 2
            print(threshold)
            if threshold < 0:
                print('Error')
                return None
            loc = np.where(res >= threshold)
            print(len(loc[1]))
            if len(loc[1]) > 1:
                L += (R - L) / 2
            elif len(loc[1]) == 1:
                print('目标区域起点x坐标为：%d' % loc[1][0])
                break
            elif len(loc[1]) < 1:
                R -= (R - L) / 2

        return loc[1][0]

    def crack_slider(self):
        self.open()
        time.sleep(1)
        self.driver.switch_to.frame(self.driver.find_element_by_xpath("//div[@id='j_login_page']/iframe"))
        time.sleep(0.5)
        self.driver.find_element_by_class_name("tab0").click()
        time.sleep(0.5)
        self.driver.find_element_by_id("phoneipt").send_keys("17671434829")
        time.sleep(0.5)
        self.driver.find_element_by_xpath("//input[@autocomplete='new-password']").send_keys("1996.fsw")
        target = 'target.jpg'
        template = 'template.png'
        self.get_pic()
        distance = self.match(target, template)
        tracks = self.get_tracks((distance +2) * self.zoom)  # 对位移的缩放计算
        print(tracks)
        slider = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'yidun_slider')))
        ActionChains(self.driver).click_and_hold(slider).perform()

        for track in tracks['forward_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=track, yoffset=0).perform()
        time.sleep(0.5)
        for back_tracks in tracks['back_tracks']:
            ActionChains(self.driver).move_by_offset(xoffset=back_tracks, yoffset=0).perform()
        #一步滑到
        # ActionChains(self.driver).move_by_offset(xoffset=distance, yoffset=0).perform()

        ActionChains(self.driver).move_by_offset(xoffset=-3, yoffset=0).perform()
        ActionChains(self.driver).move_by_offset(xoffset=3, yoffset=0).perform()
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()
        try:
            failure = self.wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, 'yidun_tips__text'), '向右滑动滑块填充拼图'))
            print(failure)
        except:
            print('验证成功')
            time.sleep(1)
            self.driver.find_element_by_id("submitBtn").click()
            time.sleep(1)
            cookies = self.driver.get_cookies()
            cookies = "; ".join([i["name"] + '=' + i["value"] for i in cookies]) + "; "
            print(cookies)
            return cookies

        if failure:
            self.crack_slider()


if __name__ == '__main__':
    c = CrackSlider()
    cook = c.crack_slider()
    headers = {
        'Cookie': cook,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
    }
    ret = requests.get("https://buff.163.com/api/market/goods/sell_order?game=dota2&goods_id=2730&page_num=1&sort_by=default&mode=&allow_tradable_cooldown=1&_=1566829202589",headers=headers)
    c.driver.quit()
    print()
