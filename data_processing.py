import pandas as pd
from faker import Faker

# Initialize Faker
fake = Faker()

# Generate fake data
data = {
    'Name': [fake.name() for _ in range(10)],
    'Email': [fake.email() for _ in range(10)],
    'Phone': [fake.phone_number() for _ in range(10)]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Anonymize the 'Email' column using Faker
df['Email'] = df['Email'].apply(lambda x: fake.email())

# Show the anonymized DataFrame
print(df)