import os
from pyairtable import Table

api_key = os.environ["AIRTABLE_API_KEY"]

categories = Table(api_key, 'appNGShhkZe2XPPSW', 'Categories')
twitter = Table(api_key, 'appNGShhkZe2XPPSW', 'Twitter')

if __name__ == "__main__":
    print(categories.all())

## NEXT STEPS:
# - Fetch data from twitter API and from tiktok API (other files) 
# - Once grabbing likes from the input streams, they will be added to the corresponding airtable as a new record (https://pyairtable.readthedocs.io/en/latest/api.html)