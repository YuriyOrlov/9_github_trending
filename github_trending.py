import requests
import json
import datetime

NUMBER_OF_REPOSITORIES_TO_SHOW = 20


def get_trending_repositories(top_size):
    beginning_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    todays_date = (datetime.datetime.now()).strftime('%Y-%m-%d')
    url = 'https://api.github.com/search/repositories?q=python+created:"{}..{}"'.format(beginning_date, todays_date)
    additional_parameters = {'sort': 'stars', 'order': 'desc', 'per_page': top_size}
    top_trending_repos = requests.get(url, params=additional_parameters)
    return json.loads(top_trending_repos.text)


def shows_needed_info_about_repositories(repos):
    for item in repos['items']:
        print("Repo name:{}\n\
               Number of stars:{}\n\
               Number of issues:{}\n\
               Link:{}".format(item['name'], item['stargazers_count'], item['open_issues'], item['svn_url']))


if __name__ == '__main__':
    top_trending_repos = get_trending_repositories(NUMBER_OF_REPOSITORIES_TO_SHOW)
    shows_needed_info_about_repositories(top_trending_repos)
