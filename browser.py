import sys
import os
import requests
import bs4
from colorama import init, Fore

# write your code here

init(autoreset=True)
white_list = ('.com', '.org')
allowed_tags = ('p', 'a', 'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6')


def parse_html_pages(page):
    html_page_soup = bs4.BeautifulSoup(page, 'html.parser')
    content = []
    for item in html_page_soup.find_all(allowed_tags):
        if item.name == 'a':
            content.append(Fore.BLUE + item.get_text())
        else:
            content.append(str(item.get_text()))
    return content


def show_web_page_from_file(dir_name, page):
    with open(f'./{dir_name}/{page}.txt') as web_page:
        for item in web_page:
            print(item)


def show_web_page_from_url(page):
    content = parse_html_pages(page)
    for item in content:
        print(item)


def save_web_page(url, page):
    url_name = url.split('.')[0]
    page = parse_html_pages(page)
    if len(sys.argv) == 2:
        dir_name = sys.argv[1]
        if not os.path.exists(dir_name):
            os.mkdir(dir_name)
        with open(f'./{dir_name}/{url_name}.txt', 'w') as webpage:
            webpage.writelines(page)


def url_checker(url):
    if '.' not in url:
        print('error')
        return False
    return True


def web_page_name_checker(page):
    if page in os.listdir():
        return True
    return False


def make_request(url):
    url = 'https://' + url
    response = requests.get(url)
    if response:
        return response.text
    else:
        print('error')
        return False


while True:
    url_or_page_name = input()
    page = ''
    dir_name = ''
    if len(sys.argv) == 2:
        dir_name = sys.argv[1]
    if url_or_page_name == 'exit':
        break

    if url_checker(url_or_page_name):
        url = url_or_page_name
        page = make_request(url)
        show_web_page_from_url(page)
        if len(sys.argv) == 2 and page:
            save_web_page(url, page)
    else:
        if web_page_name_checker(url_or_page_name):
            url_without_the_dot = url_or_page_name.split('.')[0]
            show_web_page_from_file(dir_name, url_without_the_dot)

