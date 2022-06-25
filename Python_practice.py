counties = ["Arapahoe", "Denver", "Jefferson"]


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


voting_data = [
    {"county": "Arapahoe", "registered_voters": 422829},
    {"county": "Denver", "registered_voters": 463353},
    {"county": "Jefferson", "registered_voters": 432438}
]
    

for i in range(len(voting_data)):
    county = voting_data[i]["county"]
    voters = voting_data[i]["registered_voters"]
    print(f"{county} has {voters:,} registered voters.")


