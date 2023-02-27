import requests
import json

def get_instance_metadata(metadata_key=''):
    try:
        # Query the metadata service
        metadata_url = "http://169.254.169.254/latest/meta-data/"
        response = requests.get(metadata_url + metadata_key)

        if response.status_code == 404:
            print(f"Metadata key {metadata_key} not found.")
            return None

        # If no metadata key is provided, return all metadata in a dictionary
        if not metadata_key:
            metadata_dict = {}
            metadata = response.text.strip().split("\n")
            for item in metadata:
                sub_key = item.rstrip("/")
                sub_response = requests.get(metadata_url + sub_key)
                sub_value = sub_response.text.strip()
                metadata_dict[sub_key] = sub_value
            return metadata_dict

        # If a metadata key is provided, return the corresponding value
        return response.text.strip()

    except requests.exceptions.RequestException as e:
        print(f"Error retrieving instance metadata: {e}")
        return None

# Retrieve all metadata keys and values in a dictionary
instance_metadata = get_instance_metadata()
if instance_metadata is not None:
    print(json.dumps(instance_metadata, indent=4))

# Retrieve a specific metadata key
metadata_key = "instance-id"
metadata_value = get_instance_metadata(metadata_key)
if metadata_value is not None:
    print(f"{metadata_key}: {metadata_value}")