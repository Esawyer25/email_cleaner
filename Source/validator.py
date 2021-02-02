
class Validator():
  # add words to exclude here
  TEST_WORDS = ["test"] #words that indicate test account
  CURSE_WORDS = ["fuck"] 
  BAD_DOMAIN_WORDS = ["domain", "gmial"] #common invalid domains
  GOOD_SUFFIX = set(["com", "edu", "org"]) #allowed suffixes

  def __init__(self):
    self.contains_curses = []
    self.bad_domains = []
    self.contains_test = []
    self.bad_suffix = []

  def hasCurseWords(self, email):
    for word in self.CURSE_WORDS:
      if word in email.orginal_address:
        self.contains_curses.append(email.orginal_address)

  def hasTest(self, email):
    for word in self.TEST_WORDS:
      if word in email.orginal_address:
        self.contains_test.append(email.orginal_address)

  def hasBadDomain(self, email):
    for word in self.BAD_DOMAIN_WORDS:
      if word in email.domain:
        self.bad_domains.append(email.orginal_address)
      elif email.domain == "":
        self.bad_domains.append(email.orginal_address)

  def hasBadSuffix(self, email):
    if email.suffix not in self.GOOD_SUFFIX:
      self.bad_suffix.append(email.orginal_address)