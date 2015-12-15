##############################################################
# An alternative implementation of the tree data abstraction #
##############################################################

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return {'<root>': root, '<branches>': branches}

def root(tree):
    return tree['<root>']

def branches(tree):
    return tree['<branches>']

def is_tree(tree):
    if type(tree) != dict or '<root>' not in tree or '<branches>' not in tree:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree(size)

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return root(w)

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return root(w) != None

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, u, v = examples()
    >>> print_tree(t)
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(t))
    3
      1
        2
      2
        1
    >>> print_tree(t)  # t should not change
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(v))
    9
      4
        3
          1
            2
          2
            1
      2
        6
          5
            1
          1
            5
              2
                3
              3
                2
    >>> print_tree(v)  # v should not change
    None
      4
        None
          1
            2
          2
            1
      2
        None
          5
            1
          1
            None
              2
                3
              3
                2
    """
    "*** YOUR CODE HERE ***"
    if is_weight(m):
        return weight(size(m))
    if root(m) == None:
        temp_root = total_weight(m)
        # return tree(total_weight(m), [side(length(s), with_totals(end(s))) for s in sides(m)])
    else:
        temp_root = root(m)
        # return tree(root(m), [side(length(s), with_totals(end(s))) for s in sides(m)])
    return tree(temp_root, [side(length(s), with_totals(end(s))) for s in sides(m)])


def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    def helper(m):
        if is_weight(m):
            return True, size(m)
        result = []
        for s in sides(m):
            side_result = helper(end(s))
            result += [[side_result[0], side_result[1], side_result[1] * length(s)]]
        if result[0][0] and result[1][0] and \
           result[0][2] == result[1][2]:
           return True, result[0][1] + result[1][1]
        else:
            return False, -1
    return helper(m)[0]



############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    incorrect_passwd = []
    def withdraw(amount, passwd):
        nonlocal incorrect_passwd
        nonlocal balance
        if len(incorrect_passwd) >= 3:
            return "Your account is locked. Attempts: ['{0}', '{1}', '{2}']".format(incorrect_passwd[0], incorrect_passwd[1], incorrect_passwd[2])
        if passwd != password:
            incorrect_passwd.append(passwd)
            return "Incorrect password"
        if amount > balance:
           return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    def joint(amount, passwd):
        if passwd == new_password:
            return withdraw(amount, old_password)
        return withdraw(amount, passwd)
    result = withdraw(0, old_password)
    if type(result) == str:
        return result
    return joint



###########
# Objects #
###########

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item, price, stock=0):
        self.item = item
        self.price = price
        self.stock = stock
        self.money = 0

    def vend(self):
        if self.stock <= 0:
            return "Machine is out of stock."
        if self.money < self.price:
            return "You must deposit ${0} more.".format(self.price-self.money)
        else:
            remain = self.money - self.price
            if remain > 0:
                s = 'Here is your {0} and ${1} change.'.format(self.item, remain)
            else:
                s = 'Here is your {0}.'.format(self.item)
            self.money = 0
            self.stock -= 1
            return s

    def restock(self, num):
        self.stock += num
        return 'Current {0} stock: {1}'.format(self.item, self.stock)

    def deposit(self, money):
        if self.stock <= 0:
            return 'Machine is out of stock. Here is your ${}.'.format(money)
        self.money += money
        return 'Current balance: ${0}'.format(self.money)


        
class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, item):
        self.item = item

    def ask(self, s, *args):
        assert type(s) == str
        index = s.find(' ')
        if s[:index] != "please":
            return 'You must learn to say please first.'
        method = s[index+1:]
        if not hasattr(self.item, method):
            return 'Thanks for asking, but I know not how to {0}.'.format(method)
        return getattr(self.item, method)(*args)



#############
# Challenge #
#############


