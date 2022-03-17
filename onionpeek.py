#!/usr/bin/env python3

import time

from modules.onion import Onion
import requests

if __name__ == "__main__":
    onion = Onion()

    file = open("onion.txt", "a")
    links = []

    print("Generating onion links...")
    for i in range(1000*1000):
        links.append(onion.generate())

    session = requests.session()
    session.proxies = {}

    session.proxies["http"] = "socks5h://localhost:9050"
    session.proxies["https"] = "socks5h://localhost:9050"

    chunk = links[:100]

    while len(chunk) > 0:
        links = links[100:]

        for link in chunk:
            print("------------------------------------------------------")
            print("Checking %s" % link)

            try:
                r = session.get("%s" % link)

                if r.status_code == 200:
                    print("[+] %s" % link)
                    file.write("%s\n" % link)
                else:
                    print("[-] %s" % link)

                r.close()
            except:
                print("[-] %s" % link)

            print("------------------------------------------------------")

        chunk = links[:100]
        time.sleep(1)

    session.close()
    file.close()

    print("Done")