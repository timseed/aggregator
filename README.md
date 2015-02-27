# aggregator
Trying to emulate IBM Identity Insights using Python


This is a test project to see how easy (or difficult) it is to join semingly unconnected pieces of data together.

# Purpose
As we all live in an increasingly Digital Work - our data is spread over many site/locations. It makes it very difficult indeed to build up a true picture of a person/entity etc.

However this entity aggregation is becoming a very useful way of looking at data - especially in a BIG-DATA Context.

# Does this work ?
My test data ... yes - becuase there are no data clashes. Every record has a unique match. The real (and much more difficult job) will be to make the best fit - when say you have 1 Million "John Smiths" or whatever the most common chinese name is (Currently: Zhang Wei).

# Graphical Output ?
I have  - but not in this release.

# Can I add other data files ?
Yes - but you will have to edit the Main.py; This however can be easily automated using command line - or an XML config file.

# Persistance ? 
Not yet - depending on your data set - pickle is not suitable when you have more data than memory; Sqlite3 works well upto 50M records on Python. After that you will need a more traditional and powerful RDBMS. All easily accomplished.


