import requests
import os
import csv
import json
from datetime import datetime


def collect_data():
    proxies = {
        'https': f'http://{os.getenv("LOGIN")}:{os.getenv("PASSWORD")}@163.198.213.235:8000'
    }


def main():
    collect_data()
    
    
if __name__ == '__main__':
    main()
    
    

