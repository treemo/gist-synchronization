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

        # add auth infos in https url
        git_url = repo['git_pull_url'].replace('://', '://%s:%s@' % (
            USERNAME, TOKEN
        ))

        if not os.path.exists(path):
            print('create %s' % name)
            os.system('git clone %s' % git_url)

        else:
            print('update %s' % name)
            os.system('cd %(path)s && git pull %(git)s && git push %(git)s' % {
                'path': path,
                'git': git_url,
            })


if __name__ == '__main__':
    synchronise_repository()
