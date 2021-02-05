from email_address import EmailAddress
from validator import Validator

# replace with path to csv file
INPUT_FILE = "suspicious.csv"

#get emails
unedited_emails = []
with open(INPUT_FILE) as data:
    for i, line in enumerate(data):
        email = EmailAddress(line, i)
        unedited_emails.append(email)

#validate emails
validator = Validator()
passed = []
failed = []
for email in unedited_emails:
    validator.has_curse_word(email)
    validator.has_test_word(email)
    validator.has_bad_domain(email)
    validator.has_bad_suffix(email)
    validator.is_gibberish(email)

#temp: print out results.  todo: replace with something nicer
count = 0
still_valid = []
for email in unedited_emails:
    if email.valid:
        count = count + 1
        still_valid.append(email.orginal_address)

print("total emails: {0}".format(len(unedited_emails)))
print("found invalid emails: {0}".format(count))
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
print("{0} emails is gibberish".format(len(validator.gibberish)))
print(validator.gibberish)
print("----")
print("{0} still valid".format(len(still_valid)))
print(still_valid)
