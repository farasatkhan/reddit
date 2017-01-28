import os


def create_directory(direct):
    if not os.path.exists(direct):
        os.makedirs(direct)
        create_file(direct)


def create_file(file_name):
    subreddit = os.path.join(file_name, 'subreddit.txt')
    if not os.path.exists(subreddit):
        make_file(subreddit, '')


def make_file(file, data):
    f = open(file, 'w')
    f.write(data)


def file_to_set(file_name):
    results = []
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results