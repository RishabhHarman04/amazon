from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
print("test case started")

driver.maximize_window()
driver.get("https://www.amazon.in/?&ext_vrnc=hi&tag=googhydrabk1-21&ref=pd_sl_5j0bx521tf_e&adgrpid=61665929249&hvpone=&hvptwo=&hvadid=486445347800&hvpos=&hvnetw=g&hvrand=15401016297275157187&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007786&hvtargid=kwd-298441375321&hydadcr=5621_2175698&gclid=EAIaIQobChMIncyTxOLt9gIVwg5yCh2YVgYDEAAYASAAEgKccfD_BwE")
time.sleep(1)
driver.find_element_by_name("field-keywords").send_keys("samsung s22")
time.sleep(1)
driver.find_element_by_id("nav-search-submit-button").click()
time.sleep(5)
driver.close()
print("test case has successfully completed")