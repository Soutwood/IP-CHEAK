
import requests

const = 5


def get_info(ip="127.0.0.1"):
    try:
        responce = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        print(responce)
        print("Script by Amaz1ng")
    except requests.exceptions.ConnectionError:
        print("<ERROR> Error code: 35 Print: Oh,Sorry,check YOU CONNECTION :/")


def main():
    print("The script was created for entertainment purposes, by entering the IP YOU accept responsibility for yourself")
    print("Example: 220.19.70.203")
    ip = input("Please enter a IP ;) : ")

    get_info(ip=ip)


if __name__ == "__main__":
    main()
