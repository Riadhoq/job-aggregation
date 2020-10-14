from bs4 import BeautifulSoup
import requests

if __name__ == "__main__":

    url = f"https://www.linkedin.com/jobs/search?keywords=Software%20Engineering&location=Atlan&redirect=false&position=1&pageNum=0"

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    result_cards = soup.select('.result-card.job-result-card')

    for result_card in result_cards:
        
        result = { 
            "data-id" : result_card['data-id'],
            "link" : result_card.select('.result-card__full-card-link')[0]['href'],
            "image" : result_card.select('.result-card__image')[0]['data-delayed-url'],
            "title" : result_card.select('.result-card__title')[0].get_text(),
            "company_link" : result_card.select('.result-card__subtitle-link')[0]['href'],
            "company_name" : result_card.select('.result-card__subtitle-link')[0].get_text(),
            "location" : result_card.select('.job-result-card__location')[0].get_text(),
            "listdate" : result_card.select('time')[0]['datetime'],
        }

        print(result.values())