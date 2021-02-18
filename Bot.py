#Arafat Iqbal
#January, 2021
#For Educational Purposes Only

from selenium import webdriver
from info import fill
from selenium.webdriver.support.ui import Select
import time


def Unemployment_Fill():

	#Make Window Full Screen
	driver.maximize_window()

	#Checkout item from the URL
	driver.find_element_by_xpath('//*[@id="secondary"]/div/table/tbody/tr[2]/td/div/form/center/font/input').click()
	#time.sleep(1)
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/center/font/input').click()
	#time.sleep(1)
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/center/font/input').click()
	#time.sleep(1)

	#Fill in Information
	driver.find_element_by_xpath('//*[@id="ssn"]').send_keys(fill['social'])
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[2]/td/center/font[2]/input').click()
	driver.find_element_by_xpath('/html/body/dir/dir/div/div/table/tbody/tr[2]/td/table/tbody/tr[2]/td/form/div/input[1]').send_keys(fill['num'])
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/div/input[2]').click()
	#Claim the Benefits
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[4]/td[2]/label[2]/input').click() #1
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[5]/td[2]/label[2]/input').click() #2
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[6]/td[2]/label[2]/input').click() #3
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[7]/td[2]/label[2]/input').click() #4
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[8]/td[2]/label[1]/input').click() #5
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[9]/td[2]/label[1]/input').click() #6
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[10]/td[2]/label[1]/input').click() #7
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[11]/td[2]/label[1]/input').click() #8

	driver.find_element_by_xpath('//*[@id="Q4a"]').send_keys(fill['hours'])
	driver.find_element_by_xpath('//*[@id="Q4b"]').send_keys(fill['money'])

	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[14]/td/table/tbody/tr[10]/td/table/tbody/tr[2]/td[1]/input').click()
	driver.find_element_by_xpath('//*[@id="CFForm_1"]/table/tbody/tr[15]/td/input').click()

if __name__ == '__main__':

	PATH = "S:\Old Desktop\Projects\chromedriver.exe"
	driver = webdriver.Chrome(PATH)

	driver.get(fill['url'])
	Unemployment_Fill()
