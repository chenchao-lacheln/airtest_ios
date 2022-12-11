# -*- encoding=utf8 -*-
__author__ = "lacheln"

from airtest.core.api import *

auto_setup(__file__)
'''
assert_equal:判断第一个值和第二个值是否相等
assert_not_equal:判断第一个值和第二个值是否不相等
判断预期结果和实际结果是不是相等的
'''

# exists(Template(r"tpl1670785802536.png", record_pos=(0.002, -0.71), resolution=(1284, 2778)))

assert_equal(False, exists(Template(r"tpl1670785802536.png", record_pos=(0.002, -0.71), resolution=(1284, 2778))), "判断 页面 不存在todesk logo")
