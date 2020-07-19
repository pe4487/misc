import requests
import sqlite3
from retry import retry
from pyquery import PyQuery as pq
from collections import deque

URL = 'http://xxx/'

"""
get image from post for some site
"""
class Crawler:
    def __init__(self):
        self.q = deque()
        self.db = sqlite3.connect('.last.db')
        #self.db.execute(''' DROP TABLE last_check ''')
        self.db.execute(''' CREATE TABLE IF NOT EXISTS last_check (id int PRIMARY KEY, number int, title text) ''')

    @retry(tries=3, delay=2)
    def read_page(self, page):
        if '1' != page:
            dom = pq(url=URL + 'page/' + page)
        else:
            dom = pq(url=URL)
        self.posts = dom('div').filter('.post-meta')

    @retry(tries=3, delay=2)
    def read_dom(self, url):
        dom = pq(url)
        return dom

    def update_db(self, url, title):
        try:
            self.db.execute(" INSERT INTO last_check VALUES (?,?,?)" , (0, url, title) )
            self.db.commit()

        except sqlite3.IntegrityError:
            self.db.execute(" UPDATE last_check SET number = ?, title = ? WHERE id = 0", (url, title))
            self.db.commit()

    def get_post_link(self):
        cursor = self.db.execute(''' SELECT title FROM last_check WHERE id = 0 ''')
        last_check = cursor.fetchone()[0]
        #self.db.execute(''' DELETE FROM last_check ''')
        #self.db.commit()
        #self.db.execute(''' VACUUM ''')
        updated = False
        over = False
        page = 1
        while(not over):
            print("PAGE {}".format(page))
            self.read_page(str(page))
            for link in self.posts('h2 a').items():
                url = link('a').attr('href')
                title = link('a').attr('title')
                print(title)
                if not updated:
                    #self.update_db(url, title)
                    updated = True
                if last_check != title and page <= 1:
                    self.q.append({'url': url, 'title': title})
                else:
                    over = True
                    break
            page = page + 1

    def get_image_link(self):
        print('{} pages downloading.'.format(len(self.q)))
        count = 0
        for post in self.q:
            num = 0
            post_content = self.read_dom(post['url'])
            if post_content('.post-content > p:nth-child(2) > a > img'):
                imgs = post_content('.post-content > p:nth-child(2) > a')
                for img in imgs.items():
                    num += 1
                    self.save_img(img.attr('href'), post['title'].replace('/','-') + '_' + str(num) + '.jpg')
                count += 1
            elif post_content('.post-content > p:nth-child(1) > a > img'):
                imgs = post_content('.post-content > p:nth-child(1) > a')
                for img in imgs.items():
                    num += 1
                    self.save_img(img.attr('href'), post['title'].replace('/','-') + '_' + str(num) + '.jpg')
                count += 1
            else:
                print("not found link for {}".format(post['title']))
        print('{} pages downloaded.'.format(count))

    def save_img(self, img_url, filename):
        if 'a_site' in img_url:
            try:
                d3 = pq(img_url)
                with open(filename, 'wb') as f:
                    data = requests.get(d3('img').filter('.image-img').attr('src'))
                    f.write(data.content)
            except Exception as e:
                print(e)
                print(img_url.split('_')[1])
                pass
        elif 'b_site' in img_url:
            try:
                d3 = pq(img_url)
                with open(filename, 'wb') as f:
                    data = requests.get(d3('.image-viewer-container img').attr('src'))
                    f.write(data.content)
            except Exception as e:
                print(e)
                print(filename)
                pass
        else:
            print("there is a new img site! {}".format(img_url))

site = Crawler()
site.get_post_link()
site.get_image_link()
#from IPython import embed;embed()
