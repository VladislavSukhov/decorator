from datetime import datetime
import time
import requests

URL = "https://api.stackexchange.com/2.2/questions"

def log_decorator_with_path(path):
    def logger_dec(old_foo):
        def logger_fun(*args):
            date_time = datetime.now()
            result = old_foo(*args)
            log_line = f'==> Date, time: {date_time}, Function name: {old_foo.__name__}, Arguments: {args}, result: '
            with open(path, 'a') as f:
                f.write(log_line + '\n')
                for item in result:
                    f.write(item)
                    f.write('\n')
        return logger_fun
    return logger_dec



@log_decorator_with_path('logs.txt')
def questions_for_two_days(URL):
    now = round(time.time())
    two_days_ago = round(now - 172800)

    response = requests.get(URL, params={"fromdate": two_days_ago, "todate": now, "order": "desc", "sort": "creation", "tagged": "python", "site": "stackoverflow"})
    resp = response.json()
    items = resp['items']
    quests = []
    for item in items:
        title = item['title']
        link = item['link']
        line = f'Вопрос: {title}, Ссылка на вопрос: {link}.'
        print(line)
        quests.append(line)    
    return quests


questions_for_two_days(URL)