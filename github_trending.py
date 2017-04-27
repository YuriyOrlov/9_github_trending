import requests
import json
import datetime
import itertools


def get_trending_repositories(top_size):
    beginning_date = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')
    todays_date = (datetime.datetime.now()).strftime('%Y-%m-%d')
    api_url = 'https://api.github.com/search/repositories'
    additional_parameters = '&sort=stars&order=desc'
    top_trending_repos = requests.get('{}?q=language:python{}&q=created:"{}..{}"'.format(api_url,
                                                                                         additional_parameters,
                                                                                         beginning_date,
                                                                                         todays_date))
    top_trending_repos_json = json.loads(top_trending_repos.text)
    top_trending_repos_json = itertools.islice(top_trending_repos_json['items'], 0, top_size)
    return list(top_trending_repos_json)


def get_repo_info(repos):
    for item in repos:
        print("Repo name:{}\n\
               Number of stars:{}\n\
               Number of issues:{}\n\
               Link:{}".format(item['name'], item['stargazers_count'], item['open_issues'], item['svn_url']))


if __name__ == '__main__':
    top_trending_repos = get_trending_repositories(20)
    get_repo_info(top_trending_repos)
