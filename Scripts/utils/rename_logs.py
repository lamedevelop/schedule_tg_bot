"""
Rename logs script from %d-%m-%Y to %Y-%m-%d format.

Usage:
    >> python3 RunManager.py [--config=custom] --script=rename_logs
"""


import os
import re

LOGS_FOLDER = 'Logs'


def main():
    files = os.listdir(LOGS_FOLDER)
    # rename(files)
    check(files)


def rename(files):
    """Rename log files.

    @param files Array of files in logs dir.
    """

    for file in files:
        file_s = file.split('_')
        day, month, year = file_s[-1].split('.log')[0].split('-')

        date = year + '-' + month + '-' + day
        file_s[-1] = date + '.log'

        new_file = '_'.join(file_s)

        os.rename(f'{LOGS_FOLDER}/{file}', f'{LOGS_FOLDER}/{new_file}')


def check(files):
    """Check that all files was renamed.

    @param files Array of files in logs dir.
    """

    regex = re.compile('(_[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9].log$)')

    for file in files:
        print(">> ", file)
        if regex.search(file):
            print("++ ", file)
            print()
