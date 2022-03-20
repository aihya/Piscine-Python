class Account(object):
    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount


class Bank(object):

    def __init__(self):
        self.account = []

    def add(self, account):
        self.account.append(account)

    def transfer(self, origin, dest, amount):
        try:
            assert type(origin) in (int, str), None
            assert type(dest) in (int, str), None

            for o_account in self.account:
                if isinstance(o_account, Account) and origin in (o_account.id, o_account.name):
                    if o_account.value >= amount:
                        for d_account in self.account:
                            if isinstance(d_account, Account) and dest in (d_account.id, d_account.name):
                                if o_account is not d_account:
                                    try:
                                        d_account.transfer(amount)
                                    except AttributeError:
                                        d_account.fix_account()
                                    d_account.transfer(amount)
                                    o_account.value -= amount
                                    return True
                return False

        except AssertionError:
            return False

    def fix_account(self, account):
        pass


c = Bank()
a = Account('Wee')
a.transfer(10)
print(a.__dict__)