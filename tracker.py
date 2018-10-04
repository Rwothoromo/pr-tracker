import os
import requests
import datetime

API_KEY = os.environ.get('API_KEY')
headers = {"Authorization": "Bearer {}".format(API_KEY)}


def run_query(query):
    request = requests.post('https://api.github.com/graphql',
                            json={'query': query}, headers=headers)
    if request.status_code == 200:
        return request.json()
    else:
        raise Exception("Failed: {}. {}".format(request.status_code, query))


query = """
{
  viewer {
    login
    pullRequests(last: 30) {
      nodes {
        publishedAt
        title
        repository {
          name
        }
      }
    }
  }
}
"""

start_date = datetime.datetime.strptime(
    "2018-10-01T00:00:00Z", "%Y-%m-%dT%H:%M:%SZ")
end_date = datetime.datetime.strptime(
    "2018-10-31T23:59:59Z", "%Y-%m-%dT%H:%M:%SZ")

result = run_query(query)
username = result["data"]["viewer"]["login"]
pull_requests = result["data"]["viewer"]["pullRequests"]["nodes"]
hacktoberfest_pr_count = 0
hacktoberfest_pr_repos = []

for pr in pull_requests:
    pr_date = datetime.datetime.strptime(
        pr["publishedAt"], "%Y-%m-%dT%H:%M:%SZ")

    if start_date <= pr_date <= end_date:
        hacktoberfest_pr_repos.append(pr["repository"]["name"])
        hacktoberfest_pr_count += 1

print("Username: {}\nPRs raised: {}.\nRepositories: {}".format(
    username, hacktoberfest_pr_count, {repo for repo in hacktoberfest_pr_repos}))
