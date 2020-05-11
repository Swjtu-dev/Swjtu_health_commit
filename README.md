# Swjtu_health_commit
Swjtu 每日健康签到
基于python3 
需配合charles等抓包软件食用
MacOS及Linux请使用_linux后缀版
Windiws请使用无后缀版


## 抓包教程（charles）
开启charles，进入打卡网站，按正常流程进行一次打卡  
按下图进行数据提取：  
![image](https://github.com/Swjtu-dev/Swjtu_health_commit/blob/master/pic/ttt.png)

## 各文件作用
### data文件夹内含文件

文件名 | 作用
:-----:|:-----:|
*.hel | 用户参数文件（见下表）

#### *.hel文件参数

行号 | 参数
:-----:|:-----:|
1 | 学号
2 | 姓名
3 | 身份证后六位
4 | 爬取的信息

### status文件夹内含文件

文件名 | 作用
:-----:|:-----:|
*.sta | 打卡状态文件
- 此文件名与*.hel文件名对应
- 打卡成功后自动写入当前日期
- 若此文件存在且内部日期为当前日期，则停止打卡
- 重复打卡需删除此文件
