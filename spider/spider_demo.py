#!/usr/bin/env python
# encoding: utf-8

import os
import codecs
import requests
from bs4 import BeautifulSoup
from multiprocessing import Process, Lock  # multi-threading doesn't work well on Mac
import threading
from threading import Thread


URL = ''  # this url is leave empty intended
ERROR_LOG = "error.txt"
ERROR_LIST = []
RESULTS = {}
RESULTS_OUTPUT = "results.txt"


def format__error_print(message):
    split_line = "-"*5 + '\n'
    print split_line, message, split_line


def download_page(url):
    try:
        page = requests.get(url, timeout=10).content
        if not page:
            error_info = ["Error: empty page.", url]
            format__error_print(error_info)
        return page

    except requests.exceptions.Timeout:
        error_info = ["Error: request timeout.", url]
        format__error_print(error_info)
        return None


def parse_html(url):

    html = download_page(url)

    if not html:
        return []

    soup = BeautifulSoup(html)

    try:
        # find names on page.
        return [brfs_name.getText().strip() for brfs_name in soup.find_all('span', attrs={'itemprop':'name'})]
    except Exception as e:
        error_info = ["html Error:", e.message]
        format__error_print(error_info)
        return []


def process_unit(url, id, result_lock=None, error_lock=None):
    single_result = parse_html(url)
    # if single_result:
    # result_lock.acquire()
    # RESULTS[id] = single_result
    # print RESULTS
    write_file(id, single_result)
    print id, '',  # progress info
    # result_lock.release()
    # else:
    #     error_lock.acquire()
    #     ERROR_LIST.append()
    #     error_lock.release()


def write_file(filename, content):
    with codecs.open(os.path.join("results", str(filename)), 'wb', encoding='utf-8') as f:
        f.write("\n".join(content))


# todo: change parameter names
def run_in_parallel(p_list, concurrency=20):
    # Thread and Process have the same methods,
    # so this function can serve them both.
    count = 0
    running_list = []

    for p in p_list:
        while count >= concurrency:
            for process in running_list:
                process.join(1)
                if not process.is_alive():
                    running_list.remove(process)
                    count -= 1
        p.start()
        running_list.append(p)
        count += 1

    while running_list:
        for p in running_list:
            p.join(1)
            if not p.is_alive():
                running_list.remove(p)


def multi_processing():
    if not os.path.isdir("results"):
        os.mkdir("results")

    # condition is: page url is already know, no need to iterate by "next page" navigation.
    # create one process instance for each page
    start_page = 1
    end_page = 21
    result_lock = Lock()
    p_list = [Process(target=process_unit, args=(URL.format(num), num, result_lock))
              for num in xrange(start_page, end_page)]

    run_in_parallel(p_list=p_list, concurrency=10)


def multi_threading():
    global ERROR_LIST, ERROR_LOG, RESULTS_OUTPUT
    start_page = 1
    end_page = 401
    result_lock = threading.Lock()
    error_lock = threading.Lock()
    t_list = [Thread(target=thread_unit, args=(URL.format(num), num, result_lock, error_lock))
              for num in xrange(start_page, end_page)]

    run_in_parallel(p_list=t_list, concurrency=50)

    with codecs.open(RESULTS_OUTPUT, "w", encoding="utf-8") as f:
        for index in xrange(start_page, end_page):
            f.write("\n".join(RESULTS[index]) + "\n")
    if ERROR_LIST:
        print "\nErrors: ", ", ".join(ERROR_LIST)
        with open(ERROR_LOG, 'w') as f:
            f.write("\n".join(ERROR_LIST))


def thread_unit(url, index, result_lock=None, error_lock=None):
    global RESULTS, ERROR_LIST

    single_result = parse_html(url)

    result_lock.acquire()
    RESULTS[index] = single_result
    result_lock.release()
    print index, '',  # progress info

    if not single_result:
        error_lock.acquire()
        ERROR_LIST.append(str(index))
        error_lock.release()


if __name__ == '__main__':
    # multi_processing()
    multi_threading()
