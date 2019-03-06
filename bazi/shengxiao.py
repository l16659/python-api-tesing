#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author:  钉钉或微信pythontesting 技术支持qq群：630011153 144081101
# CreateDate: 2019-2-21

# -*- coding:utf-8 -*-

import argparse
from datas import shengxiaos, zhi_atts

def output(des, key):
    print()
    print(des, end='')
    for item in zhi_atts[zhi][key]:
        print(shengxiaos[item], end='')       

description = '''
'''
parser = argparse.ArgumentParser(description=description,
                                 formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('shengxiao', action="store", help=u'生肖')
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1 Rongzhong xu 2019 03 06 钉钉或微信pythontesting')
options = parser.parse_args()

if options.shengxiao not in shengxiaos.inverse:
    print("请输入正确的生肖：")
    print(shengxiaos.inverse.keys())
else:
    print("你的生肖是：", options.shengxiao)
    zhi = shengxiaos.inverse[options.shengxiao]
    print("你的年支是：", zhi)
    print("="*80) 
    print("生肖是八字的一小部分，有一定参考意义，但是不是全部。") 
    print("合婚请以八字为准，技术支持：钉钉或微信pythontesting") 
    print("="*80) 
    output("与你最合的生肖：", '合')  
    output("与你较合的生肖：", '会')  
    output("与你相冲的生肖：", '冲')  
    output("你刑的生肖：", '刑')
    output("被你刑的生肖：", '被刑') 
    output("与你相害的生肖：", '害')     
    output("与你相破的生肖：", '害')     
        
    
    
    