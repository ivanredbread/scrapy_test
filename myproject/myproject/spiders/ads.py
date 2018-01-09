# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 22:29:18 2018

@author: tedoreve
"""

# -*- coding: utf-8 -*-
import scrapy
#from scrapy.loader import ItemLoader
from myproject.items import AdsItem

class AdsSpider(scrapy.Spider):
    
#==============================================================================    
    urllist=['2014ApJ...793...95Z',
             '2014ApJ...783L...2T']

        
#==============================================================================

    op  = 'http://adsabs.harvard.edu/cgi-bin/nph-ref_query?bibcode='
    ed  = '&amp;refs=CITATIONS&amp;db_key=AST'
    name = "ads"
    allowed_domains = ["adsabs.harvard.edu"]
    start_urls = (
    op+urllist[0]+ed,
    op+urllist[1]+ed,
    )

#==============================================================================

    def parse(self, response):

        item = AdsItem()
        item['name'] = response.xpath('//tr[@valign="top"]/td[@align="left"]/h3/a/text()').extract()[0]
        item['link'] = response.xpath('//form/input/@value').extract()[0]                        
        yield item


