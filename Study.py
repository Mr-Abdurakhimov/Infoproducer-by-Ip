import requests


def get_info_by_IP(ip):
    try:
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()
        data = {
            "[IP]": response['query'],
            '[Country]': response['country'],
            '[City]': response['city'],
            '[Zip]': response['zip'],
            '[Latitude]': response['lat'],
            '[Longitude]': response['lon'],
        }
        for k, v in data.items():
            print(f"{k} : {v}")
    except requests.exceptions.ConnectionError:
        print('Something went wrong,check your connections')


def main():
    ip = input('Enter the IP address: ')
    get_info_by_IP(ip)


if __name__ == '__main__':
    main()
