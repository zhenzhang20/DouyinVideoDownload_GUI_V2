---

---

DYDownloader是一个简单的界面化下载指定抖音up主所有视频的程序。使用者超过100人后，将公开源码~~

### 下载演示

![download_demo](https://github.com/zhenzhang20/zhenzhang20.github.io/tree/master/2020/08/25/2020-08-25-Douyin-Downloader/2020-08-25-download_demo.gif)



[下载地址](https://pan.baidu.com/s/1nhSxX05rcaETFG1oPc3oPg )  提取码：1234

![panbaidu_download_qr](https://github.com/zhenzhang20/zhenzhang20.github.io/tree/master/2020/08/25/2020-08-25-Douyin-Downloader/2020-08-25-panbaidu_download_qr.png)





### 安装运行环境

1. 安装[Python3.7](https://www.python.org/downloads/release/python-377/)

1. 安装本项目依赖库

```
pip install requirements.txt
```

如果安装失败，请多次尝试或更换网络环境进行安装。

### 程序使用方法

1. 使用Python打开DYDownloader程序。

```
python Download.pyc
```

1. 正常启动后，界面为： 

   ![dy_downloader_main_window](https://github.com/zhenzhang20/zhenzhang20.github.io/tree/master/2020/08/25/2020-08-25-Douyin-Downloader/2020-08-25-dy_downloader_main_window.png)

2. 点击界面右上角“开启本地服务”来打开所需服务

本程序使用了Chrome浏览器内核进行模拟访问。首次使用时，会下载安装相应的文件，该过程在不同网络状态下，可能会比较慢，也可能安装失败。失败信息：

```
[WinError 10060] 由于连接方在一段时间后没有正确答复或连接的主机没有反应,连接尝试失败。
```

如果自动安装失败，可以手动进行安装。安装方法： 从[googleapis官方](https://storage.googleapis.com/chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip)或者 [淘宝镜像网站](https://npm.taobao.org/mirrors/chromium-browser-snapshots/Win_x64/575458/chrome-win32.zip)下载575458版本的chrome-win32.zip

下载后，解压缩到下述目录：

```
C:\Users\Name\AppData\Local\pyppeteer\pyppeteer\local-chromium\575458\chrome-win32
```

其中Name根据实际情况修改，替换为当前电脑用户名称。 解压后内容如下：

![chrome_to_pyppeteer](https://github.com/zhenzhang20/zhenzhang20.github.io/tree/master/2020/08/25/2020-08-25-Douyin-Downloader/2020-08-25-chrome_to_pyppeteer.png)



6. 重新运行DYDownloader程序，并启动服务，服务正常启动后，显示如下信息（最后一行信息会持续输出） 2020-08-25-start_service_success.png

7. 点击“URL”进行下载链接(用户分享链接)设置

```
https://v.douyin.com/tSsdJ1/
https://v.douyin.com/wS4Sr9/
https://v.douyin.com/wSGSg9/
https://v.douyin.com/wSQudo/
https://v.douyin.com/wSw9qV/
https://v.douyin.com/wSQunG/
https://v.douyin.com/wSwxG1/
https://v.douyin.com/wStLr8/
https://v.douyin.com/wSKqMr/
```

获取用户分享链接的方法: 直接在抖音分享，然后复制连接发送到qq或微信或者自己粘贴出来即可。

8. 点击“开始”进行下载

9. 点击“下载结果”打开视频存储路径

10. 程序需要license执行（免费申请），请发送您的机器物理地址到 [zhen_zhang20@163.com](http://mailto:zhen_zhang20@163.com) 或进行申请，邮件标题为“抖音下载许可申请，或者微信联系我进行申请。 

    ![mac_address_message](https://github.com/zhenzhang20/zhenzhang20.github.io/tree/master/2020/08/25/2020-08-25-Douyin-Downloader/2020-08-25-mac_address_message.png)

11. 一些说明：

- 程序没有暂停功能，如需中途停止，直接关闭
- 下载过程中，“开始”按钮会变为“下载中...”，下载完成后，自动恢复为“开始”
- 目前支持“下载路径”、‘下载失败重复次数’、“连接超时“、“定制报头信息”设置
- 不支持“线程数”设置（即不支持多线程下载）

### 联系我

如果你对该程序感兴趣，可以扫码下面的二维码勾搭申请加入群聊。

 ![share_wechart_qr](https://github.com/zhenzhang20/zhenzhang20.github.io/tree/master/2020/08/25/2020-08-25-Douyin-Downloader/2020-08-25-share_wechart_qr.png)

### 致谢

* 本文受到[wangshub/Douyin-Bot](https://github.com/wangshub/Douyin-Bot/) 和 [hokaso/douyin2bilibili](https://github.com/hokaso/douyin2bilibili) 启发而生

* 感谢 [coder-fly/douyin-signature](https://github.com/coder-fly/douyin-signature) 及 很多微信上提供过信息的小伙伴。



### 声明

* 如有侵权，请联系进行删除，谢谢





[View Blog](https://zhenzhang20.github.io/2020/08/25/2020-08-25-Douyin-Downloader)