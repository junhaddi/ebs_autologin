from selenium import webdriver
import os
import datetime

# Chrome Headless 옵션
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--disable-gpu')

# Chrome 웹 드라이버 생성
# driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=chrome_options)
driver = webdriver.Chrome(executable_path='C://chromedriver.exe', chrome_options=chrome_options)
driver.implicitly_wait(100)
print('웹 드라이버 생성')

# url 로딩
driver.get('https://oc.ebssw.kr')
print('url 로딩')

# 고등학교 온라인 클래스 입장
driver.find_element_by_xpath(
    '//a[@href="http://hoc.ebssw.kr/onlineClass/reqst/onlineClassReqstInfoView.do?schCssTyp=online_high"]').click()
print('고등학교 온라인 클래스 입장')

# EBS 로그인 페이지 이동
ebsLoginPage = driver.find_element_by_xpath('//a[@href="/sso/loginView.do?loginType=onlineClass"]')
driver.execute_script('arguments[0].click();', ebsLoginPage)
print('EBS 로그인 페이지 이동')

# 카카오 로그인 페이지 이동
kakaoLoginPage = driver.find_element_by_xpath('//a[@href="javascript:doSnsLogin(\'kakao\');"]')
driver.execute_script('arguments[0].click();', kakaoLoginPage)
print('카카오 로그인 페이지 이동')

# 카카오 계정 로그인
id = ''
pw = ''
driver.find_element_by_id('id_email_2').send_keys(id)
driver.find_element_by_id('id_password_3').send_keys(pw)
driver.find_elements_by_xpath('//button')[5].click()
print('카카오 계정 로그인')

# 3-5반 클래스 이동
driver.find_element_by_xpath('//a[@href="https://hoc22.ebssw.kr/sunrin305"]').click()
print('3-5반 클래스 이동')

# 텝 이동
last_tab = driver.window_handles[-1]
driver.switch_to.window(window_name=last_tab)
print('텝 이동')

# 일일 출결 페이지 이동
driver.find_element_by_xpath(
    '//a[@href="/sunrin305/hmpg/hmpgBbsListView.do?menuSn=402937&bbsId=BBSID_000393499"]').click()
print('일일 출결 페이지 이동')

# 출석체크 계시글 이동
dt = datetime.datetime.now()
# nowDate = str(dt.month) + '/' + str(dt.day) + ' 출석체크'
nowDate = '4/10(금) 출석체크'

table = driver.find_elements_by_tag_name('tbody')
for i in table:
    # register = print(i.find_element_by_xpath('//td[@class="wdate"]').text)
    title = i.find_element_by_xpath('//td[@class="tit tl"]').text
    if title == nowDate:
        # i.find_element_by_xpath('//a[@class="class_nm_ellipsis"]').click()
        post = i.find_element_by_xpath('//a[@class="class_nm_ellipsis"]')
        driver.execute_script('arguments[0].click();', post)
        print(title + ' 페이지 이동')

# 댓글 작성
message = '출석체크'
driver.find_element_by_xpath('//textarea[@name="cmmntsCn"]').send_keys(message)
driver.find_element_by_xpath('//a[@class="submit"]').click()
alert = driver.switch_to.alert
alert.accept()
print('댓글 작성')

# 종료
driver.quit()
