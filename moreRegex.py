import re

phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
message = 'Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim 508-123-4786 cupidatat excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip amet voluptate voluptate dolor minim nulla est proident. Nostrud officia 555-666-1833 pariatur ut officia. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia dolor Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit commodo ex non excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea consectetur et est culpa et culpa duis.'

print(phoneRegex.findall(message))
vowelcount = re.compile(r'[aeiouAEIOU]')
constanantscount = re.compile(r'[^aeiouAEIOU\s]')
print(len(vowelcount.findall(message)))
print(len(constanantscount.findall(message)))
print(len(message))
