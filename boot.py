import socket
import time
# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
from machine import Pin #从machine库中导入Pin类
from time import sleep
import upip
from random import randint
import webrepl
import network
import urequests
import ujson
import socket
from lib.microdot import Microdot,send_file



ledpin = Pin(4,Pin.OUT)
webrepl.start(port=3333,password="123456")    
def connectAp(ssid,pwd):
    import network
    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        sta.active(True)
        sta.connect(ssid,pwd)
        while not sta.isconnected():
            pass
    print("network config:",sta.ifconfig())
connectAp("TP-LINK_3B0E","13849115761")

app = Microdot()
@app.route('/')
def index(request):
    return send_file('public/index.html')

@app.get('/off')
def index(request):
    # 如果收到get请求off就关灯
    print("如果收到get请求off就关灯")
    ledpin.value(0)
    return '{"code":200,"value":null}'
# 设置一个get请求 如果
@app.get('/on')
def index(request):
    # 如果收到get请求on就开灯
    ledpin.value(1)
    return "开灯了"

app.run(host='192.168.1.104', port=5000, debug=False, ssl=None)


