!pip install google-play-scraper
import pandas as pd
import csv
from google_play_scraper import app, reviews, Sort, reviews_all

scrapreview = reviews_all(
    'com.shopeepay.id',
    lang='id',
    country='id',
    sort=Sort.MOST_RELEVANT,
    count=10500
)

with open('ulasan_shopee_pay.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Review'])
    for review in scrapreview:
        writer.writerow([review['content']])

spay_df = pd.DataFrame(scrapreview)
spay_df.shape
spay_df.head()
spay_df.to_csv('ulasan_shopee_pay.csv', index=False)

# Membuat DataFrame dari hasil scrapreview
spay_df = pd.DataFrame(scrapreview)

