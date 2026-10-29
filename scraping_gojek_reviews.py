"""
Kode Scraping Review Aplikasi Gojek dari Google Play Store

Output:
- gojek_reviews_raw.csv
"""

import pandas as pd
from google_play_scraper import Sort, reviews


APP_ID = "com.gojek.app"
JUMLAH_DATA = 8000
OUTPUT_FILE = "gojek_reviews_raw.csv"


def scrape_gojek_reviews(app_id=APP_ID, jumlah_data=JUMLAH_DATA):
    result, continuation_token = reviews(
        app_id,
        lang="id",
        country="id",
        sort=Sort.NEWEST,
        count=jumlah_data,
        filter_score_with=None
    )

    df = pd.DataFrame(result)
    return df


if __name__ == "__main__":
    print("Mulai scraping review Gojek dari Google Play Store...")
    df_reviews = scrape_gojek_reviews()

    print(f"Jumlah data hasil scraping: {len(df_reviews)}")

    df_reviews.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

    print(f"Dataset berhasil disimpan sebagai {OUTPUT_FILE}")