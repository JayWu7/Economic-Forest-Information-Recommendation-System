from urllib import request

def crawel_tender(url):   #crawel the tender information
    page = request.urlopen(url)
    page.read()