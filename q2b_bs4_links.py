from bs4 import BeautifulSoup

html = '''
<html>
  <head><title>Cyber Security Portal</title></head>
  <body>
    <a href="https://owasp.org">OWASP</a>
    <a href="https://cert-in.org.in">CERT-In</a>
    <a href="https://github.com">GitHub</a>
  </body>
</html>
'''

soup = BeautifulSoup(html, "html.parser")
print("Page Title:", soup.title.string if soup.title else "No Title")
print("Hyperlinks:")
for link in soup.find_all("a", href=True):
    print("-", link["href"])
