# Election_Analysis

## Project Overview
We have been tasked with completing an audit of a local Colorado congresional election. Our goals are to:
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate receieved.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, BBEdit Text Editor v14.1.2, pylint 2.14.3

## Election Audit Results
The analysis of the election shows that:
- There were 369,711 total votes in the election.
- The vote share by county is as follows
	- Jefferson county cast 10.5% of the votes and 38,855 votes.
	- Denver county cast 82.8% of the votes and 306,055 votes.
	- Arapahoe county cast 6.7% of the votes and 24,801 votes.
- Denver county had the largest number of votes at 82.8%, and 306,055 votes.
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The candidate results were:
	- Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
	- Diana DeGette received 73.8% of the vote and 272,892 votes.
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
	- Diana DeGette, who received 73.8% of the vote and 272,892 votes.


See charts below for a breakdown of voter turnout by county, followed by election results by candidate:

County:


![voter_turnout_by_county](https://user-images.githubusercontent.com/35434608/175830754-7af0d9e7-4ff6-49d7-bd90-137b55f72ece.png)

Candidates:


![election_results_by_candidate](https://user-images.githubusercontent.com/35434608/175830762-60908afb-d49e-40ca-ad32-5149c399ee80.png)


## Overview of Election Audit
This challenge was completed using the ```csv``` and ```os``` python libraries. The bulk of the work was done by writing a script that opened a CSV file and reading data from it. Each line of the file was read in as a list and from that list we were able to extract the relavent data to use in our analysis. We did our work concerning the CSV file inside of a ```with``` statement as shown below:
```
# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
```

This helped keep things clean because the ```with``` statement will close your file for you once you exit its block of code. We ran through the rows of the file using a ```for``` loop and stored the candidates and their vote counts in a dictionary. We did the same for the counties and their vote counts.


We wrote our results to another text file also using a ```with``` statement but this time set to writing mode as shown below:
```
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
```

Here we looped through the dictionaries we created in the first half of the script and gathered the relavent information to write to our text file.

The pie charts were created using python library Matplotlib.


## Election-Audit Summary
This script was written with no prior assumptions about the candidates or geography of the election, except for the fact that the text output is flavored for tracking counties voting outcomes. This could easily be changed to track any scope of election, from small committees, to cities, all the way up to states. We would just need to add another block in the ```for``` loop that extracted data from the rows of the CSV file as shown below:
```
# For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county = row[1]

        # For example: Extract the state name from each row.
        state = row[3] 
```

Our script was written for a "first-past-the-post" voting system where you need a plurality of the votes, just more votes than anyone else. If an election required an absolute majority of votes, or at least 50.1%, we could add a third condition when determining the winning candidate in this block of code below:
```
# Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
```
Many countries including Austrailia, New Zealand, and Austria use some form of what is called Preferential voting where voters rank their choice of candidates, rather than just choosing one. Under this system candidates can achieve an absolute majority more frequently and voters can generally be more satisfied with the results. Though it would take some more work, our script could be modified to accurately audit this type of voting system as well. If there was another column in the CSV for rank, we would just have to loop through the CSV selecting for the highest rank for each candidate, and then the second highest rank, and so on, until a candidate achieved more than 50% of the votes. 











