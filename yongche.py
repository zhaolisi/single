#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
driver=webdriver.Chrome()
#driver=webdriver.Firefox()
#driver.maximize_window()

driver.get('https://sso.yongche.org')
driver.set_window_size(1920,1080)
try:
    #向文本框发送内容
    driver.find_element_by_id('J_login').send_keys('zhaolisi')
    time.sleep(1)#强制等待：不管浏览器是否加载完了，程序都得等待1秒，1秒一到，继续执行下面的代码
    driver.find_element_by_id('J_pwd').send_keys('Zls@8891')
    time.sleep(1)
    driver.find_element_by_id('id_submit').click()
    time.sleep(1)
    driver.find_element_by_link_text('首页').click()
    time.sleep(1)
    # 获取当前窗口句柄
    currentwinfirstpage = driver.current_window_handle
    driver.find_element_by_xpath("//*[contains(text(),'ERP')]").click()
    driver.implicitly_wait(10)#隐形等待：设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步
    #获取所有窗口句柄
    handles=driver.window_handles
    for handle in handles:
        if handle !=currentwinfirstpage:
            driver.switch_to.window(handle)
    # 跳转页面后，如果页面含有frame,需要定位到相应的frame，才能够定位元素
    driver.switch_to.frame("content")
    driver.find_element_by_id("cellphone").send_keys("16801015609")
    driver.find_element_by_id("cellphone_search").click()
    #页面刷新后，需要等待,显性等待
    locator=(By.ID,'btn_create')
    WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located(locator))
    # 定位到滚动条要拉动打元素位置，拉动滚动条
    target = driver.find_element_by_id("btn_create")
    driver.execute_script("arguments[0].scrollIntoView();",target)
    target.click()
    #点选radiobutton
    time.sleep(1)
    radioselected=driver.find_element_by_id("use_type_17")
    if radioselected.is_selected():
        print ("none")
    else:
        radioselected.click()
    time.sleep(1)
    driver.find_element_by_name("start_position").click()
    driver.find_element_by_xpath("//*[contains(text(),'中谷酒店')]").click()
    time.sleep(1)
    driver.find_element_by_name("end_position").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*/div[@id='end_addrlist']/li/a[contains(text(),'北京西站')]").click()
    time.sleep(1)

    target1 = driver.find_element_by_xpath("//*/input[@type='submit']")
    driver.execute_script("arguments[0].scrollIntoView();", target1)

    driver.find_element_by_id("car_type").click()
    driver.find_element_by_xpath("//*/option[@value='37']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*/select[@name='corporate_id']").click()
    driver.find_element_by_xpath("//*/option[@value='0']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*/span[@id='self-use']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*/input[@name='passenger_phone']").click()
    time.sleep(1)
    is_auto_dispatch=driver.find_element_by_xpath("//*/input[@id='is_auto_0']")
    if is_auto_dispatch.is_selected():
        print ("none")
    else:
        is_auto_dispatch.click()
    time.sleep(1)
    send_message_to_passenger=driver.find_element_by_xpath("//*/input[@name='passenger']")
    if send_message_to_passenger.is_selected():
        send_message_to_passenger.click()
    else:
        print ("none")
    time.sleep(1)
    driver.find_element_by_xpath("//*/input[@type='submit']").click()
    time.sleep(1)

    target2= driver.find_element_by_xpath("//*/input[@id='driverCPhoneNumber']")
    driver.execute_script("arguments[0].scrollIntoView();", target2)
    target2.send_keys("16810003000")

    driver.find_element_by_xpath("//*/input[@id='selectCarButton']").click()
    time.sleep(1)
    try:
        if driver.find_element_by_xpath("//*/input[@value='确定使用']").is_displayed():
            driver.find_element_by_xpath("//*/input[@value='确定使用']").click()
        else:
            print ("No driver find")
            driver.get_screenshot_as_file("/Users/zhaolisi/PycharmProjects/test/ScreenShots")#截图保存
    except Exception as e:
        print ('Exception found',format(e))
    time.sleep(1)
    driver.find_element_by_xpath("//*/input[@value='取消订单']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*/option[@value='12']").click()
    time.sleep(1)
    driver.find_element_by_id("J_cancel_submit").click()
    time.sleep(1)
    driver.switch_to.alert.accept()
    time.sleep(2)
except Exception as e:
    print ('Exception found',format(e))
driver.quit()


