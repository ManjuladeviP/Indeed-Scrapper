from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("<YOUR_API_TOKEN>")

# Prepare the Actor input
run_input = {
    "urls": [
        "https://www.crunchbase.com/organization/linkedin",
        "https://www.crunchbase.com/organization/twitter",
        "https://www.crunchbase.com/person/mark-zuckerberg",
        "https://www.crunchbase.com/person/elon-musk",
    ],
    "useBrowser": False,
}

# Run the Actor and wait for it to finish
run = client.actor("0K3HqBhFzzs0UoMOW").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)