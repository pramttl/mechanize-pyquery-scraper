'''
Author: Pranjal Mittal
14/03/2013
Extracting Information of Indian Restaurants in Chicago from a website (Sulekha) and structuring the information.
Runnning Time: 2 minutes (500 kbps internet connectivity)

BASE_LINK = http://mycity.sulekha.com/restaurants_in_chicago-metro-area_0
'''
# mechanize emulates a browser session via code.
import mechanize_boilerplate
from pyquery import PyQuery as PQ

br = mechanize_boilerplate.br

##########################################################################################################################################
from pyquery import PyQuery as PQ
from xlwt import Workbook
book = Workbook()
sheet1 = book.add_sheet('Restaurants1')
sheet1.write(0,0,'Name')
sheet1.write(0,1,'Address')
sheet1.write(0,2,'Contact')

'''
def details_scrapper(url):
    global br
    obj = PQ(br.open(url).read())
    tables = obj("table")

    contact = tables.eq(12).text()
    features = tables.eq(14)("tr").eq(2).text()
    hours = tables.eq(14)("tr").eq(3).text()
    note = tables.eq(18)("tr").eq(3).text()
    return (contact,features,hours,note)
'''

total = 0
try:
    # Opening the pages one by one.
    for i in range(0,8):
        info_url = 'http://mycity.sulekha.com/restaurants_in_chicago-metro-area_%s'%(str(i),)

        r = br.open(info_url)
        html = r.read()
        obj = PQ(html)

        n = 24
        for ind in range(3,27):
            restobj = obj("div.bgborder.pad5trbl").eq(ind)

            #Restaurant Name
            name = restobj("div").eq(1).text()

            #Address
            s = restobj("div").eq(2).text()
            phni = s.lower().find('phone')
            address = s[:phni-1]

            #Phone Number
            contact = s[phni+7:]

            sheet1.write(total+ind,0,name)
            sheet1.write(total+ind,1,address)
            sheet1.write(total+ind,2,contact)

        total+=n
        print str(i) + ' out of 9 pages done'

# To save whatever has been scrapped in case any exception is encountered.
except:
    book.save('result.xls')

book.save('result.xls')

