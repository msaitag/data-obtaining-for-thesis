# from googletrans import Translator

# sa = 'RESTAURANT GÖRÜNTÜLERİ'
# t = Translator().detect(sa)
# print(type(t))
# print(t.lang)

"""tag1 = "button"
tag2 = ""
clas = 'src'
clasName = '/static/images/google.png'

path = f'//{tag1}{tag2}[@{clas}="{clasName}"]'
print(path)
"""

# currentTime = strftime('%H:%M')
# print(currentTime)
# currentTime = currentTime.replace(':', '')
# currentTime = int(currentTime)
# print(type(currentTime))
# time = []
# for i in range(3):
#     print(i)
#     currentTime += i
#     time.append(currentTime)
#     currentTime -= i

# print(time)


from googletrans import Translator
from unidecode import unidecode
from statistics import mode


def hotelLang(website):
    from selenium import webdriver
    from selenium.webdriver.support.select import By
    from bs4 import BeautifulSoup
    from googletrans import Translator
    import time
    domain = website
    driver = webdriver.Chrome()
    driver.get(domain)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    hotel_lang = []
    excludeItems = ['facebook', 'instagram', 'youtube', 'twitter']
    for tag in soup.find_all(['a', 'option']):
        langs = []
        tagText = tag.get_text()
        try:
            if 'english' in tagText.lower():
                target = tagText.strip()
                l = driver.find_element(
                    by=By.XPATH, value=f'//a/*[contains(text()[1], "{target}")] | //a/*[contains(text()[2], "{target}")] | //a[contains(text()[1], "{target}")] | //a[contains(text()[2], "{target}")]')
            elif tag.find('img') != None:
                img = tag.find('img')
                src = img.get('src')
                if 'en.' in str(src):
                    target = str(src)
                    l = driver.find_element(
                        by=By.XPATH, value=f'//a/img[@src[1] = "{target}"] | //a/img[@src[2] = "{target}"]')
            driver.execute_script("arguments[0].click();", l)
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[0])
            soup2 = BeautifulSoup(driver.page_source, 'html.parser')
            for tag2 in soup2.find_all('a'):
                tagText2 = tag2.get_text()
                t = Translator().detect(tagText2)
                langs.append(t.lang)
            count = 0
            for lan in langs:
                if 'en' == str(lan):
                    count += 1
            if count > len(langs)/2:
                hotel_lang.append('en')
        except:
            continue
    driver.quit()
    return hotel_lang


def xpath():
    from selenium import webdriver
    from selenium.webdriver.support.select import By
    import time
    from bs4 import BeautifulSoup
    driver = webdriver.Chrome()
    driver.get('https://www.hiistanbulcity.com.tr/')
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    item = ""
    for tag in soup.find_all('a'):
        tagText = tag
        if '<img' in str(tagText) and 'en.' in str(tagText):
            img = tag.find('img')
            item = img.get('src')
            item = str(item)
            print(item)
            try:
                l = driver.find_element(
                    by=By.XPATH, value=f'//a/*[@src[1]= "{item}"] | //a[contains(text()[1], "{item}")] | //a[contains(text()[2], "{item}")]')
                driver.execute_script("arguments[0].click();", l)
                time.sleep(5)
                print("Page title is: ")
                if len(driver.window_handles) > 1:
                    driver.switch_to.window(driver.window_handles[1])
            except:
                continue
            url = driver.current_url
    driver.quit()
    return url


# l = driver.find_element(by=By.XPATH, value=f'//a/*[@src[1]= "{item}"] | //a[contains(text()[1], "{item}")] | //a[contains(text()[2], "{item}")]')
# driver.execute_script("arguments[0].click();", l)
# if len(driver.window_handles) > 1:
#     driver.switch_to.window(driver.window_handles[1])
# url = driver.current_url


# csv rename
"""
df = pd.read_csv('eMicaContentAnalysis/csvFiles/results.csv')
renamedDf = df.rename(
    columns={'<function hotelAbout at 0x000002276F7CBB50>': 'hotelAbout'})
renamedDf.to_csv('eMicaContentAnalysis/csvFiles/results.csv', index=False)
"""

"""
array = ['ali', 'ata', 'bak', 'ali']
string = 'ali gel buraya'
x = next(w for w in array if w in string)
y = [w for w in array if w in string]
print(array.index(x))
"""


def webdriver(domain):
    from selenium import webdriver
    from bs4 import BeautifulSoup

    browser = webdriver.Chrome()
    # browser.maximize_window()
    # browser.set_window_size(1920, 1080)
    browser.get(domain)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    browser.close()
    return soup


def hotelSocial(website):
    print(website)
    print(website)
    searchItems = ['instagram', 'facebook', 'twitter']
    errorMessages = ['busayfayaulasilamiyor',
                     'thispageisntavailable', 'thisaccountdoesntexist']
    hotel_social = []
    soup = webdriver(website)
    sayac = 0
    for tag in soup.find_all('a'):
        try:

            href = tag.get('href')
            if any(x in str(href).lower() for x in searchItems):
                href = str(href)
                soup2 = webdriver(href)
                for tag2 in soup2.find_all(['h2', 'span']):
                    tagText = tag2.get_text()
                    tagText = str(tagText)
                    text = ''
                    for i in tagText:
                        if i.isalpha():
                            text += i
                    if any(x in text for x in errorMessages):
                        sayac += 1
                if sayac == 0:
                    hotel_social.append(href)
                # xpath = f'//a[@href[1] = "{href}"] | //a[@href[2] = "{href}"]'
                # url = xpathclick(domain, xpath)
            if len(hotel_social) > 0:
                break
            else:
                continue
        except:
            pass
    return hotel_social


def hotelLang():
    from googletrans import Translator
    inlinks = [
        "https://www.europarkotel.com",
        "https://www.europarkotel.com/galeri",
        "https://www.europarkotel.com/vr-galeri",
        "https://www.europarkotel.com/iletisim",
        "https://www.europarkotel.com/covid-19-planimiz",
        "https://www.europarkotel.com/en",
        "https://www.europarkotel.com/standart-odamiz",
        "https://www.europarkotel.com/delux-odamiz",
        "https://www.europarkotel.com/executive-odamiz",
        "https://www.europarkotel.com/luxury-odamiz",
        "https://www.europarkotel.com/deluxe-oda",
        "https://www.europarkotel.com/luxury-oda",
        "https://www.europarkotel.com/cerez-politikamiz"
    ]

    hotel_lang = []
    langs = []

    for link in inlinks:
        soup = webdriver(link)
        try:
            for tag in soup.find_all('html'):
                tLang = tag.get('lang')
            if tLang != None and tLang not in langs:
                langs.append(tLang)
        except:
            pass

    if len(langs) > 1:
        hotel_lang.append(langs)
    print(hotel_lang)
    return hotel_lang


url = 'https://www.addresshotels.com/fr/hotels/address-istanbul/'
hotelLang()
