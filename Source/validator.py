from __future__ import division
from gibberish_utils import classify
import re
import math

class Validator():
  # add words to exclude here
  TEST_WORDS = ["www.", "test", "spam", "example", "123", "456", "asdf", "aaaa", "jdj", "abcd", "qwerty"] #words that indicate test account
  CURSE_WORDS = ["fuck", "slut", "shit", "fu", "lmao", "suck"]
  BAD_DOMAIN_WORD = ["guerrillamail", "gmial", "gmal", "yaho", "sharklasers", "hotmial", "domain"]
  GOOD_SUFFIX = set(["com", "edu", "org", "co.uk"]) #allowed suffixes
  VOWELS = set(["a", "e", "i", "o", "u"])

  # Used to exclude emails that are likely gibberish. 
  # Increase this to exclude fewer cases, decrease to exclude more
  HOME_KEY_PERCENTAGE = 70 

  def __init__(self):
    self.contains_curses = []
    self.bad_domains = []
    self.contains_test = []
    self.bad_suffix = []
    self.gibberish = []

#mark invalid if email address contains curse words
  def has_curse_word(self, email):
    for word in self.CURSE_WORDS:
      if word in email.orginal_address:
        self.contains_curses.append(email.orginal_address)
        email.valid = False

#mark invalid if email address contains test words
  def has_test_word(self, email):
    for word in self.TEST_WORDS:
      if word in email.orginal_address:
        self.contains_test.append(email.orginal_address)
        email.valid = False

# Mark invalid domain in bad domain list
  def has_bad_domain(self, email):
    for word in self.BAD_DOMAIN_WORD:
      if word in email.domain:
        self.bad_domains.append(email.orginal_address)
        email.valid = False

  #mark invalid if suffix is bad or missing
  def has_bad_suffix(self, email):
    if email.suffix not in self.GOOD_SUFFIX:
      self.bad_suffix.append(email.orginal_address)
      email.valid = False
    elif email.suffix == "":
      self.bad_suffix.append(email.orginal_address)
      email.valid = False

  def is_gibberish(self, email):
    if(home_keys_percentage(email.prefix) > HOME_KEY_PERCENTAGE):
      email.valid = False
      self.gibberish.append(email.orginal_address)
  
  #get percentage of characters that are in the home row
  #ex: "asdf" = 100%, "asdr" = 75%, "awer" = 25%
  def home_keys_percentage(text):
  home_keys = 0
  total = 0
  for c in text:
    if not c.isalpha():
      continue

    total += 1
    if c in "asdfghjklASDFGHJKL":
      home_keys += 1
  if total != 0:
    return home_keys / total * 100
  else:
    return 0  

