from urllib import request

from bs4 import BeautifulSoup


def repos_by_stars(period):
    """
    :param period: Week or month.
    :return: A list of lists of repositories, its owners and its amount
             of stars per the period.
    """
    if period == 'week':
        git_trending = BeautifulSoup(
            request.urlopen('https://github.com/trending?since=weekly'),
            'html.parser'
        )
    else:
        git_trending = BeautifulSoup(
            request.urlopen('https://github.com/trending?since=monthly'),
            'html.parser'
        )

    top_block = BeautifulSoup(
        str(git_trending.select('.repo-list')[0]),
        'html.parser'
    )

    # Making of a lists of top 25 repositories and their authors.
    h3 = top_block.find_all('h3')
    authors = []
    repositories = []
    for h in h3:
        a = h.find('a')
        details = a['href'].split('/')
        authors.append(details[1])
        repositories.append(details[2])

    # Making of a list of the amount of stars of the repositories.
    meta = top_block.find_all('p', class_='repo-list-meta')
    stars = []
    for p in meta:
        meta_contents = p.contents[0].split('   ')
        if len(meta_contents) == 12:
            repo_stars = meta_contents[4].split(' ')[1]
        else:
            repo_stars = meta_contents[2].split(' ')[1]
        if ',' in repo_stars:
            repo_stars = repo_stars.replace(',', '')
        stars.append(int(repo_stars))

    top = [[repositories[i], authors[i], stars[i]] for i in range(25)]

    return sorted(top, key=lambda repo: repo[2], reverse=True)
