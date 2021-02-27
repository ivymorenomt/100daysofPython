### Day 10

I did most of [21 day data challenge](https://github.com/ivymorenomt/21DaysDataChallenge) code. 
The key takeaway in resolving programming challenges is that, read. Read the problem.
Read it one by one, and visualize how to resolve the issue

Example is the data challenge where: 
Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:

- Total Milk Production
- Total Revenue
- How much revenue did the cow farm make in the year 2020? 

Resolve total milk production first by:

    df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']

Resolve total revenue by:

    df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']

Then finally resolve revenue:

    year_2020 = df['Month'].str.contains('20-')
    tot_2020 = df[year_2020].sum()['Total Revenue']
    
How to come up with these solutions? 
In Total Milk production, think about the formula on how to calculate the total. Obviously, it would be monthly * number of cows
In Total Revenue - it's about the same but use total milk production and the price per pound

the df means Dataframe, I have used pandas library to store the data. 

While doing 100 days of code, i am also doing the 21 day challenge simultaneously so I won't lose my muscle memory on coding/ all the 
important things I have learned in data science/Machine Learning using these libraries.