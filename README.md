# PR Tracker

A Python app to fetch and return Pull Requests raised by a user during Hacktoberfest 2018.

## Technologies

* Python 3.6
* GitHub GraphQL API

## Requirements

* Install [Python](https://www.python.org/downloads/)

## Setup (Mac OS)

* Run `git clone` this repository and `cd` into the project root.
* Run `pip install virtualenv` on command prompt.
* Run `virtualenv ../pr-venv --python=python3`.
* Run `source ../pr-venv/bin/activate`.
* Run `pip install -r requirements.txt`.
* Run `export API_KEY=<your-api-key>`. See how to [Create a token](https://help.github.com/articles/creating-a-personal-access-token-for-the-command-line/).
* Run `python tracker.py`.

## Output format

```bash
Username: <Username>
PRs raised: Personal - <X> and Other - <Y>.
Personal repositories: {<'Repo 1'>, <'Repo 2'>, ..., <'Repo N'>}
Other repositories: {<'Repo 1'>, <'Repo 2'>, ..., <'Repo N'>}
```
