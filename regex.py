import re

mo = re.compile(r'Bat(man|mobile)').search("Batman has a Batmobile but it is not a steal")
print(mo.group())

batRegex = re.compile(r'Bat(wo)+man')
print(batRegex.search('The Adventure of Batwoman'))

haRegex = re.compile(r'(Ha){3}')
print(haRegex.search('He said HaHaHa'))

digitRegex = re.compile(r'(\d){3,5}?')
digitRegexGreed = re.compile(r'(\d){3,5}')
print(digitRegex.search('123456789'))
print(digitRegexGreed.search('123456789'))
