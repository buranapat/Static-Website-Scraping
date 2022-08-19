# Static-Website-Scraping
### Static Web Scraping 
### from Intermediate Data Engineering Workshop
### by P' Isarapong Eksinchol, PhD (GBDi)
---
### Scrape company news from SET (The Stock Exchange of Thailand) using `requests` and `BeautifulSoup`.

## Workflow
1. Import `requests` and `BeautifulSoup` library.
2. Get `HTML` code from company news webpage and turn in to `txt`
3. Inspect `HTML` code from that webpage to find the part of the company news
4. Turn `txt` to `BeautifulSoup` object to distill data and get the company news
5. Transform company news to `pandas DataFrame` to export in form of Excel

