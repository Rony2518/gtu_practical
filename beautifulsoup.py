from bs4 import BeautifulSoup

# For HTML
html_doc = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
</body>
    <div class="container">
        <h2 class="box">Lorem ipsum dolor sit amet.</h2>
        <h2 class="box">Lorem ipsum dolor sit amet.</h2>
        <h2 class="box">Lorem ipsum dolor sit amet.</h2>
        <h2 class="box">Lorem ipsum dolor sit amet.</h2>
        <h2 class="box">Lorem ipsum dolor sit amet.</h2>
    </div>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# Now you can access the values in the HTML

count_h2 = soup.find_all('h2',class_="box")

for t in count_h2:
    print(t.text)
    
print(soup.title) # <title>The Dormouse's story</title>
print(soup.title.string) # The Dormouse's story

# For XML
xml_doc = """
<food>
<name>Belgian Waffles</name>
<price>$5.95</price>
<description>Two of our famous Belgian Waffles with plenty of real maple syrup</description>
<calories>650</calories>
</food>
"""

soup = BeautifulSoup(xml_doc, 'lxml-xml')

print(soup.food)

