# Beverages Inventory

This is a simple program that builds an SQLite database, which contains 3 tables:

        1. Brands 
    
        2. Producers
        
        3. Categories

Then it fills the tables with data given by a JSON file,
and enables the user to perform some interesting queries on it. 

The project includes a dummy JSON file, called "brands.json" that the program uses by default, when the user doesn't provide its own JSON file.

### Database Structure

It is easier to demonstrate the database structure with a real example. 

These are the 3 database tables filled with the data taken from "brands.json":

Brands:

| pk           | brand        | price        | producer_fk  | category_fk 
| ------------ | ------------ | ------------ | ------------ | ------------
| 1            | Coke         | 12           | 1            | 1           
| 2            | Fanta        | 12           | 1            | 1           
| 3            | Sprite       | 12           | 1            | 1           
| 4            | Fuze Tea     | 13           | 1            | 2           
| 5            | Minute Maid  | 8            | 1            | 3           
| 6            | Kinley       | 6            | 1            | 4           
| 7            | Pepsi        | 10           | 2            | 1           
| 8            | Mountain Dew | 10           | 2            | 1           
| 9            | 7 Up         | 10           | 2            | 1           
| 10           | Mirinda      | 11           | 2            | 1           
| 11           | Lipton Tea   | 12           | 2            | 2           
| 12           | Aquafina     | 5            | 2            | 4           
| 13           | Nestea       | 12           | 3            | 2           
| 14           | Ice Mountain | 7            | 3            | 4  

Producers:

| pk           | producer    
| ------------ | ------------
| 1            | Coca-Cola   
| 2            | PepsiCo     
| 3            | Nestle      

Categories:

| pk           |category    
| ------------ | ------------
| 1            | sparkling   
| 2            | iced tea    
| 3            | juice       
| 4            | water       

The "pk" (product key) column in every table is the table's primary key.

In addition, in the "Brands" table, 
"producer_fk" and "category_fk" are foreign keys reference "Producers.pk" and "Categories.pk" accordingly.


### Usage

Running the program with default options is very simple:

    python simulator.py
    
    
In order to use other JSON file than "brands.json":

    python simulator.py -br <path to your JSON file>
    
And in order to determine where the database is created:
 
    python simulator.py -db <path to prefereed DB location>

Otherwise, it will be created in your working directory.<br/><br/><br/>
For any more details run:

    python simulator.py -h

<br/><br/>

### User interface

Once the program is up it will present the user the following menu:

        Hello, what do you wish to do?
        1 - show DB
        2 - query something
        3 - quit

If the second option is chosen, the user will be suggested to perform the following queries:

        1 - get brands of producer
        2 - get brands of category
        3 - get brands of producer and category
        4 - count brands by producer
        5 - count brands by category
        6 - count brands by producer and category
        7 - get max priced brand
        8 - get max priced brand per producer
        9 - get max priced brand per category

The queries will print to the screen the results in a readable format.

Some queries require extra information, which will be presented to the user.

In any stage, the user can go back and observe the entire database.

Have Fun!

