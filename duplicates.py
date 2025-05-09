import pandas as pd
import re
data = {
    'Name': ['John Doe', 'John Doe', 'Jane Smith', 'Jane Smith'],
    'Email': ['john.doe@gmail.com', 'john.doe+1@gmail.com', 'jane.smith@gmail.com', 'jane.smith+abc@gmail.com'],
    'Phone': ['9876543210', '9876543210', '8765432109', '8765432109'],
    'Aadhar': ['123456789012', '123456789012', '234567890123', '234567890123'],
    'PAN': ['ABCDE1234F', 'ABCDE1234F', 'XYZAB1234P', 'XYZAB1234P']
}
df = pd.DataFrame(data)
def normalize_email(email):
    return re.sub(r'(\+.*)(?=@)', '', email)
df['Normalized_Email'] = df['Email'].apply(normalize_email)
duplicates = df[df.duplicated(subset=['Normalized_Email', 'Phone', 'Aadhar', 'PAN'], keep=False)]
duplicate_aadhar = df[df.duplicated(subset=['Aadhar'], keep=False)]
duplicate_pan = df[df.duplicated(subset=['PAN'], keep=False)]
print("Duplicate Applications:")
print(duplicates)
print("\nDuplicate Aadhar Numbers:")
print(duplicate_aadhar)
print("\nDuplicate PAN Numbers:")
print(duplicate_pan)
