kospi_top10 = ['삼성전자', 'SK하이닉스', '현대차', '한국전력', '아모레퍼시픽', '제일모직', '삼성전자우', '삼성생명', 'NAVER', '현대모비스']
kospi_top10.append("SK텔레콤")

print(len(kospi_top10))

# remove specific item in the list using by 'del' keyword
del kospi_top10[-1]

print(len(kospi_top10))
print(kospi_top10)