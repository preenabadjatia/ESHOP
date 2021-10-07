import requests
from bs4 import BeautifulSoup
headers = {
    'authority': 'fls-eu.amazon.in',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'sec-fetch-site': 'same-site',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-dest': 'image',
    'referer': 'https://www.amazon.in/',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cookie': 'session-id=257-4247507-9937119; i18n-prefs=INR; ubid-acbin=262-8608688-4855337; session-token=hsOPaGeCQGTWi8r2353ceTvhc4fXSAUJAtE0GViXh8SzAyxs8yCOEJhPDzKXbDgM9J3XacyKq+KSE//CgtrnmhPIHQNAOztU20Jf/7VgKu1kwgiRSWe6nXq95As/AiiwAYJLibGJV3YRShWvOL9crADporbBr55EZe5/9pNq/WbtpD6sAbM2Eke8GRmb2qJmtlvw5cRi6ryn0ZkVVp3+/a8cGFj+nCdwUEbW/tCJy1eQcKwErdSKKtlJCj1ADT4t; session-id-time=2082758401l; visitCount=3',
}
url='https://www.amazon.in/Vills-Laurrens-Black-Wrist-VL-1114/dp/B08B3FT6X4/ref=sr_1_1_sspa?dchild=1&fst=as%3Aoff&pf_rd_i=2563504031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=4b4e67a6-350d-41ce-ad9e-66e1aa6b3c0b&pf_rd_r=414PHAS4RC5XRWTST2A5&pf_rd_s=merchandised-search-8&pf_rd_t=30901&qid=1630496489&refinements=p_n_feature_seven_browse-bin%3A1480900031&rnid=1350388031&s=watch&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTE5ESkwzOTJMWUZMJmVuY3J5cHRlZElkPUEwMTcxODQ0M1E5MjdNTlo1UlYzQSZlbmNyeXB0ZWRBZElkPUExMDQ3NDU3MThYSVU5WExDSzREVCZ3aWRnZXROYW1lPXNwX2F0Zl9icm93c2UmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl'

res=requests.get(url=url,headers=headers)
soup = BeautifulSoup(res.content,u'html.parser')
print(soup.find('span',attrs={'id':'priceblock_ourprice'}).text.strip())