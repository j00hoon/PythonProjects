import requests
from bs4 import BeautifulSoup
import smtplib


TARGET_PRICE = 200
url = "https://www.amazon.com/Instant-Pot-Ultra-Programmable-Sterilizer/dp/B06Y1MP2PY/ref=dp_fod_3?pd_rd_w=zJ9QN&content-id=amzn1.sym.8ec84471-8e07-456a-83de-89571ec52fe8&pf_rd_p=8ec84471-8e07-456a-83de-89571ec52fe8&pf_rd_r=3G76S2K3MESABEKA13ZS&pd_rd_wg=tsHFQ&pd_rd_r=39a27bed-eb62-4548-8f0b-abc1e2562c54&pd_rd_i=B06Y1MP2PY&psc=1"

# Get a price of product
response = requests.get(url=url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0", "Accept-Language": "en-US,en;q=0.5"})
amazon_product_page = response.text

soup = BeautifulSoup(amazon_product_page, "html.parser")
product_price_html = soup.find(name="span", class_="a-offscreen")
product_price = float(product_price_html.getText().split("$")[1])


if product_price < TARGET_PRICE:
    # Sending email
    EMAIL = "j00hoon1101@gmail.com"
    PASSWORD = "btpygqgeztdqczhl"
    "STN.SXF.2020-08-25*SXF.STN.2020-09-08"
    MESSAGE = f"The product price is {product_price}.\n It is lower than our target price which is {TARGET_PRICE}!!!"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="j00hoon1101@gmail.com",
            msg=f"Subject: Check out your target price!!\n\n {MESSAGE}"
        )