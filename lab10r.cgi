#!/usr/bin/env ruby

require 'cgi'

cgi = CGI.new

# Retrieving form data
city = cgi['city']
province = cgi['province']
country = cgi['country']
picture_url = cgi['picture_url']

# Capitalizing city, province, and country names
city.capitalize!
province.capitalize!
country.capitalize!

# Generating HTML response
cgi.out('content-type' => 'text/html') do
  "<html>
  <head>
    <title>City Information - Ruby CGI</title>
  </head>
  <body>
    <div style='text-align: center; background-color: yellow; padding: 20px;'>
      <h1>#{city}, #{country}</h1>
    </div>
    <img src='#{picture_url}' style='width: 100%;' alt='#{city}'>
  </body>
  </html>"
end
