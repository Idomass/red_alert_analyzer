#! /usr/bin/env python3

import argparse
import datetime
from oref_analyzer import OrefAnalyzer

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--language', dest='lang', default='en', choices=['en', 'he'])
    parser.add_argument('--location', help='Location to show history of red alerts')
    parser.add_argument('--start-date', type=lambda s: datetime.datetime.strptime(s, '%Y-%m-%d'),
                        default=datetime.datetime(2021, 5, 10))

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    OrefAnalyzer(language=args.lang).show_history(args.location, args.start_date)
