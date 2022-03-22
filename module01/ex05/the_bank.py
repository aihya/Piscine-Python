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

    def identify(self, account):
        """Identify 'account' if it exist in 'self.account' and is of type Account"""

        for acc in self.account:
            if isinstance(acc, Account):
                attrs = acc.__dict__.keys()
                if ('id' in attrs and account == acc.id) or ('name' in attrs and account == acc.name):
                    return acc
        return None

    def transfer(self, origin, dest, amount):
        """Transfer amount from account 'origin' to account 'dest'. They both have to be of type Account."""

        o = self.identify(origin)
        d = self.identify(dest)

        if isinstance(o, Account) and isinstance(d, Account):
            if ("value" in o.__dict__.keys()) and ("value" in d.__dict__.keys()):
                if o.value >= amount:
                    d.transfer(amount)
                    o.transfer(-amount)
                    return True

        return False

    def fix_account(self, account):
        """Identify 'account' and fix its attributes."""

        acc = self.identify(account)
        if isinstance(acc, Account):

            # Get current instance attributes.
            attrs = acc.__dict__.keys()

            # Create default dictionary.
            valid_attrs = {"name": None,
                           "id": None,
                           "value": 0}

            # Use previous values of 'name', 'id' and 'value' if they exist in attributes.
            if 'name' in attrs:
                valid_attrs['name'] = acc.name
            if 'id' in attrs:
                valid_attrs['id'] = acc.id
            else:
                valid_attrs['id'] = Account.ID_COUNT
                Account.ID_COUNT += 1
            if 'value' in attrs:
                valid_attrs['value'] = acc.value

            # Check if an attribute starts with the letter 'b'.
            for attr in attrs:
                if attr.startswith('b'):
                    delattr(acc, attr)

            # Check if there is an attribute starting with either 'zip' or 'addr'.
            found = False
            for attr in attrs:
                if attr.startswith('zip') or attr.startswith('addr'):
                    found = True
                    break

            if not found:
                valid_attrs['zip'] = 1337
                valid_attrs['addr'] = "Fes 7akma l3alam"

            # Update the attributes of the corresponding instance.
            acc.__dict__.update(valid_attrs)

            # Get the updated attributes
            attrs = acc.__dict__.keys()

            # Check if there is an even number of attributes and delete one of it's the case.
            if len(attrs) % 2 == 0:
                for i, attr in enumerate(attrs):
                    if attr not in ("name", "id", "value"):
                        delattr(acc, attr)
                        break

            return True
        return False
