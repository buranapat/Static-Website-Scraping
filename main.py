def get_news(symbol):
    import requests
    from bs4 import BeautifulSoup

    url = f"https://classic.set.or.th/set/companynews.do?symbol={symbol}&language=th&country=TH" 
    source = requests.get(url).text

    soup = BeautifulSoup(source,'lxml')

    maincontent = soup.find(
        "div",
        id = "maincontent"
    )

    div_row = maincontent.find(
        "div",
         class_="row"
    )

    body = div_row.findChildren(
        "div",
        class_ = "table-responsive",
        recursive = False
    )[-1].find(
          "table",
           class_ = "table table-hover table-info-wrap"
    ).findChildren(
          "tbody",
          recursive = False
    )[0] 

    rows = body.findChildren(
          "tr",
          recursive = False
    )

    lsls=[]
    for row in rows:
        cells=row.findChildren(
              "td",
               recursive = False
        )
        ls =[]

        for cell in cells:
            ls += [cell.text.replace('\n','').replace('\r','').strip()]
        lsls += [ls]

    import pandas as pd
    df = pd.DataFrame(
          lsls,
        columns=['date','','source','detail','']
    )
    df.to_excel(f'companynews_{symbol}.xlsx')
    
################################################

stocks = ['advanc','aot','ptt','scb','true'] # example stocks
for stock in stocks:
    get_news(stock.upper())
