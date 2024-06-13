#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 16:08:10 2024

@author: Jasmine Chen
"""

import requests

# URL provided in the email
url = "https://nam12.safelinks.protection.outlook.com/?url=https%3A%2F%2Fsandboxneu-dot-yamm-track.appspot.com%2F2kwpLrXimslsFuTuWZI2I4vaEVssYJgb3aMBodxfM7qTtDQzMjwEeCASQEHSxrZOW6lDUU87ZHQ96g7dAq6t0DKrBWsBiQDM-7_3VCTSJuroByeBEB4TQMubo5muduKFxeO3eqpUbphrHXlw0D4bURLbeshubG1niCxJXzQ7arPBHFxpKRhcAbd0CoQTgSfZgACH3uE0EcmX6lZ5-O9cKbSfulKklwco4TjmZCXMQrs0Uuzm5bVD-_00lUI4pu1olJ4V0pg5X9uHCSZJKpPXqYNIN9tZDc-1CWJOZ9GtGXWO7AMgejaZYMBvDGE5wgnGfx1qTijkSPhdkbGwkzuol0TgSJ_TBFAtI5Tv9aTw0M7wgEBiXNmlKAroCETNospMewq7rXZYL7bPizUr0WSdkI7Y_nE9xueMPXJE5fQ&data=05%7C02%7Cchen.jasmi%40northeastern.edu%7Ce61fbdbc5264450fd76608dc89aa980d%7Ca8eec281aaa34daeac9b9a398b9215e7%7C0%7C0%7C638536613013791529%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=aZROgHC3i97hmnSkXXiJgbO53PmT32GD5oRAVejCvAs%3D&reserved=0"

# Make the request to the URL
response = requests.get(url)

# Raise an exception if the request was unsuccessful
response.raise_for_status()

# Parse the JSON response
data = response.json()

# Parse the data
sessions = data['sessions']
rounds = data['rounds']
participants = data['participantInfo']

# Map session IDs to participant IDs
session_to_participant = {}
for session in sessions:
    session_id = session['sessionId']
    participant_id = session['participantId']
    session_to_participant[session_id] = participant_id

# Calculate average scores for each participant
participant_scores = {}
for round in rounds:
    session_id = round['sessionId']
    score = round['score']
    participant_id = session_to_participant.get(session_id)
    
    if participant_id:
        if participant_id not in participant_scores:
            participant_scores[participant_id] = []
        participant_scores[participant_id].append(score)

# Compute average score for each participant
participant_avg_scores = {}
for participant_id, scores in participant_scores.items():
    average_score = sum(scores) / len(scores) if scores else 0
    participant_avg_scores[participant_id] = average_score

# Map participant IDs to participant names
participant_names = {p['participantId']: p['name'] for p in participants}

# Combine names and average scores into a list of tuples and sort by name
sorted_participant_scores = sorted(
    [(participant_names[participant_id], avg_score) for participant_id, avg_score in participant_avg_scores.items()],
    key=lambda x: x[0]
)

# Print results
for name, avg_score in sorted_participant_scores:
    print(f"Participant: {name}, Average Score: {avg_score:.2f}")
