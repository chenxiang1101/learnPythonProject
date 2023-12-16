import requests
from bs4 import BeautifulSoup

def get_movie_data(url):
    # 定义一个伪装成浏览器的 User-Agent
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
    }
    # 存储电影信息的列表
    movie_data = []
    # 循环遍历每一页
    for page in range(10):
        # 构建每一页的URL
        page_url = f'{url}?start={page * 25}'

        # 发送 GET 请求并设置 User-Agent
        response = requests.get(page_url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch the page. Status code: {response.status_code}")
            return None

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        # print(soup.prettify())

        #查找电影列表中每部电影的信息(通过div=info来查找，因为每部电影都被写在div=info的下面）
        movies = soup.find_all('div', class_='info')
        # print(movies)

        # 遍历每部电影，提取信息并添加到列表中
        for movie in movies:
            title = movie.find('span', class_='title').get_text()
            star = movie.find('span', class_='rating_num').get_text()
            # 检查是否存在引言信息(因为有些电影没有span=inq的内容（引言）
            quote_elem = movie.find('span', class_='inq')
            quote = quote_elem.get_text() if quote_elem else "No Quote"

            other_info = movie.find('div', class_='bd').get_text(strip=True)
            # 将每部电影的信息存储为一个字典，并添加到 movie_data 列表中。
            movie_data.append({
                'title': title,
                'star': star,
                'quote': quote,
                'other_info': other_info
            })

    return movie_data

def main():
    url = 'https://movie.douban.com/top250'
    movie_data = get_movie_data(url)
    # print(movie_data)

    if movie_data:
        # 打印前N电影的信息
        N=int(input("你想打印前多少部电影的信息："))
        if N <= 250:
            print("以下是前{}部电影信息：".format(N))
        else :
            N = 250
            print("这里只列出top250部的电影信息：")
        for idx, movie in enumerate(movie_data[:N], start=1):
            print(f"Movie #{idx}")
            print(f"Title: {movie['title']}")
            print(f"Star: {movie['star']}")
            print(f"Quote: {movie['quote']}")
            print(f"Other Info: {movie['other_info']}")
            print("\n")

if __name__ == "__main__":
    main()