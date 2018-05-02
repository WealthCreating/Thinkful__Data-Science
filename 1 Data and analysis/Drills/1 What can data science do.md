### Below we have a series of questions for you to translate into a technical plan. For each question, describe how you would make it testable and translate it from a general question into something statistically rigorous. Write your answers down in a shareable document and submit the link below. 

---


#### 1. You work at an e-commerce company that sells three goods: widgets, doodads, and fizzbangs. The head of advertising asks you which they should feature in their new advertising campaign. You have data on individual visitors' sessions (activity on a website, pageviews, and purchases), as well as whether or not those users converted from an advertisement for that session. You also have the cost and price information for the goods.
* I would start by analyzing the sales of each good.
* If a good has a high conversion rate, but only makes up a small fraction of the total sales, I would not advertise that good.  * Then, I would look at the activity on the website for each good.
* If one of the goods has the highest activity but comparable sales to the other goods, the company would be better off advertising for the goods with lowest activity, because they have the most room to grow in new visits, which will relate to higher sales.

#### 2. You work at a web design company that offers to build websites for clients. Signups have slowed, and you are tasked with finding out why. The onboarding funnel has three steps: email and password signup, plan choice, and payment. On a user level you have information on what steps they have completed as well as timestamps for all of those events for the past 3 years. You also have information on marketing spend on a weekly level.
* If my web design company spends less on marketing over time, I would expect to see a correlation with the number of sign-ups.
* If the marketing costs have been the same or increased, I would look at which demographics are impacted by the marketing.
* If all marketing is targeting to the same demographic, additional marketing would not help to generate more signups.
* If there are demographic groups that we haven't advertised to, it may help expanding marketing to those groups.

### 3. You work at a hotel website and currently the website ranks search results by price. For simplicity's sake, let's say it's a website for one city with 100 hotels. You are tasked with proposing a better ranking system. You have session information, price information for the hotels, and whether each hotel is currently available.
* I would change the ranking to include a factor that accounts for how full a hotel is.
* If the cheapest hotel is full of customers, its ranking should lower to reflect that.
* Otherwise, the cheapest hotels would remain at the top of the list, no matter what their occupancy rate is.

### 4. You work at a social network, and the management is worried about churn (users stopping using the product). You are tasked with finding out if their churn is atypical. You have three years of data for users with an entry for every time they've logged in, including the timestamp and length of session.

* I would separate the users by how long they have been using the website, and look at the newest users.  
* If new users make up the largest percentage of the churn rate, we would need to make the website more friendly for new users. * This could be done by creating a guided tour when they sign up,ensuring visitors can easily access customer support, and  simplifying the starting pages.  
* If the highest churn is instead from users that have been on the site for years, I would see what changes the site has implemented over the years.  
* If the website structure is the exact same as three years ago and no new features have been added, the old users are bored 
with the website.
