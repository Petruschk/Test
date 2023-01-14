import requests
from bs4 import BeautifulSoup
import lxml

url = 'https://allo.ua/ua/products/notebooks/'

user = {"user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition Yx 03)"}


'https://kups.club/?page=1'
for j in range(1, 3):
    response = requests.get(url+f'?page={j}', headers=user)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")

        all_product = soup.find("div", class_="row mt-4")
        product = all_product.find_all("div", class_="col-lg-4 col-md-4 col-sm-6 portfolio-item")


        for prod in product:
            title = prod.find('h3', class_='card-title')
            price = prod.find('p', class_='card-text')
            shop_title = prod.find('p', class_='card-text text-black-50 one-line h25px mb-0')
            pr = prod.find('p', class_='card-text text-black-50 one-line mb-0')

            # print(title.text.lstrip(), end='')
            # print(price.text)

            s = str(pr)
            if s == 'None':
                continue
            else:
                c = s.rfind('"')
                n = s.rfind('=') + 2
                # print(s[n:c])

            with open('product.txt', 'a', encoding='utf-8') as file:
                file.write(f'{title.text.lstrip()}\n{price.text}\n{pr.text}{s[n:c]}\n')

                all_product = soup.find("div", class_="products-layout__container products-layout--grid")
                product = all_product.find_all("div", class_="product-card")