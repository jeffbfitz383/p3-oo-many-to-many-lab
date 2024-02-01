class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        all = []
        for contract in Contract.all:
            if contract.author == self:
                all.append(contract)
        return all

    def books(self):
        all = []
        for contract in self.contracts():
            all.append(contract.book)
        return all

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        count = 0
        for contract in self.contracts():
            count = count + contract.royalties
        return count
    


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)  

    def contracts(self):
        all = []
        for contract in Contract.all:
            if contract.book == self:
                all.append(contract)
        return all  

    def authors(self):
        all = []
        for contract in Contract.all:
            if contract.book == self:
                all.append(contract.author)
        return all
    




class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value 

    @property
    def book(self):
        return self._book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties =value

    @classmethod
   
    def contracts_by_date(cls, date):
        all = []
        for contract in cls.all:
            if contract.date == date:
                all.append(contract)
        return all
        
    
    