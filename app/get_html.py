import requests
from bs4 import BeautifulSoup

def amazon(link):
	url = link
	flag=0
	count=0
	while(flag!=1):
		try:
			amalist = []
			response = requests.get(url)
			soup = BeautifulSoup(response.content, 'lxml')

			#タイトル取得
			amalist.append(soup.title.string)
			#画像リンク取得
			amalist.append(soup.find('img', class_="a-dynamic-image").get('src'))
			#amazonのカテゴリすべて取得
			for tag in soup.find('ul', class_="a-unordered-list").findAll('li'):
				amalist.append(tag.text.strip())

			#amazonからデータが取れていないときは以下のテキストが出るから、出てなければループ抜け
			if(amalist[0]!= "Amazon CAPTCHA"):
				flag=1



		except (ZeroDivisionError, TypeError, AttributeError) as e:
			count+=1
			#30回繰り返してみて無理なら諦め。後々時間を空けてからお試しください的なページを作って遷移する
			if(count>30):
				if(len(amalist)):
					amalist[0] = "sippai"
				else:
					amalist.append("sippai")
				flag=1
			pass
	return amalist











