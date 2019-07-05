import csv
import random
import string
import time
from faker import Faker

RECORD_COUNT = 100
fake = Faker()

def genName(env):
    zoneChooser = {
        'Entwicklung': 'd',
        'Abnahme': 'a',
        'Produktion': 'p'
    }
    return 'm999' + ''.join(random.choice(string.ascii_lowercase) for j in range(5)) + randint(100, 999) + zoneChooser.get(env)

def genTestdata():
    with open('./data.csv', 'w', newline='') as csvfile:
        fieldnames = ['UUID', 'Servername', 'OS', 'Zone', 'Anwendung']
        osTypes = ['MacOS', 'Linux', 'Windows']
        zoneTypes = ['Entwicklung', 'Abnahme', 'Produktion']
        applications = ['MongoDB', 'OracleDB', 'PostgreSQL', 'Cassandra', 'Jira', 'Confluence', 'Notes', 'GitLab', 'WebSphere', 'Wekan', 'NodeJS', 'Apache', 'TFS', 'Proxy', 'Loadbalancer', 'MSSQL', 'SharePoint', 'Exchange']
        zone = random.choice(zoneTypes)
        os = random.choice(osTypes)
        writer = csv.DictWriter(csvfile, fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'UUID': fake.uuid4(),
                    'Servername': genName(),
                    'OS': os,
                    'Zone': zone,
                    'Anwendung': random.choice(applications)
                }
            )

if __name__ == '__main__':
    start = time()
    genTestdata()
    elapsed = time() - start
    print('created data in: {}'.format(elapsed))