class Queries:
    def __init__(self):
        self.city  = ""
        self.token = ""
        self.lang  = ""
        self.unit  = ""
    # Construtor Padrão

    def __init__(self, city):
        self.city  = city
        self.lang  = 'pt_br'
        self.unit  = 'metric'
        self.token = 'token no openweathermap.org'
    # Construtor Parametrizado
    
    def getQueries(self):
        return (
            "?q="      + self.city 
            +"&appid=" + self.token
            +"&lang="  + self.lang 
            +"&units=" + self.unit
        )
    # getQueries
# Queries