from datetime import date, datetime, time, timedelta


def month_statistics(repository):
    """
    Obtains amount of commits and contributors of last four week
    from GitHub API.
    :param repository: A GitHub repository object.
    :return: List of lists of amounts of commits and contributors
             per every of four week and time intervals.
    """
    today_midnight = datetime.combine(date.today(), time.min)

    dates = [
        today_midnight - timedelta(days=27),
        today_midnight - timedelta(days=20),
        today_midnight - timedelta(days=13),
        today_midnight - timedelta(days=6),
        datetime.combine(date.today(), time.max)
    ]

    commits = [0, 0, 0, 0]
    contributors = []

    for i in range(4):
        authors = []
        for commit in repository.get_commits(since=dates[i], until=dates[i+1]):
            commits[i] += 1
            creator = commit.author
            if creator not in authors:
                authors.append(creator)
        contributors.append(len(authors))

    intervals = ['%s - %s' % (dates[i].strftime('%d.%m.%Y'),
                 dates[i+1].strftime('%d.%m.%Y')) for i in range(4)]

    return commits, contributors, intervals


def week_statistics(repository):
    """
    Obtains amount of commits and contributors of every day of the last
    seven days from GitHub API.
    :param repository: A GitHub repository object.
    :return: List of lists of amounts of commits and contributors
             per every day of the last seven ones and days' names.
    """
    today_midnight = datetime.combine(date.today(), time.min)

    dates = [today_midnight - timedelta(days=i) for i in range(6, -1, -1)]

    commits = [0, 0, 0, 0, 0, 0, 0]
    contributors = []

    for i in range(7):
        authors = []
        for commit in repository.get_commits(
            since=dates[i],
            until=dates[i] + timedelta(days=1)
        ):
            commits[i] += 1
            creator = commit.author
            if creator not in authors:
                authors.append(creator)
        contributors.append(len(authors))

    days_names = [day.strftime("%A") for day in dates]

    return commits, contributors, days_names
