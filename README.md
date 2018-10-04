# PR Tracker

A Python app to fetch and return Pull Requests raised by a user during Hacktoberfest 2018.

## Technologies

* Python 3.6
* GitHub GraphQL API

## Requirements

* Install [Python](https://www.python.org/downloads/)

## Setup (Mac OS)

* Run `git clone` this repository and `cd` into the project root.
* Run `pip install virtualenv` on command prompt
* Run `virtualenv ../pr-venv --python=python3`
* Run `source ../pr-venv/bin/activate`
* Run `pip install -r requirements.txt`
* Run `export API_KEY=<your-api-key>`

## Output format

```bash
Username: <Username>
PRs raised: <X>.
Repositories: {<'Repo 1'>, <'Repo 2'>, ..., <'Repo N'>}
```
