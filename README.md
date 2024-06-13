## Jasmine Chen - Caterpillar Challenge Fall 2024

### How to Run the Solution
1. Use Python 3.x & install the requests library using pip if it's not installed already
2. Download the Script
3. Run the script using Python

### Thought Process and Design
1. Understanding the requirements of the challenge: The goal was to fetch participant data, map sessions to participants, calculate their average scores, and print the scores.
2. Fetching Data: Using the requests library, I performed an HTTP GET request to retrieve the data from the provided URL. This step ensures that I have access to the JSON data needed for further processing. 
3. Parsing JSON: I extracted sessions, rounds, and participant information. This extraction is necessary to perform mapping and calculations.
4. Mapping sessions to participants By iterating through the sessions, I created a dictionary that maps session IDs to participant IDs. This allowed me to link scores from rounds to the correct participants.
5. Calculating average scores: For each round, I fetched the score and the corresponding session ID, then used mapping to find the participant ID. Scores were then aggregated for each participant, and averages were calculated by dividing the sum of scores by the number of scores.
6. Mapping participant names: A dictionary is created to map participand IDs to their names, allowing me to output meaningful results.
7. Printing results: Finally, I printed each participant's name and their average score, formatted to two decimal places for more clarity. The results are sorted by the participant names in ascending order.

### Technical Challenges
1. Handling JSON data: It was difficult to ensure that the JSON data was correctly parsed and handled, especially considering the potential changes in the data structure.
2. Mapping and aggregating data: I found it difficult to also correctly map session IDs to participant IDs and to accurately calculate average scores. These required careful iteration and dictionary management.
3. Error handling: Sometimes, I couldn't figure out what was wrong with my code or logic, so ensuring that the script handled the HTTP request errors and the missing or malformed data within the JSON response was most difficult. It was hard to change my code when I thought that my original code and logic was reasonable.

### Time Taken
The approximate time it took for me to complete this project was around 5 hours. This included understanding the requirements, writing the script, testing multiple trials and errors, and writing this README file. 
