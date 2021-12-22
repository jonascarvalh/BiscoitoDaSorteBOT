class Url:
    def __init__(self):
        self.queries  = ""
        self.base_url = ""
    # Construtor Padrão

    def __init__(self, queries, base_url):
        self.queries  = queries
        self.base_url = base_url
    # Construtor Parametrizado

    def getUrl(self):
        return (self.base_url + self.queries)
    # getUrl
# class Url