from email_address import EmailAddress
from validator import Validator

unedited_emails = []

with open("suspicious.csv") as data:
    for i, line in enumerate(data):
        email = EmailAddress(line, i)
        unedited_emails.append(email)

validator = Validator()
passed = []
failed = []
for email in unedited_emails:
    validator.hasCurseWords(email)
    validator.hasTest(email)
    validator.hasBadDomain(email)
    validator.hasBadSuffix(email)


print("{0} emails with a bad suffix".format(len(validator.bad_suffix)))
print(validator.bad_suffix)
print("----")
print("{0} emails with a bad domain".format(len(validator.bad_domains)))
print(validator.bad_domains)
print("----")
print("{0} emails with a curse word".format(len(validator.contains_curses)))
print(validator.contains_curses)
print("----")
print("{0} emails with a test word".format(len(validator.contains_test)))
print(validator.contains_test)
print("----")