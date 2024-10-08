import requests
import csv

def fetch_and_print_posts():
    """
    Function for fetch data from a specific url and print it in output
    """
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print('Status Code:', r.status_code)
    if r.ok:
        r = r.json()
        for item in r:
            for key, value in item.items():
                if key == "title":
                    print(value)

def fetch_and_save_posts():
    """
    Function for fetch data from a specific url and save it into a CSV file
    """
    data = []
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.ok:
        json_data = r.json()
        for item in json_data:
            data.append(dict(id = item['id'], title = item['title'], 
            body = item['body']))

    with open('posts.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'title', 'body']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow({'id': item['id'], 'title': item['title'], 
            'body': item['body']})

            
