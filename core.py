import requests

from objects import Genre, Access


class AT:
    
    def __init__(self) -> None:
        self.__API: str = "https://api.author.today"
        self.__WEB_API: str = "https://author.today"
        self.__TOKEN: str = "Bearer guest"
        self.__HEADERS: dict = {
            "authorization": self.__TOKEN,
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        self.__GENRES: list[Genre] = []
        self.__ACCESSES: list[Access] = []
    
    def Login(self, user_login: str, user_password: str) -> dict:
        data = {
            "login": user_login,
            "password": user_password
        }
        response = requests.post(
            f"{self.__API}/v1/account/login-by-password",
            json=data,
            headers=self.__HEADERS,
            verify=False
        ).json()
        
        if "token" in response:
            self.__TOKEN = response["token"]
            self.__HEADERS["authorization"] = f"Bearer {self.__TOKEN}"
            self.__USER_ID = self.__GetAccountInfo__()["id"]
        
        return response
    
    def LoginWithToken(self, token: str) -> dict:
        self.__TOKEN = token
        self.__HEADERS["authorization"] = f"Bearer {self.__TOKEN}"
        response = self.__GetAccountInfo__()
        if "id" in response:
            self.__USER_ID = response["id"]
        return response
    
    def __GetAccountInfo__(self) -> dict:
        return requests.get(
            f"{self.__API}/v1/account/current-user",
            headers=self.__HEADERS,
            verify=False
        ).json()
        
    def __RefreshToken__(self) -> dict:
        return requests.post(
            f"{self.__API}/v1/account/refresh-token",
            headers=self.__HEADERS,
            verify=False
        ).json()
        
    def __GetAllGenres__(self) -> dict:
        genres = requests.get(
            f"{self.__API}/v1/work/genres",
            headers=self.__HEADERS,
            verify=False
        ).json()
        
        for genre in genres:
            genre_name: str = genre["title"]
            genre_key: str = genre["code"]
            genre_id: int = int(genre["id"])
            
            parent_genre = None
            if genre["parentId"] != None:
                parent_genre = self.__FindGenreInAll__(genre["parentId"])
            
            if parent_genre != None:
                parent_genre.Childs.append(Genre(genre_name, genre_key, genre_id))
            else:
                self.__GENRES.append(Genre(genre_name, genre_key, genre_id))
            
        return genres

    @property
    def AllGenres(self) -> list[Genre]:
        if len(self.__GENRES) == 0:
            self.__GetAllGenres__()
        return self.__GENRES
    
    def __FindGenreInAll__(self, genre_id: str | int, all_genre: list[Genre] = None) -> Genre | None:
        if all_genre == None:
            all_genre = self.__GENRES
            
        if type(genre_id) == str:
            if genre_id.isnumeric():
                genre_id = int(genre_id)
        
        for genre in all_genre:
            if genre.Id == genre_id:
                return genre
            else:
                if len(genre.Childs) > 0:
                    child = self.__FindGenreInAll__(genre_id, genre.Childs)
                    if child:
                        return child
        
        return None
    
    @property
    def AllAccesses(self) -> list[Access]:
        accesses = requests.get(
            f"{self.__API}/v1/catalog/accesses",
            headers=self.__HEADERS,
            verify=False
        ).json()
        
        self.__ACCESSES = []
        for access in accesses:
            self.__ACCESSES.append(Access(access["title"], access["value"]))
        
        return self.__ACCESSES
