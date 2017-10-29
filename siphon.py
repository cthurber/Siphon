import time
from sys import argv
from retrieve import save_page
from multiprocessing import Pool

# Retrieves URLs from text file
def get_urls(filename):
    urls = []

    with open(filename, 'r') as url_list:
        for url in url_list:
            urls.append(url.replace('\n',''))

    return urls

def main():
    args = argv[1:]
    if "help" in args or "-h" in args or len(args) < 1:
        print("\ncollect.py should be run as follows:")
        print("collect.py <urls> <destination>")
        print("\t-urls: Text file containing urls of pages to download")
        print("\t-destination: Path where pages should be saved\n")

    urls = get_urls(args[0])

    if len(args) > 1:
        path = args[1]
    else:
        path = "./data"

    start_time = time.time()
    pool = Pool(processes=16)
    pool.map(partial(save_page, location=path), urls)

    print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == "__main__":
    main()
