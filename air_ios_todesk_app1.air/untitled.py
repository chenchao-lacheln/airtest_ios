# -*- encoding=utf8 -*-
__author__ = "lacheln"

from airtest.core.api import *

auto_setup(__file__)

'''
1.touch 使用 完成todesk启动
'''
touch(Template(r"tpl1670779282594.png", record_pos=(0.341, 0.444), resolution=(1284, 2778)))

'''
2.text 使用 完成登陆todesk登陆操作
wait 使用
'''
# rgb 为true，即在我的 页面时，就不会点击‘我的’栏目


touch(wait(Template(r"tpl1670780117634.png", rgb=True, record_pos=(0.333, 0.951), resolution=(1284, 2778)))) # 确认‘我的’是否出现，出现了就点击，wait会返回图标坐标，touch实现点击操作
touch(Template(r"tpl1670780144300.png", record_pos=(-0.14, -0.736), resolution=(1284, 2778)))
sleep(0.5)
touch(Template(r"tpl1670780331080.png", record_pos=(-0.248, 0.846), resolution=(1284, 2778)))

touch(Template(r"tpl1670780174597.png", record_pos=(-0.287, -0.481), resolution=(1284, 2778)))
text("17511618501")
sleep(0.5)
touch(Template(r"tpl1670780194814.png", record_pos=(-0.378, -0.296), resolution=(1284, 2778)))
text("111111")
sleep(0.5)
touch(Template(r"tpl1670780219072.png", record_pos=(-0.301, -0.155), resolution=(1284, 2778)))
sleep(0.5)
touch(Template(r"tpl1670780537028.png", record_pos=(-0.005, 0.055), resolution=(1284, 2778)))

'''
3.swipe 使用 页面滑动操作
'''
touch(Template(r"tpl1670781486424.png", record_pos=(-0.005, 0.944), resolution=(1284, 2778)))
touch(Template(r"tpl1670781507966.png", record_pos=(-0.299, -0.207), resolution=(1284, 2778)))
# 3.1 自动生成坐标 实现滑动操作
swipe(Template(r"tpl1670781684095.png", record_pos=(-0.284, 0.639), resolution=(1284, 2778)), vector=[-0.00, -0.393],duration=5)

# 3.2 两个图标 滑动
# swipe(Template(r"tpl1670781820653.png", record_pos=(-0.291, 0.632), resolution=(1284, 2778)), Template(r"tpl1670781846592.png", record_pos=(-0.301, -0.205), resolution=(1284, 2778)),duration=5)

'''
4.keyeven 使用 返回到桌面 (iOS设备现在暂时 只支持 HOME 按键的 keyevent 。)
'''
# keyevent("HOME") # 键名
# keyevent("3") # 键码 iOS不支持

'''
5.snapshot 使用 截图 截取当前屏幕的图标，可以在测试报告中显示
'''
# 复用之前的登陆case
snapshot(msg="检查是否登陆成功，用户名是否为CHaron")

'''
6.exist 判断图片是否存在，如果存在就返回图片的中心坐标，不存在就返回false（断言不会报错）
判断todesk logo是否出现
'''
# 复用之前的启动流程
if exists(Template(r"tpl1670783721620.png", record_pos=(0.338, 0.442), resolution=(1284, 2778))):
    touch(exists(Template(r"tpl1670783721620.png", record_pos=(0.338, 0.442), resolution=(1284, 2778)))) # 判断存在之后，实现点击
else:
    print("这个图片是不存在的！")

    
'''
7.assert_exist 判断图标是否存在，如果存在就返回图片的中心坐标，不存在就raise AssersionError （断言会报错）
assert_not_exist 判断图片是否不存在，如果存在就raise AssersionError

判断是否存在todesk app logo，并启动，再判断不存在logo
'''
touch(assert_exists(Template(r"tpl1670784562068.png", record_pos=(0.333, 0.439), resolution=(1284, 2778)), "判断 todesk app logo 是否存在."))
sleep(1)
assert_not_exists(Template(r"tpl1670784639060.png", record_pos=(0.341, 0.444), resolution=(1284, 2778)), "判断 todesk app logo 不存在.")

'''
8.assert_equal:判断第一个值和第二个值是否相等
assert_not_equal:判断第一个值和第二个值是否不相等
判断预期结果和实际结果是不是相等的
'''

assert_equal(False, exists(Template(r"tpl1670785168466.png", record_pos=(0.343, 0.442), resolution=(1284, 2778))), "判断出来页面logo是不存在的")

















