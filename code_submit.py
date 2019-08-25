#! /usr/bin/env python3

from getpass import getpass
import argparse
from robobrowser import RoboBrowser
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import json
import time


def get_submission_data(user):
    req = requests.get('https://codeforces.com/api/user.status?'
                       'handle={}&from=1&count=1'.format(user))
    content = req.content.decode()
    js = json.loads(content)

    if 'status' not in js or js['status'] != 'OK':
        raise ConnectionError('Codeforces BOOM!')

    res = js['result'][0]
    id_, verdict = res['id'], res['verdict']
    return id_, verdict


def main():
    parser = argparse.ArgumentParser(
        description='Submit codeforces in command line')
    #parser.add_argument('user', type=str,
    #                    help='Your codeforces ID')
    parser.add_argument('prob', type=str,
                        help='Codeforces problem ID (Ex: 33C)')
    parser.add_argument('file', type=argparse.FileType('r'),
                        help='path to the source code')
    args = parser.parse_args()
	

    user_name = os.getenv('HANDLE')#args.user
    #last_id, _ = get_submission_data(user_name)

    passwd = os.getenv('PASS')#getpass()

    start_time = time.time()
    browser = RoboBrowser()
    browser.open('https://codeforces.com/enter')

    enter_form = browser.get_form('enterForm')
    enter_form['handleOrEmail'] = user_name
    enter_form['password'] = passwd
    browser.submit_form(enter_form)

    try:
        checks = list(map(lambda x: x.getText()[1:].strip(),
            browser.select('div.caption.titled')))
        if user_name not in checks:
            print("Login Failed.. probably because you've typed"
                  "a wrong password.")
            return
    except Exception as e:
        print("Login Failed.. probably because you've typed"
              "a wrong password.")
        return 

    browser.open('https://codeforces.com/problemset/submit')
    submit_form = browser.get_form(class_='submit-form')

    submit_form['submittedProblemCode'] = args.prob
    submit_form['source'] = str(args.file.read())

    browser.submit_form(submit_form)

    '''
    if browser.url[-6:] != 'status':
        print('Your submission has failed, probably '
              'because you have submit the same file before.')
        return
    '''

    end_time = time.time()

    print("times: ", end_time - start_time)

    print('Submitted, wait for result...')
    while True:
        id_, verdict = get_submission_data(user_name)
        if id_ != "last_id" and verdict != 'TESTING':
            print('Verdict = {}'.format(verdict))
            break

if __name__ == '__main__':
    main()
