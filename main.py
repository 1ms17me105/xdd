import subprocess
import datetime
import os
import re
import time

def tracker():

    while True:

        init = ['git', 'init']
        status = ['git', 'status']
        add = ['git', 'add', '.']
        connect = ['git', 'remote', 'add', 'origin', 'https://github.com/1ms17me105/test_git1.git']
        commit = ['git', 'commit', '-m', f'{datetime.datetime.now()}']
        push = ['git', 'push', '-u', 'origin', 'main']
        pull = ['git', 'pull', 'origin', 'main']

        if not os.path.isdir('.git'):
            subprocess.call(init)

        PIPE = subprocess.PIPE

        def process(action):
            command = subprocess.Popen(action, stdout = PIPE, stderr = PIPE)
            stdoutput, error = command.communicate()
            return {'output': stdoutput.decode("utf-8"), 'error': error.decode("utf-8")}
        
        remote_connect = process(connect)
        print(f'''Connecting to remote repo:
        ---------------------------
        {remote_connect['output']}
        --------------------------------
        {remote_connect['error']}
        --------------------------------''')

        pulling = process(pull)
        print(f'''Pulling:
        ---------------------------
        {pulling['output']}
        --------------------------------
        {pulling['error']}
        --------------------------------''')

        status_check = process(status)
        print(f'''Checking status
        ---------------------------
        {status_check['output']}
        --------------------------------
        {status_check['error']}
        --------------------------------''')

        if re.search(r'\nChanges not staged for commit:\n', status_check['output']):
            stage = process(add)
            print(f'''Stagings Changes:
                    ---------------------------
                    {stage['output']}
                    --------------------------------
                    {stage['error']}
                    --------------------------------''')
            comm = process(commit)
            print(f'''Commiting changes:
                    ---------------------------
                    {comm['output']}
                    --------------------------------
                    {comm['error']}
                    --------------------------------''')

        if re.search(r'\nUntracked files:\n', status_check['output']):
            stage = process(add)
            print(f'''Stagings Changes:
                    ---------------------------
                    {stage['output']}
                    --------------------------------
                    {stage['error']}
                    --------------------------------''')
            comm = process(commit)
            print(f'''Commiting changes:
                    ---------------------------
                    {comm['output']}
                    --------------------------------
                    {comm['error']}
                    --------------------------------''')

        pushing = process(push)
        print(f'''Pushing Changes:
                    ---------------------------
                    {pushing['output']}
                    --------------------------------
                    {pushing['error']}
                    --------------------------------''')

        print(f'Pushed now!')

        time.sleep(60)

tracker()