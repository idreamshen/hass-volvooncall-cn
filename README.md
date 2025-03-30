![Version](https://img.shields.io/github/v/release/idreamshen/hass-volvooncall-cn?color=green&label=Version)
[![GitHub all releases](https://img.shields.io/github/downloads/idreamshen/hass-volvooncall-cn/total?label=Downloads)](https://github.com/idreamshen/hass-volvooncall-cn/releases)
[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://github.com/hacs/integration)


# Volvo On Call CN
Homeassistant volvooncall 中国区插件

# 实体一览
`{vin}` 表示车架号
| ID                                            | 名称             | 备注                                                      |
|-----------------------------------------------|------------------|-----------------------------------------------------------|
| `lock.{vin}_lock`                             | 车锁             | 远程锁定或解锁车辆                                        |
| `binary_sensor.{vin}_engine`                  | 引擎             |                                                           |
| `switch.{vin}_engine_remote_control`          | 远程启动         | 远程启动 & 空调                                           |
| `number.{vin}_engine_duration`                | 远程启动持续时长 | 单位分钟，默认 5 分钟                                     |
| `sensor.{vin}_distance_to_empty`              | 续航里程         |                                                           |
| `binary_sensor.{vin}_front_left_door`         | 前左门           | 表示门是否打开                                            |
| `binary_sensor.{vin}_front_right_door`        | 前右门           |                                                           |
| `binary_sensor.{vin}_rear_left_door`          | 后左门           |                                                           |
| `binary_sensor.{vin}_rear_right_door`         | 后右门           |                                                           |
| `lock.{vin}_window_lock`                      | 远程窗锁         | 远程开窗或关窗（新款车型支持）                            |
| `binary_sensor.{vin}_front_left_window_open`  | 前左窗           | 表示窗是否打开, 属性`open_status_ajar`表示是否仅打开一条缝|
| `binary_sensor.{vin}_front_right_window_open` | 前右窗           |                                                           |
| `binary_sensor.{vin}_rear_left_window`        | 后左窗           |                                                           |
| `binary_sensor.{vin}_rear_right_window`       | 后右窗           |                                                           |
| `sensor.{vin}_fuel_amount`                    | 油箱剩余油量     |                                                           |
| `binary_sensor.{vin}_hood`                    | 引擎盖           | 表示引擎盖是否打开                                        |
| `sensor.{vin}_odometer`                       | 总里程           |                                                           |
| `binary_sensor.{vin}_sunroof`                 | 天窗             |                                                           |
| `binary_sensor.{vin}_tail_gate`               | 尾门             |                                                           |
| `device_tracker.{vin}_position`               | 位置             |                                                           |
| `device_tracker.{vin}_position_wgs84`         | 位置 wgs84 坐标  | 在 ha 默认地图上展示车辆时，请使用此实体                  |
| `button.{vin}_flash`                          | 闪灯             |                                                           |
| `button.{vin}_honk_and_flash`                 | 闪灯鸣笛         |                                                           |
| `button.{vin}_honk`                           | 鸣笛             |                                                           |
| `switch.{vin}_sunroof_control`                | 远程控制天窗     | 仅在遮阳帘已打开时支持远程打开天窗（新款车型支持）        |
| `switch.{vin}_tailgate_control`              | 远程控制尾箱     | 打开尾箱会同时解锁车辆,请注意及时锁车（新款车型支持）     |
| `sensor.{vin}_fuel_average_consumption_liters_per_100_km` | 百公里油耗 |                                           |
| `binary_sensor.{vin}_service_warning`              | 保养警告     |      |
| `sensor.{vin}_service_warning_msg`              | 保养警告信息     | 无需保养、未知警告、定期保养即将到期、发动机工作时间即将需要保养、行驶里程即将需要保养、定期保养时间已到、发动机工作时间保养时间已到、行驶里程保养时间已到、定期保养已逾期、发动机工作时间保养已逾期、行驶里程保养已逾期 |
| `binary_sensor.{vin}_brake_fluid_level_warning`              | 刹车液警告     |      |
| `binary_sensor.{vin}_engine_coolant_level_warningg`              | 发动机冷却液警告     |      |
| `binary_sensor.{vin}_oil_level_warning`              | 机油警告     |      |
| `binary_sensor.{vin}_washer_fluid_level_warning`              | 玻璃水警告     |      |
| `binary_sensor.{vin}_front_left_tyre_pressure_warning`              | 左前胎压警告     |      |
| `binary_sensor.{vin}_front_right_tyre_pressure_warning`              | 右前胎压警告     |      |
| `binary_sensor.{vin}_rear_left_tyre_pressure_warning`              | 左后胎压警告     |      |
| `binary_sensor.{vin}_rear_right_tyre_pressure_warning`              | 右后胎压警告     |      |


# 测试车型
- 2021 S60
- 2024 XC60

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

# 特别鸣谢
- [@chliny](https://github.com/chliny) 实现了新版车机云端协议对接
