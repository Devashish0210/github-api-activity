from urllib.request import urlopen
import json

username = input("Enter a GitHub username ")

URL = "https://api.github.com/users/"+username+"/events"

try:
    with urlopen(URL) as f:
        result = json.load(f)
        with open("data.json", 'w+') as file:
            json.dump(result, file, indent=4, default =str)
except:
    print("Something went wrong, please check the entered username")
    exit()


def pushevent(event):
    repo = event['repo']['name']
    number = event['payload']['distinct_size']
    if number == 1:
        print(f'Pushed a commit to the repo {repo}')
    else:
        print(f'Pushed {number} commits to the repo {repo}')

def createevent(event):
    ref_type = event['payload']['ref_type']
    if ref_type == 'repository':
        print('Created a repository')
    elif ref_type == 'branch':
        repo = event['repo']['name']
        print(f'Created a branch in the repo {repo}')
    else:
        print(f'Created a tag in {repo}')

def forkevent(event):
    fork = event['repo']['name']
    print(f'Forked the repo {fork}')

def issuesevent(event):
    action = event['payload']['action']
    issue = event['payload']['issue']['title']
    print(f'{action} the issue {issue}')

def deleteevent(event):
    ref_type = event['payload']['ref_type']
    print(f'Deleted a {ref_type}')

def gollumevent(event):
    pages = event['payload']['pages']
    for pos, page in enumerate(pages):
        action = page[pos]['action']
        name = page[pos]['page_name']
        print(f'{action} the page {name}')

def issuecommentevent(event):
    action = event['payload']['action']
    issue_name = event['payload']['name']
    comment = event['payload']['comment']
    print(f'{action} the comment {comment} on the issue {issue_name}')

def memberevent(event):
    action = event['payload']['action']
    username = event['payload']['user']['name']
    print(f'{action} user {username}')

def publicevent(event):
    print("Made a private repo public")

def pullrequestevent(event):
    action = event['payload']['action']
    number = event['payload']['number']
    print(f'{action} the pull request number {number}')

def watchevent(event):
    print("Starred a repo")

for event in result:
    event_type = event['type']
    if event_type.lower() == 'pushevent':
        pushevent(event)
    elif event_type.lower() == 'createevent':
        createevent(event)
    elif event_type.lower() == 'forkevent':
        forkevent(event)
    elif event_type.lower() == 'issuesevent':
        issuesevent(event)
    #
    elif event_type.lower() == 'deleteevent':
        deleteevent(event)
    elif event_type.lower() == 'gollumevent':
        gollumevent(event)
    elif event_type.lower() == 'issuecommentevent':
        issuecommentevent(event)
    elif event_type.lower() == 'memberevent':
        memberevent(event)
    elif event_type.lower() == 'publicevent':
        publicevent(event)
    elif event_type.lower() == 'pullrequestevent':
        pullrequestevent(event)
    # elif event_type.lower() == 'pullrequestreviewevent':
    #     pullrequestreviewevent(event)
    # elif event_type.lower() == 'pullrequestreviewcommentevent':
    #     pullrequestreviewcommentevent(event)
    # elif event_type.lower() == 'pullrequestreviewthreadevent':
    #     pushpullrequestreviewthreadeventevent(event)
    # elif event_type.lower() == 'releaseevent':
    #     releaseevent(event)
    # elif event_type.lower() == 'sponsorshipevent':
    #     sponsorshipevent(event)
    elif event_type.lower() == 'watchevent':
        watchevent(event)