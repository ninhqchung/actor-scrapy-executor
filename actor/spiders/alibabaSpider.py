import apify
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class SipSpider(CrawlSpider):
    name = 'sip'
    allowed_domains = ['alibaba.com']
    start_urls = ['https://gdxianxing03.en.alibaba.com/productlist.html']
    rules = (
        Rule(LinkExtractor(allow='productlist-1')),
        Rule(LinkExtractor(allow='product-detail'), callback='parse_item')
    )

    def parse_item(self, response):
        url = response.url
        title = response.css('title::text').get()
        variants = response.css('.sku-option')
        # image = response.css('div.main-item > img').attrib['src'].replace('_100x100xz.jpg','')
        image_list = []

        for image in variants:
            image = response.css('div.main-item > img').attrib['src'].replace('_100x100xz.jpg','')
            image_list.append(image)
            
        
        # yield(image_list)
            


        try:
            variant_img = response.css('.sku-option > img').attrib['src'].replace('_100x100xz.jpg','')
        except Exception:
            variant_img = response.css('div.image-view > a > div > img').attrib['src']
        except:
            variant_img = 'None'
        yield {
            'tile': title,
            # 'variant_img': variant_img,
            # 'image': image,
            'imagelist': image_list,
            'url': url
        }

        # output = {
        #     'tile': title,
        #     'variant_img': variant_img,
        #     'url': url
        # }
        # apify.pushData(output) #Khi nào push lên mới cần đẩy qua DataStore
        

