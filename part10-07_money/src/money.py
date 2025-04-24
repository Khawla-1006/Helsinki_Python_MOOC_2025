# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self._euros = euros
        self._cents = cents

    def __str__(self):
        if self._cents < 10 :
            return f"{self._euros}.0{self._cents} eur"
        else:
            return f"{self._euros}.{self._cents} eur"

    def __eq__(self, another):
        return self._euros == another._euros and self._cents == another._cents
    
    def __gt__(self, another):
        if self._euros == another._euros :
            return self._cents > another._cents
        return self._euros > another._euros
    
    def __lt__(self, another):
        if self._euros == another._euros :
            return self._cents < another._cents
        return self._euros < another._euros
    
    def __ne__(self, another):
        if self._euros == another._euros :
            return self._cents != another._cents
        return self._euros != another._euros

    def __add__(self, another):
        add_euros = self._euros + another._euros
        add_cents = self._cents + another._cents
        cents_to_eur = 0
        if add_cents >= 100 :
            cents_to_eur = add_cents // 100
            remain = add_cents - cents_to_eur*100
            add_euros += cents_to_eur
            if remain < 10 :
                return f"{add_euros}.0{remain} eur"
            else:
                return f"{add_euros}.{remain} eur"
        else:
            if add_cents < 10 :
                return f"{add_euros}.0{add_cents} eur"
            else:
                return f"{add_euros}.{add_cents} eur"

    def __sub__(self, another):
        if self._euros < another._euros :
            raise ValueError("a negative result is not allowed")
        elif self._euros == another._euros and self._cents < another._cents:
            raise ValueError("a negative result is not allowed")
        else:
            remain_eur = self._euros - another._euros
            if self._cents < another._cents:
                remain_cents = self._cents + 100 - another._cents
                remain_eur -= 1
            else:
                remain_cents = self._cents - another._cents
            if remain_cents < 10 :
                return f"{remain_eur}.0{remain_cents} eur"      
            else:
                return f"{remain_eur}.{remain_cents} eur"  
if __name__ == "__main__":
    e1 = Money(4,5)
    e2 = Money(0,50)
    e3 = Money(4,1)
    # print(e1)
    # print(e2)
    # print(e3)
    # print(e1 == e3)
    # print(e1 == e2)
    # print(e1 != e2)
    # print(e1 < e2)
    # print(e1 > e2)
    e3 = e1 + e2
    e4 = e1 - e2
    print(e3)
    print(e4)