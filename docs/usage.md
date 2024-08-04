
**plan**
- social class impede certain spends
- put a saver type --> give an average and an std of spends for a person
- Types of spends = f(age, social_class, gender, location, religion, weight, height )
- Types of spends ==> simulation of the economy
- Black box = outside the city --> incoming flows and outgoing flows
- city --> class mutable 
  - interaction of people ==> new things : new companies

--> simulation every year then every week ... ms



- In a further way, define people with more specific data 
  - disease
  - body data so that having information about the metabolism of people 
  - That could specify other values as spends ... 

## First step

- more than 150 km2
- about 50,000 people ==> 15000
- 30 % retiree (age : avg 70, std = 10 
  - 50 %  earn €[avg : 1300, std : 350], rent (avg : 400, std : 100)
  - 30 % (avg : 2000, std : 300), rent
  - 
- 20 % minor ==> 10000
  - [0 - 3[ ==> 13 % ==> 1300
  - [3 - 11[ ==> 44 % ==> 4400
    - 4 public primary schoolS --> 700 students / school
      - from 3 to 11
      - 1 teacher / 25 student
    - 2 private primary schoolS --> 
      - (from 3 to 11)
      - 1 teacher / 20 student
      - (€3000 a year)
  - [11 - 18[ ==> 43 % ==> 4300
  - 2 public high school 
    - (from 11 to 18) 
    - one teacher for 22 students
  - 2 private high school 
    - (from 11 to 18)
    - (€ 5000 a year for first 4 years and € 7000 for the last 3 years)
    - one teacher from 19 students
- 10 % student
- Employment (age : avg = 40, std = 20)
  - artisan retailer
    - baker
    - hairdresser
    - butcher
    - fishmonger
    - car dealer and car mechanic
    - florist
    - 

Proba (avg and std) of people to go to each artisan retailer
  --> avg spend (with std) depend on jobs
  --> How many times per year/ month/ week/ day
  --> Which interval of time (avg std ex : every 3 weeks with std of 2 days)
  --> Take into account the spend of children depending on their parent's job
  --> take into account day off of people and artisan retailer 
  --> people go to the nearest artisan retailer
    --> if closed --> the second nearest and so on ...

--> some flat and house belongs to people in the ciy 
  --> some people give a rent other people in the city
--> people can earn money from assets (outside the city --> blackbox)
--> don't forget taxes (round taxes for easier computing)
--> retiree and unemployed major earn money from the state (black box)
--> some people earn a salary from flew coming from elsewhere (black box)

--> Big Companies : 
  --> Safran (Factory) : 1500, gdp/person employee : € 250,000 ==> € 375 M
      - Engineering :
        - Director of Engineering : 1, salary : € 120,000
    --> Presta : 500, gdp/person employee : € 120,000 ==> € 60 M
    
  --> Orange (Telecom shop) : 10, gdp/person employee : € 310,000 ==> € 3.1 M
  --> Factory 2 (Factory) : 200, gdp/person employee : € 130,000 ==> € 26 M
  --> Factory 3 (Factory) : 200, gdp/person employee : € 120,000 ==> € 24 M
Shop


--> City subdivided in district 
  - Factory District
  - Agricola District1
  - Secondary city center near Factories and Fields
  - Commercial District (big commercial area and some residence)
  - Main city center (Historical buildings, residence, artisan retailer)
  - Residential District 1 for rich people
  - Residential District 2 for poor people
  - Residential District 3 for middle class

1 butcher / 3000 people
1 bakery / 2000 people
1 flower shop / 
1 fast food / 1000 people
1 restaurant / 1000 people
  

