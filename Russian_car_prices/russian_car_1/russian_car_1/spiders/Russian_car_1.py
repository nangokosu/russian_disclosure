import scrapy
from scrapy_splash import SplashRequest
import scrapy_splash

class RussianCar1Spider(scrapy.Spider):
    name = 'Russian_car_1'
    def start_requests(self):
        url='https://www.avtogermes.ru/sale/new/'
        yield SplashRequest(url=url,callback=self.parse)

    def parse(self, response):
        brand_model=response.xpath('//div[@class="shaded h3"]/text()[1]').getall()
        no_discount_price_list=list()
        no_discount_price=response.xpath('//div[@class="price"]')
        for element in no_discount_price:
            if len(element.xpath('./b'))>0:
                no_discount_price_list.append(element.xpath('./b/text()').getall()[0])
            if len(element.xpath('./strong'))>0:
                no_discount_price_list.append(element.xpath('./strong/text()').getall()[0])
        year=response.xpath('//div[@class="p dop-info shaded"]/strong[1]/text()').getall()
        for i in range(len(brand_model)):
            yield {"brand_model":brand_model[i],
            "price":no_discount_price_list[i],
            "year":year[i]}
        # pagination:
        next_page=response.xpath('//a[@rel="next"]/@href').getall()
        if len(next_page)>0:
            yield SplashRequest('https://www.avtogermes.ru'+next_page[0],callback=self.parse)

    def parse2(self,response):
        car_dict={}
        elements=response.xpath('//div[@class="col-12 col-md-6"]/div[@class="row"]')
        for element in elements:
            if element.xpath('./div[1]/text()').getall()[0]=="Марка":
                car_dict['Brand (Марка)']=element.xpath('./div[2]/strong/text()').getall()[0]
            if element.xpath('./div[1]/text()').getall()[0]=="Модель":
                car_dict['Model (Модель)']=element.xpath('./div[2]/strong/text()').getall()[0]
            if element.xpath('./div[1]/text()').getall()[0]=="Год выпуска":
                car_dict['Year of issue (Год выпуска)']=element.xpath('./div[2]/strong/text()').getall()[0]
            if element.xpath('./div[1]/text()').getall()[0]=="Цена с учетом выгоды":
                car_dict['Price with benefits (Цена с учетом выгоды)']=element.xpath('./div[2]/strong/text()').getall()[0]
            if element.xpath('./div[1]/text()').getall()[0]=="Кузов":
                car_dict['Body (Цена с учетом выгоды)']=element.xpath('./div[2]/strong/text()').getall()[0]
        return car_dict