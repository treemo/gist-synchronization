import os
import requests
from config import TOKEN, USERNAME


# set path
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def synchronise_repository():
    print('synchronise git repository...')
    r = requests.get('https://api.github.com/users/%s/gists' % USERNAME, auth=(
        USERNAME, TOKEN
    ))

    for repo in r.json():
        name = repo['id']
        path = os.path.join(ROOT_PATH, name)
        if not os.path.exists(path):
            print('create %s' % name)
            os.system('git clone %s' % repo['git_pull_url'])

        else:
            print('update %s' % name)
            os.system('cd %s && git pull %s && git push %s' % (
                path, repo['git_pull_url'], repo['git_push_url']
            ))


synchronise_repository()

