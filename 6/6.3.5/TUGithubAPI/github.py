from api.repositories.repos import Repos


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "http://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="xxxxxxxxxxx")#此处请换成真实的github personal access token
    x = r.repos.list_your_repos()
    print(x.text)

    data = {"direction": "desc"}
    x = r.repos.list_user_repos("zhangting85", params=data)
    print(x.text)

    x = r.repos.list_organization_repos("TestUpCommunity")
    print(x.text)

    x = r.repos.list_all_public_repos()
    print(x.text)

    data = {"since": "364"}
    x = r.repos.list_all_public_repos(params=data)
    print(x.text)
