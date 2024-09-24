# BBB LED Webserver with Flask

基于 BeagleBoard Black 开发板，在系统中使用 Flask 建立一个网页，并且与板载 LED 联动。板卡通过网线与 PC 通信与供电，用户可通过网页按键控制 LED 的开关与闪烁。LED 通过 gpiod 控制。

# 📦 Prerequisites

开发环境：BBB 官方提供的 [Debian 11.7 镜像](https://www.beagleboard.org/distros)。项目所用到的库、参考如下：

1. python-flask
2. python-gpiod
3. [BBB Cookbook](https://docs.beagleboard.org/latest/books/beaglebone-cookbook/index.html#bone-cook-book-home)

所使用的 LED 为 USR3，最终部署的端口可修改。

```python
app.run(host="0.0.0.0", port=8080, debug=True)
```

## 📽️ More details

1. 项目详细说明，[CSDN：基于BeagleBone Black的网页LED控制功能(flask+gpiod)](https://blog.csdn.net/weixin_46422143/article/details/142466019)
2. 项目功能演示，[B站：基于BeagleBone Black的网页LED控制功能](https://www.bilibili.com/video/BV1Acsve4EQn/)
