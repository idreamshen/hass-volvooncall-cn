![Version](https://img.shields.io/github/v/release/idreamshen/hass-volvooncall-cn?color=green&label=Version)
[![GitHub all releases](https://img.shields.io/github/downloads/idreamshen/hass-volvooncall-cn/total?label=Downloads)](https://github.com/idreamshen/hass-volvooncall-cn/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)


# Volvo On Call CN
Homeassistant volvooncall 中国区插件

# 功能一览
`{vin}` 表示车架号
| ID                                          | 名称               | 备注                                                                                                                                     |
|---------------------------------------------+--------------------+------------------------------------------------------------------------------------------------------------------------------------------|
| lock.{vin}_lock                             | 车锁               | 可以远程锁定或解锁车辆。远程解锁，会变更 `binary_sensor.{vin}_remote_door_unlock` 的状态；远程锁定：变更 `binary_sensor.{vin}_lock` 状态 |
| sensor.{vin}_distance_to_empty              | 续航里程           |                                                                                                                                          |
| binary_sensor.{vin}_lock                    | 车锁状态           |                                                                                                                                          |
| binary_sensor.{vin}_front_left_door         | 前左门             | 表示门是否打开                                                                                                                           |
| binary_sensor.{vin}_front_right_door        | 前右门             |                                                                                                                                          |
| binary_sensor.{vin}_rear_left_door          | 后左门             |                                                                                                                                          |
| binary_sensor.{vin}_rear_right_door         | 后右门             |                                                                                                                                          |
| binary_sensor.{vin}_front_left_window_open  | 前左窗             | 表示窗是否打开                                                                                                                           |
| binary_sensor.{vin}_front_right_window_open | 前右窗             |                                                                                                                                          |
| binary_sensor.{vin}_rear_left_window        | 后左窗             |                                                                                                                                          |
| binary_sensor.{vin}_rear_right_window       | 后右窗             |                                                                                                                                          |
| sensor.{vin}_fuel_amount                    | 油箱剩余油量       |                                                                                                                                          |
| sensor.{vin}_fuel_amount_level              | 油箱剩余油量百分比 |                                                                                                                                          |
| binary_sensor.{vin}_hood                    | 引擎盖             | 表示引擎盖是否打开                                                                                                                       |
| sensor.{vin}_odometer                       | 总里程             |                                                                                                                                          |
| binary_sensor.{vin}_remote_door_unlock      | 远程解锁状态       | `lock.{vin}_lock` 执行“远程解锁时”会修改该状态                                                                                                          |
| binary_sensor.{vin}_sunroof                 | 天窗               |                                                                                                                                          |
| binary_sensor.{vin}_tail_gate               | 尾门               |                                                                                                                                          |



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
