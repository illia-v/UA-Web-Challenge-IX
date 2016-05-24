from datetime import datetime

from github.MainClass import Github
from github.GithubException import GithubException, UnknownObjectException

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SearchForm
from .top import repos_by_stars
from .repo_statistics import month_statistics, week_statistics


def index(request):
    """
    :param request: A url request.
    :return: If a method of request is equal to 'POST' and the search form is
             valid, returns a detail view of a requested repository.
             Otherwise, returns the main page with the search form and
             list of recently visited pages from saved cookies.
    """
    if request.method == 'POST':
        form = SearchForm(request.POST)

        if form.is_valid():
            login = request.POST['login'].strip()
            repo = request.POST['repository'].strip()
            return HttpResponseRedirect(reverse('repo_details',
                                                args=(login, repo)))
    else:
        form = SearchForm()

    if 'visited' in request.session and request.session['visited'] is not None:
        visited = reversed(request.session['visited'].split('---'))
    else:
        visited = None

    return render(request, 'statistics_app/index.html',
                  {'form': form, 'visited': visited})


def repo_details(request, login, repo):
    """
    :param request: A url request.
    :param login: An argument from a url
    :param repo: An argument from a ulr
    :return: If the login and the repository exists, returns its statistics
             and adds the login and the name of repository to 'visited'
             cookies.
             If there is not such login and/or repository, returns a 404 error
             message.
             If there is an GitHub API rate limit, returns an 403 error
             message.
    """
    try:
        repository = Github().get_user(login).get_repo(repo)

        session = request.session
        owner = repository.owner.login
        name = repository.name
        if 'visited' in session and session['visited'] is not None:
            if '%s/%s' % (owner, name) not in session['visited']:
                session['visited'] += '---%s/%s' % (owner, name)
        else:
            session['visited'] = '%s/%s' % (owner, name)
            now = datetime.now().time().strftime('%H:%M:%S').split(':')
            # The day's number of seconds minus an amount of ones
            # since the start of the current day.
            seconds_to_midnight = 86400 - (int(now[0]) * 3600 +
                                           int(now[1]) * 60 + int(now[2]))
            # Setting up how much time the cookies file will exist.
            session.set_expiry(seconds_to_midnight)

        week = week_statistics(repository)
        month = month_statistics(repository)

        return render(request, 'statistics_app/repo_details.html',
                      {'repo': repository,
                       'week_commits': week[0],
                       'week_contributors': week[1],
                       'week_days_names': week[2],
                       'month_commits': month[0],
                       'month_contributors': month[1],
                       'month_intervals': month[2],
                       'rate_limit': False, 'not_found': False})

    except (UnknownObjectException, UnicodeEncodeError):
        return render(request, 'statistics_app/repo_details.html',
                      {'not_found': True, 'rate_limit': False})

    except GithubException:
        return render(request, 'statistics_app/repo_details.html',
                      {'rate_limit': True, 'not_found': False})


def top_repo(request):
    """
    :param request: A url request.
    :return: Top 25 repositories by stars for a period (week or month).
    """
    if request.GET.get('period') == 'month':
        top = repos_by_stars('month')
        period = 'month'
    else:
        top = repos_by_stars('week')
        period = 'week'
    return render(request, 'statistics_app/top_repo.html', {'top': top,
                                                            'period': period})
