import requests
from pypac import PACSession, get_pac
pac = get_pac(url='https://whalesapp.fun/foxy.PAC')
from lxml import html
import re
import time
import configparser
import sqlite3
usersDescriptions = []
import time
import Config
import zipcodes
from random import randint
from faker import Faker
fake = Faker()
ALL_PROXIES = []

logins = []
# Import Config for your username and password
user = Config.DATACOUP_USERNAME
psw = Config.DATACOUP_PASSWORD
url = r'https://www.pof.com/register.aspx?id=1'

#co.add_argument('--ignore-certificate-errors-spki-list')
#co.add_argument('--ignore-ssl-errors')


#capabilities = webdriver.DesiredCapabilities.FIREFOX
#prox.add_to_capabilities(capabilities)


client = PACSession(pac=pac)

#proxies = { 'http', new }
print(client.proxies)
# client.proxies = ['http://'+new]

    # But wait-- there's more!
    # Use the user-configured useragent string
client.headers.update(
    {
        'Accept-Encoding': "gzip, deflate, br",
        'Referer': "http://www.pof.com/",
        'Content-Type': "application/x-www-form-urlencoded",
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36"
    }
)
from random import randint

class Session:
    
    # Exception type for various session errors.
    class POFSessionError(Exception):
        def __init__(self, value):
            self.value = value


    class Parser():
    
        @staticmethod
        def scrape( datapoint, text ):
            cases = {
                "register-form": Session.Parser.registerform,
                "description": Session.Parser.description,
                "sid": Session.Parser.SID_login,
                "active_session": Session.Parser.is_logged_in,
                "csrf_token": Session.Parser.csrf_token_login,
                "installId": Session.Parser.installId_login,
                "deviceId": Session.Parser.deviceId_login,
                "deviceLocale": Session.Parser.deviceLocale_login,
                "msgFormHiddenElements": Session.Parser.msgFormHiddenElements,
                "profile_photos": Session.Parser.profile_photos,
                "users": Session.Parser.search_users,
                "uid_from_url": Session.Parser.uid_from_url,
            }
            return cases[datapoint](text)
        @staticmethod
        def registerform(text):
            loginFormTree = html.fromstring( text )
            action_xpath = loginFormTree.xpath( '//*[@id="register-form"]/form/@action' )
            action = action_xpath[0].value
            return action
        @staticmethod
        def description(text):
            loginFormTree = html.fromstring( text )
            description_xpath = loginFormTree.xpath( '//*[@id="description"]/text()' )
            description = ""
            if len(description_xpath) > 0:
                description = "".join(description_xpath)
                description = description.replace('\r', '').replace('\n', '')

            else:
                print('len == 0')

            return description
        @staticmethod
        def SID_login(text):
            loginFormTree = html.fromstring( text )
            sid_xpath = loginFormTree.xpath( '//form[@name="frmLogin"]//input[@name="sid"]' )

            if len(sid_xpath) > 0:
                sid = sid_xpath[0].value
            else:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            if sid is None:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            return sid

        @staticmethod
        def csrf_token_login(text):
            loginFormTree = html.fromstring( text )
            csrf_token_xpath = loginFormTree.xpath( '//form[@name="frmLogin"]//input[@name="csrf_token"]' )

            if len(csrf_token_xpath) > 0:
                csrf_token = csrf_token_xpath[0].value
            else:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            if csrf_token is None:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            return csrf_token

        @staticmethod
        def installId_login(text):
            loginFormTree = html.fromstring( text )
            installId_xpath = loginFormTree.xpath( '//form[@name="frmLogin"]//input[@name="installId"]' )

            if len(installId_xpath) > 0:
                installId = installId_xpath[0].value
            else:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()
            if installId is None:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()
            return installId

        @staticmethod
        def deviceId_login(text):
            loginFormTree = html.fromstring( text )
            deviceId = loginFormTree.xpath( '//form[@name="frmLogin"]//input[@name="deviceId"]' )

            if len(deviceId) > 0:
                deviceId = deviceId[0].value
            else:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()
            if deviceId is None:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            return deviceId

        @staticmethod
        def deviceLocale_login(text):
            loginFormTree = html.fromstring( text )
            deviceLocale = loginFormTree.xpath( '//form[@name="frmLogin"]//input[@name="deviceLocale"]' )

            if len(deviceLocale) > 0:
                deviceLocale = deviceLocale[0].value
            else:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            if deviceLocale is None:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            return deviceLocale

        @staticmethod
        def is_logged_in( text ):
            edit_profile_page = html.fromstring( text )
            sign_in_link_xpath = edit_profile_page.xpath( '/html/body/div[1]/div[1]/div/div/span[3]/a' )

            ret = False
            print(sign_in_link_xpath[0].text)
            if len(sign_in_link_xpath) > 0:
                if sign_in_link_xpath[0].text == "Sign In":
                    ret = False
                else:
                    ret = True

            return ret

        @staticmethod
        def msgFormHiddenElements(m):
            # Add error handling
            msgFormTree = html.fromstring(m)

            # Add error handling
            hiddenElementsTree = msgFormTree.xpath('//form[@name="sendmessage"]/input[@type="hidden"]')

            hiddenElements = {}
            for entry in hiddenElementsTree:
                hiddenElements[entry.attrib['name']] = entry.attrib['value']

            return hiddenElements
        

         #   try:
         #       client.post(register1, data=loginData, allow_redirects=True))
         #   except requests.exceptions.ConnectionError:
         #       raise Session.POFSessionError("Could not logout.")
        @staticmethod
        def send_message_failed(m):
            return not re.search("messagesent=1", m)

        @staticmethod
        def profile_photos(m):
            profile_tree = html.fromstring(m)

            photos_xpath = profile_tree.xpath('//div[@class="image-thumb-wrap"]/a/img/@src')

            photos = list()
            for photo in photos_xpath:
                photos.append(photo)

            return photos

        @staticmethod
        def search_users(m):
            results_page = html.fromstring( m )

            # returns only the urls.  not wanted if you want a user object.

            # profile_list = results_page.xpath('//div[@class="profile"]//a/@href')
            profile_list = results_page.xpath('//div[@class="results"]')

            # container for POFSession.Users objects
            users = list()

            for i, profile in enumerate(profile_list):

                # we only care about url and online status right now
                href = profile.xpath('div[@class="profile"]/a/@href')

                if len(href) is not 0:
                    href = href[0]
                else:
                    #print('len all proxies')
                    #print (len(ALL_PROXIES))
                    if len(ALL_PROXIES) > 0:
                        aaa=1#new = ALL_PROXIES.pop()
                    else:
                        aaa=1#ALL_PROXIES = get_proxies()
                        aaa=1#new = ALL_PROXIES.pop()
                    # reassign driver if fail to switch proxy
                    #pd = proxy_driver(ALL_PROXIES)
                    #proxies = { 'http', new }
                    # client.proxies = ['http://'+new]
                    #print("--- Switched proxy to: %s" % new)
                    time.sleep(1)
                    with open('logins.txt') as f:
                        content = f.readlines()
                    # you may also want to remove whitespace characters like `\n` at the end of each line
                    content = [x.strip() for x in content] 
                    count = 0
                    done = False
                    for line in content:
                        if count == int(self.config.user) + 1:
                            done = True
                            self.config.user = int(self.config.user) + 1
                            self.config.username = line.split(',')[0]
                            self.config.password = line.split(',')[2]
                        count = count + 1
                    if done == False:
                        self.config.user = 0
                        self.config.username = "BenjaminDuran223"
                        self.config.password = "LightBlue223"
                    self.login()
                
                online_status_string = profile.xpath('div[@class="description"]/div[@class="about"]/font/text()')

                if len(online_status_string) is not 0:
                    online_status_string = online_status_string[0]

                thisUser = Session.User("https://www.pof.com/" + href)
                searchURL = "https://www.pof.com/" + href
                try:
                    profile_page = client.get( searchURL )
                except:
                    #print('len all proxies')
                    #print (len(ALL_PROXIES))
                    if len(ALL_PROXIES) > 0:
                        aaa=1#new = ALL_PROXIES.pop()
                    else:
                        aaa=1#ALL_PROXIES = get_proxies()
                        aaa=1#new = ALL_PROXIES.pop()
                    # reassign driver if fail to switch proxy
                    #pd = proxy_driver(ALL_PROXIES)
                    #proxies = { 'http', new }
                    # client.proxies = ['http://'+new]
                    #print("--- Switched proxy to: %s" % new)
                    time.sleep(1)
                    with open('logins.txt') as f:
                        content = f.readlines()
                    # you may also want to remove whitespace characters like `\n` at the end of each line
                    content = [x.strip() for x in content] 
                    count = 0
                    done = False
                    for line in content:
                        if count == int(self.config.user) + 1:
                            done = True
                            self.config.user = int(self.config.user) + 1
                            self.config.username = line.split(',')[0]
                            self.config.password = line.split(',')[2]
                        count = count + 1
                    if done == False:
                        self.config.user = 0
                        self.config.username = "BenjaminDuran223"
                        self.config.password = "LightBlue223"
                    self.login()
                if profile_page not in usersDescriptions:
                    time.sleep(0.05)
                    description = Session.Parser.scrape("description", profile_page.content)
                    thisUser.description = description
                if online_status_string == "Online Now":
                    thisUser.set_online()

                users.append(thisUser)

            return users

        @staticmethod
        def uid_from_url(m):
            searchobj = re.search('profile_id=(.*)', m)
            return searchobj.group(1)


    # Initializer for the POFSession class
    def __init__(self, config):
        self.config = config

        # handle to use for getting new pages with existing POF session
        

        # But wait -- there's more!
        # Throwing in rudimentary proxy support:
        #if self.config.proxy_enabled:
            
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]

        self.contactTracker = Session.ContactRecorder(self.config)
        self.contactTracker.ensureMessageHistoryTable()

    # Log in to POF.com as if you were a browser
    def login(self):
        time.sleep(10)
        # Can also get this from the response Set-Cookie header as
        loginURLS = {
            "formPage": "https://www.pof.com/inbox.aspx",
            "processPage": "https://login.pof.com/",
        }
        print(loginURLS)
        try:
            page_response = client.get(loginURLS["formPage"])

        except Exception as e:
            print(e)
            time.sleep(20)
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            #print(e)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            self.login()

        # get form values
        sid = Session.Parser.scrape("sid", page_response.content)
        csrf_token = Session.Parser.scrape("csrf_token", page_response.content)
        installId = Session.Parser.scrape("installId", page_response.content)
        deviceId = Session.Parser.scrape("deviceId", page_response.content)
        deviceLocale = Session.Parser.scrape("deviceLocale", page_response.content)
        print('sid etc')
        print(sid)
        print(self.config.username)
        print(self.config.password)
        # This site actually checks for these unset variables :/
        loginData = {
            'csrf_token': csrf_token,
            'installId': installId,
            'deviceId': deviceId,
            'deviceLocale': deviceLocale,
            'url': '',
            'username': self.config.username,
            'password': self.config.password,
            'sid': sid,
            # Also empty.
            'login': '',
        }

        try:
            login = client.post(loginURLS["processPage"], data=loginData, allow_redirects=True)
        except:
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            self.login()


        # throw exception if no active session created
        if not self.has_active_session():
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            print(self.config.username)
            print(self.config.password)
            self.login()
        print("Successfully logged in as user '{0}'.".format(self.config.username))

    def sendMessage(self, user, body):

        messageGateway = "https://www.pof.com/sendmessage.aspx"
        profileURL = "https://www.pof.com/viewprofile.aspx?profile_id=" + user.uid

        try:
            profileForm = client.get(profileURL)
        except:
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            self.login()

        fields = Session.Parser.scrape("msgFormHiddenElements", profileForm.content)

        client.headers.update(
            {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'en-US,en;q=0.9,es;q=0.8,mt;q=0.7',
'Content-Type': 'application/x-www-form-urlencoded',
'Host': 'www.pof.com',
'Origin': 'https://www.pof.com',
                
                'Referer': profileURL,
            }
        )

        fields.update(
            {
                "subject": 'Hi',
                "message": body,
                "sendmesage": "Send Quick Msg",
            }
        )
        try:
            submit_response = client.post(messageGateway, data=fields)
        except:
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            self.login()
        
        if Session.Parser.send_message_failed(submit_response.url):
            print("Failed to send a message to user " + user.uid + ".  Blocked?")
            logoutGateway = "https://www.pof.com/abandon.aspx"

            try:
                client.get(logoutGateway)
            except:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()
            
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
                time.sleep(60 * 4 * 60)
            self.login()
            if not self.has_active_session():
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()
        else:
            print("Successfully sent message to user " + user.uid)

    def searchUsers(self, searchCriteria, num_users, online_only=False):
        searchURL = "https://www.pof.com/advancedsearch.aspx"

        if not self.has_active_session():
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            self.login()

        total_users = list()

        page = 0
        while len(total_users) < num_users:
            page += 1

            filtered_users = list()

            options = "?iama=" + searchCriteria.gender + \
                      "&minage=" + searchCriteria.min_age + \
                      "&maxage=" + searchCriteria.max_age + \
                      "&state=" + "" + \
                      "&city=" + searchCriteria.zipcode + \
                      "&interests=" + searchCriteria.interests + \
                      "&seekinga=" + searchCriteria.target_gender + \
                      "&country=" + searchCriteria.country + \
                      "&height=" + searchCriteria.min_height + \
                      "&heightb=" + searchCriteria.max_height + \
                      "&maritalstatus=" + searchCriteria.maritalstatus + \
                      "&relationshipage_id=" + searchCriteria.relationshipage_id + \
                      "&wantchildren=" + searchCriteria.wants_children + \
                      "&smoke=" + searchCriteria.smokes + \
                      "&drugs=" + searchCriteria.drugs + \
                      "&body=" + searchCriteria.body_type + \
                      "&smarts=" + searchCriteria.smarts + \
                      "&pets=" + searchCriteria.has_pets + \
                      "&eyes_id=" + searchCriteria.eye_color + \
                      "&income=" + searchCriteria.income + \
                      "&profession_id=" + searchCriteria.profession + \
                      "&haircolor=" + searchCriteria.hair_color + \
                      "&drink=" + searchCriteria.drinks + \
                      "&religion=" + searchCriteria.religion + \
                      "&haschildren=" + searchCriteria.has_children + \
                      "&miles=" + searchCriteria.max_distance + \
                      "&page=" + str(page) + \
                      "&count=1000"

            completeURL = searchURL + options

            try:
                results_page = client.get( completeURL )

            except:
                #print('len all proxies')
                #print (len(ALL_PROXIES))
                if len(ALL_PROXIES) > 0:
                    aaa=1#new = ALL_PROXIES.pop()
                else:
                    aaa=1#ALL_PROXIES = get_proxies()
                    aaa=1#new = ALL_PROXIES.pop()
                # reassign driver if fail to switch proxy
                #pd = proxy_driver(ALL_PROXIES)
                #proxies = { 'http', new }
                # client.proxies = ['http://'+new]
                #print("--- Switched proxy to: %s" % new)
                time.sleep(1)
                with open('logins.txt') as f:
                    content = f.readlines()
                # you may also want to remove whitespace characters like `\n` at the end of each line
                content = [x.strip() for x in content] 
                count = 0
                done = False
                for line in content:
                    if count == int(self.config.user) + 1:
                        done = True
                        self.config.user = int(self.config.user) + 1
                        self.config.username = line.split(',')[0]
                        self.config.password = line.split(',')[2]
                    count = count + 1
                if done == False:
                    self.config.user = 0
                    self.config.username = "BenjaminDuran223"
                    self.config.password = "LightBlue223"
                self.login()

            this_page_users = Session.Parser.scrape("users", results_page.content)

            # we're only adding online users to the filtered users pool if the function is given that directive
            if online_only:
                for user in this_page_users:
                    if user.online:
                        filtered_users.append(user)

                # if we're no longer getting any users after applying the filter it means we're dry
                if len(filtered_users) == 0:
                    return set(total_users)

                total_users.extend( filtered_users )
                print( "Retrieved Page {0} ({1} users)".format( page, len(filtered_users) ) )

            # otherwise we extend by the raw return without filtering
            else:
                total_users.extend( this_page_users )
                print( "Retrieved Page {0} ({1} users)".format( page, len(this_page_users) ) )

        total_users = list(set(total_users))

        return total_users[0:num_users]

    def broadcastMessage(self, users, body):
        for user in users:
            if self.contactTracker.isPreviouslyContactedUser(user):
                print("User {0} has already been contacted and previously contacted members are currently forbidden.".format(user.uid))
                continue
            self.sendMessage(user, body)

    def has_active_session(self):
        # checks if session is active, somehow
        sessionCheckURL = { 
            "editPage": "https://www.pof.com/editprofile.aspx",
        }
        try:
            check_response = client.get( sessionCheckURL["editPage"] )
        except:
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
        return Session.Parser.scrape("active_session", check_response.content)

    def getPhotos(self, user):
        profileURL = "https://www.pof.com/viewprofile.aspx?profile_id=" + user.uid

        try:
            profile = client.get(profileURL)
        except:
            #print('len all proxies')
            #print (len(ALL_PROXIES))
            if len(ALL_PROXIES) > 0:
                aaa=1#new = ALL_PROXIES.pop()
            else:
                aaa=1#ALL_PROXIES = get_proxies()
                aaa=1#new = ALL_PROXIES.pop()
            # reassign driver if fail to switch proxy
            #pd = proxy_driver(ALL_PROXIES)
            #proxies = { 'http', new }
            # client.proxies = ['http://'+new]
            #print("--- Switched proxy to: %s" % new)
            time.sleep(1)
            with open('logins.txt') as f:
                content = f.readlines()
            # you may also want to remove whitespace characters like `\n` at the end of each line
            content = [x.strip() for x in content] 
            count = 0
            done = False
            for line in content:
                if count == int(self.config.user) + 1:
                    done = True
                    self.config.user = int(self.config.user) + 1
                    self.config.username = line.split(',')[0]
                    self.config.password = line.split(',')[2]
                count = count + 1
            if done == False:
                self.config.user = 0
                self.config.username = "BenjaminDuran223"
                self.config.password = "LightBlue223"
            self.login()

        photos = Session.Parser.scrape("profile_photos", profile.content)

        return photos


    class User():
        def __init__(self, profile_url):
            self.profile_url = profile_url
            self.uid = Session.Parser.scrape("uid_from_url", self.profile_url)
            self.description = ""
            self.online = False

        def set_online(self):
            self.online = True

        def __repr__(self):
            return "{0} ({1})".format(self.uid, self.online)


    class Config():
        def __init__(self, config_file):
            settings = configparser.ConfigParser(allow_no_value=True)
            settings.read(config_file)

            self.useragent = settings.get("general-client", "user_agent")

            self.username = settings.get("pof-session", "username")
            self.user = settings.get("pof-session", "user")
            self.password = settings.get("pof-session", "password")

            self.gender = settings.get("pof-search", "gender")
            self.min_age = settings.get("pof-search", "min_age")
            self.max_age = settings.get("pof-search", "max_age")
            self.zipcode = settings.get("pof-search", "zipcode")
            self.interests = settings.get("pof-search", "interests")
            self.target_gender= settings.get("pof-search", "target_gender")
            self.country = settings.get("pof-search", "country")
            self.min_height = settings.get("pof-search", "min_height")
            self.max_height = settings.get("pof-search", "max_height")
            self.maritalstatus = settings.get("pof-search", "marital_status")
            self.relationshipage_id = settings.get("pof-search", "relationshipage_id")
            self.wants_children = settings.get("pof-search", "wants_children")
            self.smokes = settings.get("pof-search", "smokes")
            self.drugs = settings.get("pof-search", "does_drugs")
            self.body_type = settings.get("pof-search", "body_type")
            self.smarts = settings.get("pof-search", "smarts")
            self.has_pets = settings.get("pof-search", "has_pets")
            self.eye_color = settings.get("pof-search", "eye_color")
            self.income = settings.get("pof-search", "income")
            self.profession = settings.get("pof-search", "profession")
            self.hair_color = settings.get("pof-search", "hair_color")
            self.religion = settings.get("pof-search", "religion")
            self.drinks = settings.get("pof-search", "drinks")
            self.has_children = settings.get("pof-search", "has_children")
            self.max_distance = settings.get("pof-search", "max_distance")

            self.proxy_enabled = settings.getboolean("proxy", "enabled")

            if self.proxy_enabled:
                self.proxy = settings.get("proxy", "proxy")

    class ContactRecorder():
        class DatabaseIOError(Exception):
            def __init__(self, value):
                self.value = value

        def __init__(self, config):
            self.conn = sqlite3.connect("{0}.db".format(config.username))
            if self.conn is not None:
                self.DB = self.conn.cursor()
            else:
                raise self.DatabaseIOError("Could not establish a connection with the database.")

        def ensureMessageHistoryTable(self):
            query = "CREATE TABLE IF NOT EXISTS {tableName} ( targetUserID integer, time DATETIME );".format(tableName="contacts")
            self.DB.execute(query)

        def addUserContactEvent(self, user):
            # adds a contact event to the database
            # uses currentTime

            query = "INSERT INTO {tableName} VALUES( {user}, DATETIME('now', 'localtime') );".format(
                tableName="contacts",
                user=user.uid
            )

            if not self.isPreviouslyContactedUser(user):
                self.DB.execute(query)
                self.conn.commit()
                print("Added uid {0} to db.".format(user.uid))

        def isPreviouslyContactedUser(self, user):
            # checks to see if a specific user has been previously contacted
            # critical that this works to avoid spamming people
            exists = False
            query = "SELECT EXISTS( SELECT 1 FROM {tableName} WHERE targetUserID={uid} LIMIT 1);".format(
                    tableName="contacts",
                    uid=user.uid
                )
            r = self.DB.execute(query)
            result = r.fetchone()[0]

            if int(result) == 1:
                exists = True

            return exists
