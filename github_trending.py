import requests
import datetime


def get_trending_repositories(top_size=20):
    num_days_in_the_past = 7
    beginning_date = (datetime.datetime.now() - datetime.timedelta(days=num_days_in_the_past)).strftime('%Y-%m-%d')
    todays_date = (datetime.datetime.now()).strftime('%Y-%m-%d')
    url = 'https://api.github.com/search/repositories'
    additional_parameters = {'q': 'python+created:"{}..{}"'.format(beginning_date, todays_date),
                             'sort': 'stars', 'order': 'desc', 'per_page': top_size}
    top_trending_repos = requests.get(url, params=additional_parameters)
    return top_trending_repos.json()


def shows_needed_info_about_repositories(repos):
    for item in repos['items']:
        print("Repo name:{}\n\
               Number of stars:{}\n\
               Number of issues:{}\n\
               Link:{}".format(item['name'], item['stargazers_count'], item['open_issues'], item['svn_url']))


if __name__ == '__main__':
    top_trending_repos = get_trending_repositories()
    shows_needed_info_about_repositories(top_trending_repos)
