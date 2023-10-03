# Table of Contents

1.  [Volvo On Call CN](#orgf1baa5f)
2.  [实体一览](#org454eeb3)
3.  [开发中](#org25d0973)
4.  [测试车型](#org75825a1)
5.  [HACS 安装集成](#org8df6d42)
6.  [Homeassistant 添加集成](#orga196806)

<div class="html" id="org87f1223">
<p>
&lt;a href="<a href="https://github.com/idreamshen/hass-volvooncall-cn/releases">https://github.com/idreamshen/hass-volvooncall-cn/releases</a>"&gt;
&lt;img alt="" src="<a href="https://img.shields.io/github/v/release/idreamshen/hass-volvooncall-cn?color=green&amp;label=Version">https://img.shields.io/github/v/release/idreamshen/hass-volvooncall-cn?color=green&amp;label=Version</a>" /&gt;
&lt;/a&gt;
</p>

</div>

<div class="html" id="orgcdde9ba">
<p>
&lt;a href="<a href="https://github.com/idreamshen/hass-volvooncall-cn/releases">https://github.com/idreamshen/hass-volvooncall-cn/releases</a>"&gt;
&lt;img alt="" src="<a href="https://img.shields.io/github/downloads/idreamshen/hass-volvooncall-cn/total?label=Downloads">https://img.shields.io/github/downloads/idreamshen/hass-volvooncall-cn/total?label=Downloads</a>" /&gt;
&lt;/a&gt;
</p>

</div>

<div class="html" id="orgcaa137d">
<p>
&lt;a href="<a href="https://github.com/hacs/integration">https://github.com/hacs/integration</a>"&gt;
&lt;img alt="" src="<img src="https://img.shields.io/badge/HACS-Custom-41BDF5.svg" alt="HACS-Custom-41BDF5.svg" class="org-svg" />" /&gt;
&lt;/a&gt;
</p>

</div>


<a id="orgf1baa5f"></a>

# Volvo On Call CN

Homeassistant volvooncall 中国区插件


<a id="org454eeb3"></a>

# 实体一览

`{vin}` 表示车架号

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">ID</th>
<th scope="col" class="org-left">名称</th>
<th scope="col" class="org-left">备注</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">lock.{vin}<sub>lock</sub></td>
<td class="org-left">车锁</td>
<td class="org-left">可以远程锁定或解锁车辆。远程解锁，会变更 <code>binary_sensor.{vin}_remote_door_unlock</code> 的状态；远程锁定：变更 <code>binary_sensor.{vin}_lock</code> 状态</td>
</tr>


<tr>
<td class="org-left">sensor.{vin}<sub>distance</sub><sub>to</sub><sub>empty</sub></td>
<td class="org-left">续航里程</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>lock</sub></td>
<td class="org-left">车锁状态</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>front</sub><sub>left</sub><sub>door</sub></td>
<td class="org-left">前左门</td>
<td class="org-left">表示门是否打开</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>front</sub><sub>right</sub><sub>door</sub></td>
<td class="org-left">前右门</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>rear</sub><sub>left</sub><sub>door</sub></td>
<td class="org-left">后左门</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>rear</sub><sub>right</sub><sub>door</sub></td>
<td class="org-left">后右门</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>front</sub><sub>left</sub><sub>window</sub><sub>open</sub></td>
<td class="org-left">前左窗</td>
<td class="org-left">表示窗是否打开</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>front</sub><sub>right</sub><sub>window</sub><sub>open</sub></td>
<td class="org-left">前右窗</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>rear</sub><sub>left</sub><sub>window</sub></td>
<td class="org-left">后左窗</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>rear</sub><sub>right</sub><sub>window</sub></td>
<td class="org-left">后右窗</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">sensor.{vin}<sub>fuel</sub><sub>amount</sub></td>
<td class="org-left">油箱剩余油量</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">sensor.{vin}<sub>fuel</sub><sub>amount</sub><sub>level</sub></td>
<td class="org-left">油箱剩余油量百分比</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>hood</sub></td>
<td class="org-left">引擎盖</td>
<td class="org-left">表示引擎盖是否打开</td>
</tr>


<tr>
<td class="org-left">sensor.{vin}<sub>odometer</sub></td>
<td class="org-left">总里程</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>remote</sub><sub>door</sub><sub>unlock</sub></td>
<td class="org-left">远程解锁状态</td>
<td class="org-left"><code>lock.{vin}_lock</code> 执行“远程解锁时”会修改该状态</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>sunroof</sub></td>
<td class="org-left">天窗</td>
<td class="org-left">&#xa0;</td>
</tr>


<tr>
<td class="org-left">binary<sub>sensor</sub>.{vin}<sub>tail</sub><sub>gate</sub></td>
<td class="org-left">尾门</td>
<td class="org-left">&#xa0;</td>
</tr>
</tbody>
</table>


<a id="org25d0973"></a>

# 开发中

-   [X] 远程开锁
-   [X] 远程关锁
-   [ ] 远程启动空调
-   [ ] 远程关闭空调


<a id="org75825a1"></a>

# 测试车型

-   2021 S60


<a id="org8df6d42"></a>

# HACS 安装集成

HACS -> 集成 -> 右上角三个点 -> 自定义存储库

-   存储库：<https://github.com/idreamshen/hass-volvooncall-cn>
-   类别：集成

浏览并下载存储库 -> 搜索 Volvo On Call CN 并下载


<a id="orga196806"></a>

# Homeassistant 添加集成

设置 -> 设备与服务 -> 添加集成 -> 搜索品牌 Volvo On Call CN -> 填入手机号和密码

-   手机号：11 位纯数字
-   密码：即“沃尔沃APP”上的登录密码，需要提前设置好登录密码

提交稍等片刻后，即可看到拥有的车辆设备
