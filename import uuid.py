import uuid
existing_ids = set()

def generate_employee_id(full_name, dob):
    first3 = full_name[:3].upper()
    last3_dob = dob[-2:] + dob[-5:-3] + dob[:4][-1] 
    initials = ''.join([name[0] for name in full_name.split()]).upper()[::-1]
    employee_id = f"{first3}-{last3_dob}-{initials}"
    while employee_id in existing_ids:
        unique_suffix = str(uuid.uuid4())[:4].upper()
        employee_id = f"{first3}-{last3_dob}-{initials}-{unique_suffix}"
    existing_ids.add(employee_id)
    return employee_id

if __name__ == "__main__":
    print(generate_employee_id("NS ADITYA", "1995-07-14"))
    print(generate_employee_id("CH ABHI", "1988-11-23"))
    print(generate_employee_id("AG RAJESH", "1995-07-14"))  
