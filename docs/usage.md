
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
  - 40 %  earn €[900, 1500], rent
- 10 % minor ==> 5000
  - [0 - 3[ ==> 13 % ==> 650
  - [3 - 11[ ==> 44 % ==> 2200
    - 2 public primary schoolS --> 700 students / school
      - from 3 to 11
      - 1 teacher / 25 student
    - 2 private primary schoolS --> 
      - (from 3 to 11)
      - 1 teacher / 20 student
      - (€3000 a year)
  - [11 - 18[ ==> 43 % ==> 2150
  - one public high school 
    - (from 11 to 18) 
    - one teacher for 22 students
  - one private high school 
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
