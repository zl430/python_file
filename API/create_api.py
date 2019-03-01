import mysql.connector
from bs4 import BeautifulSoup
mydb = mysql.connector.connect(host="10.113.4.189", user="root", passwd="123456", port="66", database="py_test")
mycursor = mydb.cursor()
mycursor.execute("DROP TABLE IF EXISTS meizi_meizis")
createTab = "create table meizi_meizis(id int primary key auto_increment,mid varchar(10) not null,title varchar(50),picname varchar(10),page_url varchar(50),img_url varchar(50));"
mycursor.execute(createTab)
def html(self, href, title):
    lists = []
    meiziid = href.split('/')[-1]
    html = self.request(href)
    max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
    for page in range(1, int(max_span) + 1):
        meizi = {}
        page_url = href + '/' + str(page)
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        picname = img_url[-9:-4]
        meizi['meiziid'] = meiziid
        meizi['title'] = title
        meizi['picname'] = picname
        meizi['page_url'] = page_url
        meizi['img_url'] = img_url
        lists.append(meizi) # 保存到返回数组中
        return lists
def all_url(self, url):
    html = self.request(url)
    all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
    for index, a in enumerate(all_a):
        title = a.get_text()
        href = a['href']
        lists = self.html(href, title)
        for i in lists:
            # print(i['meiziid'], i['title'], i['picname'], i['page_url'], i['img_url'])
            # 插入数据到数据库sql语句，%s用作字符串占位
            sql = "INSERT INTO meizi_meizis(mid,title,picname,page_url,img_url) VALUES(%s,%s,%s,%s,%s)"
            try:
                mycursor.execute(sql, (i['meiziid'], i['title'], i['picname'], i['page_url'], i['img_url']))
                mydb.commit()
                print(i[0] + " is success")
            except:
                mydb.rollback()
            mydb.close() # 关闭数据库



#https://m.jb51.net/article/141674.htm