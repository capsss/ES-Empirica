from pull_request_especifico import especifico
import time
import json

TOTAL_PULL_REQUESTS = 5000

for numero_pull_request in range(1, TOTAL_PULL_REQUESTS):
    print(numero_pull_request)
    data = especifico.requisitar(str(numero_pull_request))
    if data:
        with open('pull requests jquery/' + str(numero_pull_request) + '.json', 'w') as outfile:
            json.dump(data, outfile)

        time.sleep(1)
