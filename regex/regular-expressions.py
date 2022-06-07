# regular expressions, useful when doing validation, i'e password, email
import re
string = 'search inside of this text please!'
print('search' in string) # True

pattern = re.compile('this')

a = pattern.search(string)
b = pattern.findall(string)
c = pattern.fullmatch(string)
d = pattern.match(string)
print(a.span()) #(17, 21)
print(a.group()) # returns a string where there was a match
print(a.start())
#regex101.com
# Regular expression 2
# regular expression 3
# regex are great to use for validation

# email validation
# google email validation regex
pattern = re.compile(
r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
string = 'b@b.com'
a = pattern.search(string)
print(a)

# create a password checker, at least 8 character long
# can contain letters, numbers, $%#@
# has to end with a number
pattern2 = re.compile( r"[A-Za-z0-9$%#@]{8,}\d")
password = "ginafgyhes@#$%12"

check = pattern2.fullmatch(password)
print(check)


