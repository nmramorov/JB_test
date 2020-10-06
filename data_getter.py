from github import Github


def get_data(login, password):
    g = Github(login, password)
    repo = g.get_repo("facebook/react")
    data = []

    for stat in repo.get_stats_contributors():
        stats = {
            'login': stat.author.login,
            'total': stat.total,
        }
        data.append(stats)
    return data





