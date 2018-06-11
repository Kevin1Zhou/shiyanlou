# -*- coding:utf-8 -*-

import scrapy

class ShiyanlouSpider(scrapy.Spider):
	name = 'shiyanlou-courses'
	
	@property #scrapy.Spider 类已经有了一个默认的 start_requests方法,只提供需要爬取的 start_urls，默认的 start_requests 方法会根据 start_urls 生成 Request 对象
	def start_urls(self): #需要返回一个可迭代对象，所以，你可以把它写成一个列表、元组或者生成器，这里用的是生成器
		url_temp = 'https://www.shiyanlou.com/courses/?category=all&course_type=all&fee=all&tag=all&page={}'
		return (url_temp.format(i) for i in range(1,23)) #返回一个生成器,.format格式化输出page后{}的内容，这里为page=1直到page=22
	def parse(self,response):
		for course in response.css('div.course-body'):
			yield {
				'name': course.css('div.course-name::text').extract(),
				'description': course.css('div.course-desc::text').extract(),
				'type': course.css('div.course-footer span.pull-right::text').extract_first(default='Free'),
				'students': course.css('div.course-footer span.pull-left::text').re('[^\d]*(\d+)[^\d]*')
				#'students': course.xpath('.//span[contains(@class, "pull-left")]/text()[2]').re_first('[^\d]*(\d+)[^\d]*')
				#使用xpath需要注意//前面的. , 没有点表示整个文档所有的div.course-body,有. 才表示当前迭代的这个div.course-body

			}

"""
<div class="course-body">
    <div class="course-name">Python 数据分析入门与进阶</div>
            <div class="course-desc">在本训练营中，我们将学习怎么样使用 Python 进行数据分析。课程将从数据分析基础开始，一步步深入讲解。从 Python 的基础用法到数据分析的各种算法，并结合各种实例，讲解数据分析过程中的方方面面。</div>
            <div class="course-footer">
                <span class="course-per-num pull-left">
				
                    <i class="fa fa-users"></i>

                    133

                </span>

             <span class="course-bootcamp pull-right">训练营</span>        
      </div>
</div>
"""