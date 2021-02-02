class EmailAddress():
  PREFIX_SPLITTER = "@"
  SUFFIX_SPLITTER = "."

  def __init__(self, address, line):
    self.orginal_address = address.strip()
    self.line = line
    self.valid = True
    self.breakdown_address()

  def breakdown_address(self):
    self.prefix = ""
    self.domain = ""
    self.suffix = ""

    try:
      #set prefix
      parts = self.orginal_address.split("@")
      self.prefix = parts[0].strip()

      #set service (ex. "gmail")
      domain_parts= parts[len(parts) - 1].split(".", 2)
      self.domain = domain_parts[0].strip()

      #set suffix (ex. ".com", ".co.uk")
      self.suffix = domain_parts[1].strip()
    except Exception as e:
      print("{0} is malformated: {1}".format(self.orginal_address, e.message))
