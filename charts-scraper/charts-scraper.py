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
    positions = [int(a.text.strip()) for a in  soup.find_all('span', class_='position') ]
    print(titles_txt)
    print(positions)
    top_100 = pd.DataFrame({
        'positions':positions,
        'artists':artists_txt,
        'titles':titles_txt
    })
    prevlink = 'https://www.officialcharts.com'+soup.find('a', text ='prev')['href']
    return top_100, chart_date, prevlink

url = 'https://www.officialcharts.com/charts/singles-chart/19521218/7501/'
chart_date=''

while '1951' not in chart_date:
    top_100, chart_date, prevlink = get_chart(url)
    print(prevlink)
    top_100.to_csv(f'charts-data/top100 {chart_date}.csv', index=False)
    url=prevlink

url = 'https://www.officialcharts.com/charts/singles-chart/19810301/7501/'
top_100, chart_date, prevlink = get_chart(url)
print(prevlink)
top_100.to_csv(f'charts-data/top100 {chart_date}.csv', index=False)