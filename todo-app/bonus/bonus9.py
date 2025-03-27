import re

password = (input("Enter new password: ")).strip()

result = {
    'length': False,
    'numeric': False,
    'uppercase': False,
}

if len(password) >= 8:
    result['length'] = True

if re.search("[0-9]", password) is not None:
    result['numeric'] = True

upper = False
for letter in password:
    if letter.isupper():
        upper = True
result['uppercase'] = upper

if all(result.values()):
    print("Strong password!")
else:
    print("Weak password!")
    if not result['length']:
        print("Password should be 8 or more characters")
    if not result['numeric']:
        print("Password should have at least one number")
    if not result['uppercase']:
        print("Password should have at least one uppercase character")


