from urllib import request
from crawel import get_request
from crawel.config import SpiderConfig
import xml.etree as etree
import xml
itao_buyer = SpiderConfig('http://www.itaomiao.com/purchases/purchaseList.itm')

def crawel_tender(re):   #crawel the tender information
    page = request.urlopen(re)
    doc = etree.HTML(page.read())
    print(doc.findall('//li'))


crawel_tender(get_request(itao_buyer))