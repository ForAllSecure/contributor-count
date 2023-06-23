from datetime import datetime, timedelta
from typing import List

from azure.devops.v7_1.git import GitQueryCommitsCriteria
from msrest.authentication import BasicAuthentication
from azure.devops.connection import Connection

from common.model import ContributorCountSummary, RepositoryContributorCount

import pprint

RECORDS_TO_FETCH = 1_000_000


def from_date_str(since_days: int) -> str:
    from_date = datetime.today() - timedelta(days=since_days)

    return f'{from_date.year}/{from_date.month}/{from_date.day} {from_date.hour}:{from_date.minute}'


def count_contributors(personal_access_token: str,
                       organization: str,
                       since_days: int = 90,
                       project_names: List[str] = None) -> ContributorCountSummary:
    """
    Count the number of unqiue contributors
    :param personal_access_token: Personal access token is required to access REST API
    :param organization: The name of the organization to check
    :param since_days: Limit commits to those within the last 'since_days" days.
    :param project_names: Limit the matching projects to those in the list
    :return: A ContributorCountSummary instance containing contributor counts for each repo
    """
    from_date = from_date_str(since_days)

    organization_url = f'https://dev.azure.com/{organization}'
    credentials = BasicAuthentication('', personal_access_token)
    connection = Connection(base_url=organization_url, creds=credentials)

    # Get a client (the "core" client provides access to projects, teams, etc)
    core_client = connection.clients.get_core_client()
    # Git_client is used to access repository information for a project
    git_client = connection.clients.get_git_client()

    projects = core_client.get_projects(top=RECORDS_TO_FETCH)
    results = []
    for project in projects:
        # If a project filter is specified, skip if project is not present
        if project_names and project.name.lower() not in project_names:
            continue

        record = RepositoryContributorCount(project.name)

        # Gather repos for the project. Projects can contain 0 or more repositories.
        repos = git_client.get_repositories(project.id)
        for repo in repos:
            search_criteria = GitQueryCommitsCriteria(from_date=from_date)
            commits = git_client.get_commits(repo.id, search_criteria=search_criteria, project=project.id, top=RECORDS_TO_FETCH)
            for commit in commits:
                record.increment(commit.author.email)
        results.append(record)

    return ContributorCountSummary(results)