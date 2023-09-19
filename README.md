[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)
[![GitHub all releases](https://img.shields.io/github/downloads/idreamshen/hass-volvooncall-cn/total)](https://github.com/idreamshen/hass-volvooncall-cn/releases)

# Volvo On Call CN
Homeassistant volvooncall 中国区插件

# 功能列表
1. Sensor: 油箱、里程数、续航里程
2. BinarySensor: 门、车锁、窗、发动机
3. DeviceTracker: 位置

# TODO
- 远程开锁
- 远程关锁
- 远程启动空调
- 远程关闭空调

# 测试车型
- 2021 S60

# HACS 安装集成
HACS -> 集成 -> 右上角三个点 -> 自定义存储库
- 存储库：https://github.com/idreamshen/hass-volvooncall-cn
- 类别：集成

浏览并下载存储库 -> 搜索 Volvo On Call CN 并下载

# Homeassistant 添加集成
设置 -> 设备与服务 -> 添加集成 -> 搜索品牌 Volvo On Call CN -> 填入手机号和密码
- 手机号：11 位纯数字
- 密码：即“沃尔沃APP”上的登录密码，需要提前设置好登录密码

提交稍等片刻后，即可看到拥有的车辆设备

# 效果预览
<img src="images/screenshot-20230729-011246.png" alt="" width="50%"/>
<img src="images/screenshot-20230729-011320.png" alt="" width="50%"/>
