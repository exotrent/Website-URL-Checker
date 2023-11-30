import requests
import time


def check_url(url):
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()

        if response.status_code == 200:
            return True, end_time - start_time
        else:
            return False, None
    except Exception as e:
        return False, None


def main():
    urls = [
        "https://www.example.com",
        "https://www.google.com",
        "https://www.nonexistenturl12345.com"
        # Add more URLs to check
    ]

    for url in urls:
        status, response_time = check_url(url)

        if status:
            print(f"{url} is accessible. Response time: {response_time:.4f} seconds")
        else:
            print(f"{url} is not accessible. Maybe its down?")


if __name__ == "__main__":
    main()
