from typing import List


class RepositoryContributorCount:
    def __init__(self, repository_name: str):
        """
        :param repository_name: The name of the repository
        :param email_contribution_count_map: A map of email-># contributions
        """
        self.repository_name = repository_name
        self.email_contribution_count_map = dict()

    def increment(self, email: str):
        if email not in self.email_contribution_count_map:
            self.email_contribution_count_map[email] = 0
        self.email_contribution_count_map[email] += 1


class ContributorCountSummary:
    def __init__(self, counts: List[RepositoryContributorCount]):
        self.counts = counts

        # Combine all repository counts into a single summary
        self.combined_email_contribution_count_map = dict()

        for record in counts:
            for (email, contribution_count) in record.email_contribution_count_map.items():
                if email not in self.combined_email_contribution_count_map:
                    self.combined_email_contribution_count_map[email] = 0
                self.combined_email_contribution_count_map[email] += contribution_count

