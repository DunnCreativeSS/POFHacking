from faker import Faker
from random import randint
import zipcodes
proxies = [u'167.99.169.232:3128', u'104.236.48.178:8080', u'12.205.32.193:53281']
a = 0
fake = Faker()

while a <= 20:
    a = a + 1
    name = fake.name()
    first = name.split(' ')[0]
    last = name.split(' ')[1]
    textnows = []
    index = str(randint(0, 500))
    i = str(randint(0, 500))
    pi = (randint(0, len(proxies) - 1))
    p = fake.color_name()+index
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
    description = (para + '      Beep Boop I\'m a B0t! Should you want to reach back out to me, check this (my original profile): pof dot com / viewprofile dot aspx ? profile_id=161871538        I had a joke profile for the longest time, haha, and decided it was time to spend some serious time being serious about this serious world of online dating.      Seriously,... I have a great job that\'s rewarding, challenging and constantly evolving. I\'m involved in an industry that\'s technical and changes lives - and wouldn\'t have it any other way. I incorporated my self-employment income in 2015 and would appreciate getting to know more small business owners. I have a family I adore and that adores me, and friends I wouldn\'t trade the world for.      I\'m looking for someone to compliment me, compliment my lifestyle and be an \'equal yet opposite\' factor in moving onwards and upwards to a better future together.       I have a strong affection for all things science fiction, enjoy eclectic and eccentric things and my two cats are my favorite people.      Am looking for kids, marriage, house with a white picket fence (preferably next to a body of water). \'Go big or go home,\' right?      I\'m a mental health consumer and advocate. I welcome discussing these issues with anyone interested - open discussion and interaction on sensitive subjects is required to lift taboos.')
    interests = ",".join(fake.words(nb=6, ext_word_list=None, unique=True))
    interests = '"' + interests + '"'
    headline = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
    textnows.append('\n' + first+',' + last + ','+name.split(' ')[0]+name.split(' ')[1]+index+',' + p + ','+ e + ',' + prof + ',' + zipIn + ',' + cityIn + ',' + stateIn + ',716,' + headline + ',' + interests + ',' + description)
    with open('exampletextnow.csv', 'a') as f:
        for item in textnows:
            f.write("%s   " % item)