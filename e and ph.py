import re

def valid_email(email):
    pattern = r'^[a-zA-Z0-9._#\\]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    return False

def valid_phnumber(phnumber):
    if len(phnumber) == 10 and phnumber.isdigit():
        country_codes = {
            '1': 'USA',
            '91': 'India',
            '44': 'UK',
            '81': 'Japan',
            '61': 'Australia',
            '49': 'Germany',
            '33': 'France'
        }
        country = country_codes.get(phnumber[:2], 'International number')
        return f"Valid {country} number"
    return "Invalid phone number"

print(valid_email("abc_e@mail123@gmail.com"))  
print(valid_email("hiii_email.com"))        
print(valid_phnumber("1234567890"))           
print(valid_phnumber("9187654321"))           
print(valid_phnumber("441234567890"))          
print(valid_phnumber("12345"))             