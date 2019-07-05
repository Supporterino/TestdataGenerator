import csv
import random
from random import randint
import string
from time import time
from faker import Faker
from faker.providers import misc

RECORD_COUNT = 100000000
fake = Faker()
fake.add_provider(misc)

def genName(env):
    zoneChooser = {
        'Entwicklung': 'd',
        'Abnahme': 'a',
        'Produktion': 'p'
    }
    return 'm999' + ''.join(random.choice(string.ascii_lowercase) for j in range(5)) + str(randint(100, 999)) + zoneChooser.get(env)

def genTestdata():
    with open('./data.csv', 'w+') as csvfile:
        fieldnames = ['UUID', 'Servername', 'OS', 'Zone', 'Anwendung']
        osTypes = ['MacOS', 'Linux', 'Windows']
        zoneTypes = ['Entwicklung', 'Abnahme', 'Produktion']
        applications = ['MongoDB', 'OracleDB', 'PostgreSQL', 'Cassandra', 'Jira', 'Confluence', 'Notes', 'GitLab', 'WebSphere', 'Wekan', 'NodeJS', 'Apache', 'TFS', 'Proxy', 'Loadbalancer', 'MSSQL', 'SharePoint', 'Exchange']
        writer = csv.DictWriter(csvfile, fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            zone = random.choice(zoneTypes)
            os = random.choice(osTypes)
            writer.writerow(
                {
                    'UUID': fake.uuid4(),
                    'Servername': genName(zone),
                    'OS': os,
                    'Zone': zone,
                    'Anwendung': random.choice(applications)
                }
            )

if __name__ == '__main__':
    print('Generating {:,} assets'.format(RECORD_COUNT))
    start = time()
    genTestdata()
    elapsed = time() - start
    print('created data in: {}'.format(elapsed))