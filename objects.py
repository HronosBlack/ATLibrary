class ATObject:
    """
    Класс общего представления объектов онлайн библиотеки Author.Today
    """
    
    def __init__(self, name: str = "", key: str = "") -> None:
        """Инициализатор объекта класса

        Args:
            name (str, не обязателен): Наименование объекта. По умолчанию "".
            key (str, не обязателен): URL ключ объекта для запроса. По умолчанию "".
        """
        self.__NAME: str = name
        self.__URL_KEY: str = key
        self.__URL_PREFIX: str = ""
    
    @property
    def Name(self) -> str:
        return self.__NAME
    
    @Name.setter
    def Name(self, value: str) -> None:
        self.__NAME = value
    
    @property
    def UrlKey(self) -> str:
        return self.__URL_KEY
    
    @UrlKey.setter
    def UrlKey(self, value: str) -> None:
        self.__URL_KEY = value
    
    @property
    def UrlPrefix(self) -> str:
        return self.__URL_PREFIX
    
    @UrlPrefix.setter
    def UrlPrefix(self, value: str) -> None:
        self.__URL_PREFIX = value
    
    def __str__(self) -> str:
        return self.Name
    
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return ((self.Name == value.Name) and 
                (self.UrlKey == value.UrlKey) and
                (self.UrlPrefix == value.UrlPrefix))
    
    @property
    def UrlQuery(self) -> str:
        return f"{self.UrlPrefix}={self.UrlKey}"
    
    
class Author(ATObject):
    """
    Класс представления автора произведения оналйн библиотеки Author.Today
    """
    
    def __init__(self, name: str = "", key: str = "") -> None:
        super().__init__(name, key)
        self.UrlPrefix = "author"
        
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return super().__eq__(value)
        
        
class Series(ATObject):
    """
    Класс представления серии произведений онлайн библиотеки AuthorToday
    """
    
    def __init__(self, name: str = "", key: str = "") -> None:
        super().__init__(name, key)
        self.UrlPrefix = "series"
        
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return super().__eq__(value)


class Genre(ATObject):
    """
    Класс представления жанра произведения онлайн библиотеки Author.Today
    """
    
    def __init__(self, name: str = "", key: str = "", id: int | None = None, childs: list['Genre'] = None) -> None:
        super().__init__(name, key)
        self.UrlPrefix = "genre"
        if childs:
            self.__CHILDS: list['Genre'] = childs
        else:
            self.__CHILDS: list['Genre'] = []
        self.__ID: int | None = id
    
    @property
    def Childs(self) -> list['Genre']:
        return self.__CHILDS
    
    @Childs.setter
    def Childs(self, value: list['Genre']) -> None:
        self.__CHILDS = value
        
    @property
    def Id(self) -> int:
        return self.__ID
    
    @Id.setter
    def Id(self, value: int) -> None:
        self.__ID = value
        
    def AddChild(self, value: 'Genre') -> None:
        self.Childs.append(value)
        
    def __eq__(self, value: object) -> bool:
        if type(value) != type(self):
            return False
        return super().__eq__(value) and (self.Childs == value.Childs)

class Book(ATObject):
    """
    Класс представление произведения онлайн библиотеки Author.Today
    """
    
    def __init__(self, name: str = "", key: str = "", authors: list[Author] | Author = None, genres: list[Genre] = None, series: Series = None) -> None:
        super().__init__(name, key)
        self.UrlPrefix = "work"
        
        if genres:
            self.__GENRES: list[Genre] = genres
        else:
            self.__GENRES: list[Genre] = []
        
        if authors:
            if type(authors) == Author:
                self.__AUTHORS: list[Author] = [authors, ]
            else:
                self.__AUTHORS: list[Author] = authors
        else:
            self.__AUTHORS: list[Author] = []
        
