
class Validator():
  # add words to exclude here
  TEST_WORDS = ["test", "spam", "example", "+", "123", "456", "asdf", "aaaa", "jdj", "abcd"] #words that indicate test account
  CURSE_WORDS = ["fuck", "slut", "shit", "fu", "lmao", "suck"]
  GOOD_DOMAIN_WORDS = set(["gmail", "yahoo", "hotmail"]) #allowed domains
  GOOD_SUFFIX = set(["com", "edu", "org", "co.uk"]) #allowed suffixes
  VOWELS = set(["a", "e", "i", "o", "u"])

  def __init__(self):
    self.contains_curses = []
    self.bad_domains = []
    self.contains_test = []
    self.bad_suffix = []

  def hasCurseWords(self, email):
    if not email.valid:
      return

    for word in self.CURSE_WORDS:
      if word in email.orginal_address:
        self.contains_curses.append(email.orginal_address)
        email.valid = False

  def hasTest(self, email):
    if not email.valid:
      return

    for word in self.TEST_WORDS:
      if word in email.orginal_address:
        self.contains_test.append(email.orginal_address)
        email.valid = False

  def hasBadDomain(self, email):
    if not email.valid:
      return
    elif email.domain not in self.GOOD_DOMAIN_WORDS:
      self.bad_domains.append(email.orginal_address)
      email.valid = False
    elif email.domain == "":
      self.bad_domains.append(email.orginal_address)
      email.valid = False

  def hasBadSuffix(self, email):
    if not email.valid:
      return
    elif email.suffix not in self.GOOD_SUFFIX:
      self.bad_suffix.append(email.orginal_address)
      email.valid = False
  
  #todo: filter out emails with no vowels
  

