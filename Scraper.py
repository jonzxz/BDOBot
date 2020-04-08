from bs4 import BeautifulSoup
import requests


class Scraper:
    # Constructor
    def __init__(self):
        self.headers = requests.utils.default_headers()
        self.initialization()

    # Function to update the headers to imitate a browser
    def initialization(self):
        self.headers.update({
            'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',
        })

    # Function that returns a list of ingredients in the form of [Name(Count)]
    # Algorithm to be reimplemented using Selenium, scraping from BDOCodex and such, unless I can implement
    # suggestions logic with this algo, this logic has to be redone regardless.
    def create_data(self, name):
        url = "https://www.bdodae.com/items/index.php?item=" + name
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.content, 'lxml')
        raw_ingredients = []
        first = soup.find_all("div", {"class": "ing1_box"})
        for x in first:
            second = x.find_all("div", {"class": "ing1_item"})
            for y in second:
                raw_data = y.find_all("a", {"class": "item_popup"})
                for item in raw_data:
                    if "(" and ")" in item.contents[0]:
                        raw_ingredients.append(item.contents[0])
        return raw_ingredients

    # Function that returns a list of ingredients in the form of [Count Name] i.e. 5 Wheat.
    def generate_results(self, name, multiples):
        name = self.clean_word(name)
        list = self.create_data(name)
        final = []
        for ingredient in list:
            count = self.clean_number(ingredient.split()[-1])
            name = self.remove_number(ingredient)
            count = int(count) * int(multiples)
            formatted = str(count) + " " + name
            final.append(formatted)
        return final

    def print_ingredients(self, item):
        input = item.replace('%', '')
        if self.isdigit(input.split()[0]):
            space = ' '
            result = self.generate_results(space.join(input.split()[1:]), input.split()[0])
        else:
            input = self.clean_word(input)
            result = self.generate_results(input, 1)

        return result

    # -- Helper functions
    # Function to remove ( and )
    def clean_number(self, number):
        return number.replace("(", "").replace(")", "")

    # Function to clean up string in the format of bdodae's url format
    # i'll have to rework this sooner or later
    def clean_word(self, word):
        return word.strip().replace(": ", "-").replace(" ", "_").replace("'", "")

    def isdigit(self, word):
        return word.isdigit()

    def remove_number(self, word):
        return ' '.join(word.split(' ')[:-1])


    def get_all_recipes(self, type):
        url = "https://www.bdodae.com/items/index.php?cat=" + type
        r = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(r.content, 'lxml')
        full_list = []
        all_items = soup.find_all("div", {"class" : "sort_cooking"})
        for item in all_items:
            div_name = item.find_all("div", {"class": "link_title"})
            for name in div_name:
                full_list.append(name.find("a").contents[0])
        return full_list
        #return '```{}```'.format(full_list)
