# BaiduKouBei
a spider of baidu koubei，百度口碑爬虫

爬虫思路：
1.建立百度口碑爬虫类。
初始化参数
url 爬去的机构口碑页面
https://koubei.baidu.com/s/76e0eb471cf9bd323fb1dc1717a2d451?tab=comt&page=

startpage 开始页面
endpage 结束页面
header 爬去的头部
offset 自增量，主要是页面增加

2.抽取爬去连接
从列表页面抓取到每一个评论的连接（如果从列表页面抽取文本内容，会造成抽取不完整。）

3.拿到评论连接，开始发送请求，获取响应。

4.拿到响应之后开始分析数据，提取评论

5.保存评论

6.__main__控制器




