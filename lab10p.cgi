#!/usr/bin/python
import cgi
form = cgi.FieldStorage()
city = form.getvalue('city').upper()
province = form.getvalue('province').upper()
country = form.getvalue('country').upper()
picture_url = form.getvalue('picture_url')

print("Content-type: text/html\n")
print("<html>")
print("<head>")
print("<title>Lab 10 Problem 2</title>")
print("<style>")
print("""
    body {
        font-family: Arial, sans-serif;
        text-align: center;
        background-color: #f0f0f0;
        margin: 0;
        padding: 20px;
    }

    .header {
        background-color: #4CAF50;
        color: white;
        font-size: 36px;
        padding: 10px;
        margin-bottom: 20px;
    }

    .header span {
        color: red;
        font-weight: bold;
    }

    .city-image {
        width: 80%;
        height: auto;
        border: 10px solid #4CAF50;
        margin-bottom: 20px;
    }

    .province {
        font-weight: bold;
        font-size: 24px;
        color: #333;
    }
""")
print("</style>")
print("</head>")
print("<body>")
print("<div class='header'>")
print("<span>%s, %s</span>" % (city, country))
print("</div>")
print("<br>")
print("<img src='%s' class='city-image' alt='City Image'>" % picture_url)
print("<br>")
print("<p class='province'>%s</p>" % province)
print("</body>")
print("</html>")
