import bs4 
import requests
from splinter import Browser
import time
import lxml
start = time.time()
class SupremeBot:
	def __init__(self, **info):
		self.base_url = "http://supremenewyork.com"
		self.shop_ext = "/shop/all/"
		self.checkout = "/checkout/"
		self.info = info

	def init_browser(self):
		executable_path = {'executable_path':'#Path To Chromedriver'}
		self.b = browser('chrome', **executable_path)

	def findProduct(self):

		r = requests.get("{}{}{}".format(self.base_url, self.shop_ext, self.info["catagory"])).text


		soup = bs4.BeautifulSoup(r, 'lxml')

		temp_tuple = []
		temp_link = []

		for link in soup.findAll('a', href=True):
			temp_tuple.append([link["href"], link.text])

		for i in temp_tuple:
			if i[1] == self.info['product'] or i[1] == self.info['color']: 
				temp_link.append(i[0])

		self.final_link = (self.base_url + temp_link[1])
		print(self.final_link)


	def initializeBrowser(self):
		executable_path = {'executable_path': '#Path To Chromedriver#'}
		self.b = Browser('chrome', **executable_path)


	def visitSite(self):
		site = self.b.visit(self.final_link)

		#self.b.find_option_by_text(self.info['size']).click()
		self.b.find_by_value('add to cart').click()
		self.b.visit("{}{}".format(self.base_url, self.checkout))


	def checkoutFunc(self):

	
		self.b.fill("order[billing_name]", self.info['namefield'])
		self.b.fill("order[email]", self.info['emailfield'])		
		self.b.fill("order[tel]", self.info['phonefield'])

		self.b.fill("order[billing_address]", self.info['addressfield'])
		self.b.fill("order[billing_city]", self.info['city'])
		self.b.fill("order[billing_zip]", self.info['zip'])

		self.b.fill("carn", self.info['number'])
		self.b.select("credit_card[month]", self.info['month'])
		self.b.select("credit_card[year]", self.info['year'])
		self.b.fill("credit_card[vvv]", self.info['cvv'])
		self.b.find_by_css('.terms').click()
        #self.b.find_by_value("process payment").click()		
	def main(self):
		kdot = True
		kdot1 = True
		kdot2 = True
		while kdot == True:
			try:
				self.findProduct()
				print("Product URL found")
				kdot = False 
			except:
				print("Error Looking for product...")

		self.initializeBrowser()
		
		#while kdot1 == True:
			#try:
		self.visitSite()
		print("Visiting site")
				#kdot1 = False
			#except:
				#print("Error Visiting Site...")
		
		while kdot2 == True:
			try:
				self.checkoutFunc()
				kdot2 = False
				print("Checking out")
			except:
				print("Error Checking Out...")
		


	end = time.time()
	print(end-start)
if __name__ == "__main__":
		INFO = {
		"product": "Supreme®/Post-it® Flags",
		"color": "Red",
		"size": "",
		"catagory": "Accessories",
		"namefield": "",
		"emailfield": "",
		"phonefield": "",
		"addressfield": "",
		"city": "",
		"zip": "",
		"country": "OK",
		"card": "visa",
		"number": "",
		"month": "",
		"year": "",
		"cvv": ""
		}		
		bot = SupremeBot(**INFO)
		bot.main()



































