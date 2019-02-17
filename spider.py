from urllib import request
from crawel import get_request
from crawel.config import SpiderConfig


itao_buyer = SpiderConfig('http://www.itaomiao.com/purchases/purchaseList.itm')

def crawel_tender(re):   #crawel the tender information
    page = request.urlopen(re)
    html = page.read()
    print(type(html))


crawel_tender(get_request(itao_buyer))