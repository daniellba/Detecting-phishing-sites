from bs4 import BeautifulSoup

import urllib.request as req
import requests
import re
import ssl
import socket


# Uncover the link in case it is shortened link
def unshorten_url(url):
    try:
        response = requests.get(url)
        print('\n--------------------------------------------------------------')
        print(f"Uncovered url- \n{response.url}")
        print('--------------------------------------------------------------\n')
        return response.url
    except Exception as e:
        print(f'Bad url {url}.\n{e}')
        exit()


# Checking the response status of the url
def url_response_status(url):
    print("url connection- " + str(url.getcode()))
    if url.getcode == 404:
        print("Web page did not find.")
        exit()


# check if the url contains special characters (% decoding method)
def check_special_signs(url):
    if '@' or '%' or '#' in url:
        print("The URL contains special characters.")
    else:
        print("The url doesn't contain special characters.")
    # reg expression - need to check it and print something
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        # domain...
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'  # localhost...
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$)', re.IGNORECASE)
    print(re.match(regex, url) is not None)  # True


# checking how many dots there are
def dots_counter(url):
    url = url.split('.')
    if len(url) > 4:
        print("The url has 5 dots or more.")
        return True
    return False


# writing the url's HTML into 'f'
# Another way to detect a phishing site is to check HTML tags
def scrapping(url):
    f = requests.get(url)
    if '<script>' or '<head>' in f.text:
        print('Site contains the word "script"')
        return True

    # Another way to locate code parts in HTML (scraping)
    soup = BeautifulSoup(f.text, 'html.parser')
    if soup.findAll('<input type="submit" value="Submit">'):
        print('Found submit button.')
        return True
    else:
        print('Did not find submit.')
        return False


# checking url length
def url_length(url):
    f = len(url)
    print(f"url length {f}")
    if f > 150:
        return True
    return False


# check if the url is an IP address using regular expression
def is_ip(url):
    reg = re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", url)
    if reg is None:
        print('URL is not an IP format.')
        return True
    else:
        print('URL is an IP format.')
        return False


# checking if the site has ssl certificate
def ssl_certificate_check(url):
    host = url.split("https://", 1)[1].strip('/')
    context = ssl.create_default_context()
    port = 443
    try:
        with socket.create_connection((host, port)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                return is_valid_ssl(ssock.getpeercert())
    except Exception as e:
        print(e)
        return False


# check if the ssl certificate is vaild
def is_valid_ssl(ssock):
    start_date = _transfer_date_to_timestamp(ssock.get("notBefore", ''))
    end_date = _transfer_date_to_timestamp(ssock.get("notAfter", ''))
    current_date = datetime.now().timestamp()
    if start_date < current_date < end_date:
        return True
    return False


# calculating the expiration date of the
# certificate in order to compare it to the current date.
def transfer_date_to_timestamp(date):
    return datetime.strptime(date.strip(" GMT"), "%b %d %H:%M:%S %Y").timestamp()
