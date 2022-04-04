import requests
import bs4
import pandas as pd

def get_chart(url):
    print(url)
    req=requests.get(url)
    soup = bs4.BeautifulSoup(req.text,'html')
    chart_date = soup.find_all('p', class_='article-date')[0].text.split('-')[0].strip()
    artists_txt = [a.text.strip() for a in  soup.find_all('div', class_='artist') ]
    titles_txt = [a.text.strip() for a in  soup.find_all('div', class_='title') ]
    print(titles_txt)
    top_100 = pd.DataFrame({
        'positions':range(1,101),
        'artists':artists_txt,
        'titles':titles_txt
    })
    prevlink = 'https://www.officialcharts.com'+soup.find('a', text ='prev')['href']
    return top_100, chart_date, prevlink

url = 'https://www.officialcharts.com/charts/singles-chart/20220325/7501/'
chart_date=''

while '1952' not in chart_date:
    top_100, chart_date, prevlink = get_chart(url)
    print(prevlink)
    top_100.to_csv(f'charts-data/top100 {chart_date}.csv', index=False)
    url=prevlink

