#!/usr/bin/env python

import click
import azure_devops.count as azure

import json


@click.group()
def cli():
    pass


@cli.command(help="Fetch contributor counts from your Azure DevOps Organization")
@click.option('--token', hide_input=True, prompt=True,
              help='Azure DevOps Personal Access Token. '
                   'See https://learn.microsoft.com/en-us/azure/devops/organizations/accounts/use-personal-access-tokens-to-authenticate '
                   'for details on how to create a Personal Access Token.')
@click.option('--organization', prompt=True,
              help='Azure DevOps Organization - ie: YOURORG in URL https://dev.azure.com/YOURORG.')
@click.option('--since-days', default=90, help='Number of days prior to now to count contributors (default=90).')
@click.option('--projects', default="",
              help='Project names to check (separated by comma). If unspecified, ALL projects will be checked.')
def azure_devops(token: str, organization: str, since_days: int, projects: str):
    # Project name filter is not case sensitive
    projects = projects.lower().split(",") if projects else None

    # Fetch results
    results = azure.count_contributors(token, organization, since_days, projects)

    print(json.dumps(results.combined_email_contribution_count_map, indent=4))
    print(
        f"Total Contributors in the past {since_days} days = {len(results.combined_email_contribution_count_map.keys())}")


if __name__ == '__main__':
    cli()
