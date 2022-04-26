
#counties=["Arapahoe","Denver","Jefferson"]
#print(len (counties))
#print(counties[:2])
#counties.append("El Paso")
#counties.insert(2,"El Ganso")
#counties.pop(2)  
#or .remove("El Ganso")
#counties[2]="Señorita Taladro"

#counties_dict={"arapahoe":422829, "Denver":463353, "Jefferson":432438}
#print(counties_dict.items ())
#print(counties_dict.keys ())
#print(counties_dict.values ())
#print(counties_dict.get ("Denver"))
#counties_dict.get ("Denver") 
#print(counties_dict["arapahoe"])
 #voting_data = []
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.insert(1,{"county":"El Pason", "registered_voters": 461149})
#voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#print(voting_data)
#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")
#yas=[1,2,3,4,5]
#x=0
#for x in yas:
#    if x in yas:
#        x=x+1
#        print("yes, it is in there")    
#    else:
#         print("not it is not")
#for county in counties:
#    print(county)
#candidate_votes = int(input("How many votes did you get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes} number of votes. "
#    f"The total number of votes in the election was {total_votes}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)


import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis","Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","analysis", "election_analysis.txt")
# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

     # Write three counties to the file.
     txt_file.write("Arapahoe, Denver, Jefferson")