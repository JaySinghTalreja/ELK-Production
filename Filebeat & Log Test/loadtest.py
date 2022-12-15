#loadtest an api with 100000 requests
import requests
def loadTest():
    for i in range(100000):
        print(i)
        r = requests.get('http://localhost:8000/user_based_logging')
        print(r)
        print(r.json())
        # time.sleep(1)


if __name__ == '__main__':
    loadTest()





