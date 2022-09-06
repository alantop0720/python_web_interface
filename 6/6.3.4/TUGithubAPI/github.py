from api.repositories.repos import Repos


class Github():
    def __init__(self, **kwargs):
        self.api_root_url = "http://api.github.com"
        self.repos = Repos(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Github(token="xxxxxxxxxxx")#此处请换成真实的github personal access token
    x = r.repos.list_your_repos()
    print(x.text)

    r = Github(token="xxxxxxxxxxx")#此处请换成真实的github personal access token
    x = r.repos.list_your_repos(visibility="private")
    print(x.text)

    r = Github(token="xxxxxxxxxxx")#此处请换成真实的github personal access token
    x = r.repos.list_your_repos(visibility="all")
    print(x.text)

    r = Github(token="xxxxxxxxxxx")#此处请换成真实的github personal access token
    x = r.repos.list_your_repos(direction="desc")
    print(x.text)
