1. Data Scraping: The data was scraped using the GitHub API, focusing on users in Berlin with over 200 followers.
2. Interesting Fact: The most surprising finding was the high correlation between the number of followers and the number of public repositories.
3. Recommendation: Developers should focus on creating more repositories to increase their visibility and follower count.


The data was collected using the GitHub API. Users in Berlin with over 200 followers were identified, and their public repositories were fetched. The data was cleaned and stored in CSV files.
Files:-
users.csv: Contains information about each user in Berlin with over 200 followers.
repositories.csv: Contains information about the public repositories of these users.
README.md: This file.
(Optional)
Codes: Contains python codes of all the set of operation performed

The data was cleaned to ensure consistency and accuracy. This included:
Trimming whitespace from company names.
1. Removing leading @ symbols from company names.
2. Converting company names to uppercase.


Analysis Details
1. Top 5 Users by Followers: Identified the users with the highest number of followers.
2. Earliest Registered Users: Found the users who registered earliest on GitHub.
3. Popular Licenses: Analyzed the licenses used in the repositories to find the most common ones.
4. Company Analysis: Determined which company employs the majority of these developers.
5. Programming Languages: Identified the most popular programming languages among these users.
6. Language Popularity Post-2020: Focused on users who joined after 2020 to find the second most popular language.
7. Stars per Language: Calculated the average number of stars per repository for each programming language.
8. Leader Strength: Defined as followers divided by (1 + following), and identified the top users based on this metric.
9. Followers vs. Repositories Correlation: Calculated the correlation between the number of followers and the number of public repositories.
10. Impact of Repositories on Followers: Used regression analysis to estimate the impact of the number of repositories on the number of followers.
11. Projects and Wikis Correlation: Analyzed the correlation between having projects and wikis enabled in repositories.
12. Hireable Users’ Following: Compared the average number of people followed by hireable users versus non-hireable users.
13. Bio Length Impact: Analyzed the impact of bio length on the number of followers using regression.
14. Weekend Repository Creation: Identified users who created the most repositories on weekends.
15. Email Sharing by Hireable Users: Compared the fraction of users sharing their email addresses based on their hireable status.Common Surnames: Analyzed the most common surnames among users.
