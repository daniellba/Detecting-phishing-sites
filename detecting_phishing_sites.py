from datetime import datetime
import urllib.request as req
import common
import time
import socket

start_time = time.time()


def main():
    grading_system = {
        "ssl_check": 30,
        "scrapping": 20,
        "uncovered_url": 5,
        "check_special_signs": 10,
        "dots_counter": 10,
        "url_length": 5,
        "is_ip": 5
    }

    count = 0
    url = input("Insert url for check:")

    # examples
    # url = 'http://en.wikipedia.org/wiki/%22@%22_%28album%29'
    # http://buff.ly/1irhfHu

    uncovered_url = common.unshorten_url(url=url)
    if uncovered_url is not url:
        count += grading_system['uncovered_url']

    common.url_response_status(url=req.urlopen(uncovered_url))

    if common.check_special_signs(url=uncovered_url) is False:
        count += grading_system['check_special_signs']

    if common.dots_counter(url=uncovered_url) is True:
        count += grading_system['dots_counter']

    if common.scrapping(url=uncovered_url) is True:
        count += grading_system['scrapping']

    if common.url_length(url=uncovered_url) is True:
        count += grading_system['url_length']

    if common.is_ip(url=uncovered_url) is True:
        count += grading_system['is_ip']

    if "https://" in url:
        common.ssl_certificate_check(uncovered_url)
    else:
        count += grading_system['ssl_check']

    # run time of the program
    print('\n---------------------')
    print(f'Run time {time.time() - start_time:.2f} seconds')
    print('---------------------')
    print(f'Website grade: {count}')
    print('Above 50 the website is safe.')


if __name__ == '__main__':
    main()
