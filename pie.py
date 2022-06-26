import matplotlib.pyplot as plt
import numpy as np

# Charles Casper Stockham: 23.0% (85,213)
# Diana DeGette: 73.8% (272,892)
# Raymon Anthony Doane: 3.1% (11,606)

candidate_percentage = np.array([23, 73.8, 3.1])
candidate_names = ["Stockham", "DeGette", "Doane"]

candidates = plt.pie(candidate_percentage, labels = candidate_names)
plt.title("Election Results by Candidate")
plt.show()


# Jefferson: 10.5% (38,855)
# Denver: 82.8% (306,055)
# Arapahoe: 6.7% (24,801)

county_turnout = np.array([10.5, 82.8, 6.7])
counties = ["Jefferson", "Denver", "Arapahoe"]

plt.pie(county_turnout, labels = counties)
plt.title("Voter Turnout by County")
plt.show()