# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class StoryTestPipeline(object):
    def process_item(self, item, spider):
        fh = open('C:\\Users\\Administrator\\Desktop\\1.doc', 'a')
        string = ''
        for i in range(len(item['text'])):
            string += item['text'][i].strip() + '\n'
        fh.write('\t'*5 + item['h'])
        fh.write(string)
        print('\t'*5 + item['h'])
        return item
