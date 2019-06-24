from selenium import webdriver
import time
import Config
import zipcodes
from random import randint
from faker import Faker
fake = Faker()

from selenium.webdriver.firefox.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import NoSuchElementException

from selenium.webdriver.common.keys import Keys
logins = []
# Import Config for your username and password
user = Config.DATACOUP_USERNAME
psw = Config.DATACOUP_PASSWORD
url = r'https://www.pof.com/register.aspx?id=1'

profile = webdriver.FirefoxProfile()      
desired_capabilities = webdriver.DesiredCapabilities.FIREFOX

PAC_PROXY = {
    'proxyAutoconfigUrl': 'https://whalesapp.fun/foxy.PAC',
}

pd = webdriver.Firefox(firefox_profile=profile, desired_capabilities=desired_capabilities)


# code must be in a while loop with a try to keep trying with different proxies
running = True



pd.get(url)

time.sleep(0.1)
name = fake.name()
first = name.split(' ')[0]
last = name.split(' ')[1]
textnows = []
index = str(randint(0, 500))
i = str(randint(0, 500))
p = fake.color_name()+index
u = (name.split(' ')[0]+name.split(' ')[1]+index).replace(".","")
e = first+last+'+' + index + '@gmail.com'
z = str(randint(0, 9))
y = str(randint(0, 9))
length = len(zipcodes.similar_to(y+z))
random = (randint(0, length))
zipIn = zipcodes.similar_to(y+z)[random]['zip_code']
cityIn = zipcodes.similar_to(y+z)[random]['city']
stateIn = zipcodes.similar_to(y+z)[random]['state']
prof = " ".join(fake.words(nb=3, ext_word_list=None, unique=True))
para = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
para2 = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
para3 = fake.paragraph(nb_sentences=5, variable_nb_sentences=True, ext_word_list=None)
description2 = (para + '\n\n' + para2 + '\n\n' + para3)
interests2 = ",".join(fake.words(nb=6, ext_word_list=None, unique=True))
interests = '"' + interests2 + '"'
headline2 = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
textnows.append('\n' + first+',' + last + ','+u+',' + p + ','+ e + ',' + prof + ',' + zipIn + ',' + cityIn + ',' + stateIn + ',902,' + headline2 + ',' + interests + ',' + description2)
with open('exampletextnow.csv', 'a') as f:
    for item in textnows:
        f.write("%s   " % item)
username = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[1]/td[2]/input[3]')

Password = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[2]/td[2]/input')

PasswordConfirm = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[3]/td[2]/input')
Email = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[4]/td[2]/input')
keyval = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[5]/td[2]/input')
birthmonth = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[7]/td[2]/select[1]')
birthday = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[7]/td[2]/select[2]')
birthyear = pd.find_element_by_xpath('//*[@id="blue-box-fluid-round"]/center/table/tbody/tr[7]/td[2]/select[3]')
country = pd.find_element_by_xpath('//*[@id="country"]')

submitbutton = pd.find_element_by_xpath('//*[@id="submit-button"]')
username.send_keys(u)
logins.append(u + ',' + e + ',' + p)
#self.config.username='curlyjare_' + i
with open('logins.txt', 'a') as f:
    for item in logins:
        f.write("%s\n" % item)
time.sleep(0.1)
Password.send_keys(p)
time.sleep(0.1)
PasswordConfirm.send_keys(p)
time.sleep(0.1)
Email.send_keys(e)
time.sleep(0.1)
keyval.send_keys(e)
time.sleep(0.1)
birthmonth.send_keys(Keys.DOWN)
time.sleep(0.1)
birthday.send_keys(Keys.DOWN)
time.sleep(0.1)
birthyear.send_keys(Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN, Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN, Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN, Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN,Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN )

time.sleep(2)
country.send_keys(Keys.DOWN)

time.sleep(5)
submitbutton.click()
time.sleep(120) 

postalcode = pd.find_element_by_xpath('//*[@id="postalcode"]')
postalcode.send_keys(zipIn)
city = pd.find_element_by_xpath('//*[@id="city"]')
city.send_keys(cityIn)
height = pd.find_element_by_xpath('//*[@id="height"]')
height.send_keys(Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN, Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN, Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN, Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN,Keys.DOWN, Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN , Keys.DOWN )

searchtype = pd.find_element_by_xpath('//*[@id="searchtype"]')
searchtype.send_keys(Keys.DOWN, Keys.DOWN )

eyes_id = pd.find_element_by_xpath('//*[@id="eyes_id"]')
eyes_id.send_keys(Keys.DOWN, Keys.DOWN )
state = pd.find_element_by_xpath('//*[@id="state"]')
state.send_keys(stateIn)
maritalstatus = pd.find_element_by_xpath('//*[@id="maritalstatus"]')
maritalstatus.send_keys(Keys.DOWN )
haschildren = pd.find_element_by_xpath('//*[@id="haschildren"]')
haschildren.send_keys(Keys.DOWN ,Keys.DOWN)
two = pd.find_element_by_xpath('//*[@id="form1"]/div[1]/center/table/tbody/tr[7]/td[5]/span/select')

two.send_keys(Keys.DOWN ,Keys.DOWN)
drugs = pd.find_element_by_xpath('//*[@id="drugs"]')

drugs.send_keys(Keys.DOWN ,Keys.DOWN)
fishtype = pd.find_element_by_xpath('//*[@id="fishtype"]')

fishtype.send_keys(Keys.DOWN)
politics_id = pd.find_element_by_xpath('//*[@id="politics_id"]')

politics_id.send_keys(Keys.DOWN ,Keys.DOWN,Keys.DOWN ,Keys.DOWN)
intent = pd.find_element_by_xpath('//*[@id="intent"]')
intent.send_keys(Keys.DOWN ,Keys.DOWN,Keys.DOWN )
relationshipage_id = pd.find_element_by_xpath('//*[@id="relationshipage_id"]')
relationshipage_id.send_keys(Keys.DOWN ,Keys.DOWN,Keys.DOWN,Keys.DOWN,Keys.DOWN )
name = pd.find_element_by_xpath('//*[@id="form1"]/div[2]/center/table/tbody/tr[3]/td/input')
name.send_keys(first)
income = pd.find_element_by_xpath('//*[@id="income"]')
income.send_keys(Keys.DOWN ,Keys.DOWN,Keys.DOWN,Keys.DOWN)
maritalparents = pd.find_element_by_xpath('//*[@id="maritalparents"]')
maritalparents.send_keys(Keys.DOWN ,Keys.DOWN,Keys.DOWN)
siblings = pd.find_element_by_xpath('//*[@id="siblings"]')
siblings.send_keys(Keys.DOWN)
birthorder = pd.find_element_by_xpath('//*[@id="birthorder"]')
birthorder.send_keys(Keys.DOWN)
datekids = pd.find_element_by_xpath('//*[@id="datekids"]')
datekids.send_keys(Keys.DOWN, Keys.DOWN)
datesmokers = pd.find_element_by_xpath('//*[@id="datesmokers"]')
datesmokers.send_keys(Keys.DOWN, Keys.DOWN)
weight = pd.find_element_by_xpath('//*[@id="weight"]')
weight.send_keys(Keys.DOWN, Keys.DOWN)
h = str(randint(0, 999))

profession = pd.find_element_by_xpath('//*[@id="profession"]')
profession.send_keys(prof)
h = str(randint(0, 999))

headline = pd.find_element_by_xpath('//*[@id="headline"]')
headline.send_keys(headline2)
d = str(randint(0, 999))
description = pd.find_element_by_xpath('//textarea[.=""][1]')
description.send_keys(description2)
interests = pd.find_element_by_xpath('//*[@id="interests"]')
interests.send_keys(interests2)
submit2 = pd.find_element_by_xpath('//*[@id="form1"]/div[3]/center/table/tbody/tr[8]/td/center/input[10]')
time.sleep(2)
submit2.click()
time.sleep(30)



