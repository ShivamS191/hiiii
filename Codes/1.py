import csv

# Define the list to store user from Berlin
user_in_Berlin = []

# Read the CSV file with UTF-8 encoding
with open('user.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        location = row['location'].strip().lower()
        # Check if the user is from Berlin
        if 'Berlin' in location:
            user_in_Berlin.append({
                'login': row['login'],
                'followers': int(row['followers'])
            })

# Sort user based on followers in descending order
top_user = sorted(user_in_Berlin, key=lambda x: x['followers'], reverse=True)

# Extract the top 5 user logins
top_5_logins = [user['login'] for user in top_user[:5]]

# Print the result as a comma-separated list
print(','.join(top_5_logins))
