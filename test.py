import requests

def validate_pincode(address, pincode):
    # Create the API URL with the pincode
    api_url = f"https://api.postalpincode.in/postoffice/New Delhi/{pincode}"
    
    # Send a GET request to the API
    response = requests.get(api_url)
    
    # Check if the response is successful
    if response.status_code == 200:
        data = response.json()
        
        # Check if the API returned any data
        if data and data[0]["Status"] == "Success":
            # Extract the post office details from the response
            post_office = data[0]["PostOffice"]
            
            # Iterate through the post offices to find a matching address
            for office in post_office:
                if address.lower() in office["Name"].lower():
                    return True
        else:
            return False
    else:
        return False

# Example addresses and PIN codes
correct_address1 = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"
correct_address2 = "374/B, 80 Feet Rd, State Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bangalore. 560050"
incorrect_address1 = "2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony, Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560095"
incorrect_address2 = "Colony, Bengaluru, Karnataka 560050"

# Validate addresses with PIN codes
pincode = "560050"
print(f"Is '{correct_address1}' with PIN code {pincode} valid? {validate_pincode(correct_address1, pincode)}")
print(f"Is '{correct_address2}' with PIN code {pincode} valid? {validate_pincode(correct_address2, pincode)}")
print(f"Is '{incorrect_address1}' with PIN code {pincode} valid? {validate_pincode(incorrect_address1, pincode)}")
print(f"Is '{incorrect_address2}' with PIN code {pincode} valid? {validate_pincode(incorrect_address2, pincode)}")
