import requests
from bs4 import BeautifulSoup


url = "https://www.amazon.com/New-Amazon-Kindle-glare-free-adjustable/product-reviews/B0DDZQTYHL/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews"

custom_headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}


response = requests.get(url, headers=custom_headers)

soup = BeautifulSoup(response.text, 'lxml')

reviews = soup.find_all('span', {'data-hook': 'review-body'})

with open('kindle2024_reviews.txt', 'w', encoding='utf8') as review_file:
    for review in reviews:
        review_text = review.get_text(strip=True)

        review_file.write(review_text + "\n")