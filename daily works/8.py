# Data Scientist Career Checker (Interactive)

# taking user input
ai = input("Do you know AI? (yes/no): ").lower() == "yes"
ml = input("Do you know Machine Learning? (yes/no): ").lower() == "yes"
statistics_and_math = input("Do you know Statistics and Mathematics? (yes/no): ").lower() == "yes"
knows_python = input("Do you know Python? (yes/no): ").lower() == "yes"
knows_sql = input("Do you know SQL? (yes/no): ").lower() == "yes"

# condition
if ai and ml and statistics_and_math and knows_python and knows_sql:
    print("\n You are ready to become a Data Scientist!")
else:
    print("\n You need to improve in the following areas:")

    if not ai:
        print("- Learn AI")
    if not ml:
        print("- Learn Machine Learning")
    if not statistics_and_math:
        print("- Improve Statistics and Mathematics")
    if not knows_python:
        print("- Learn Python")
    if not knows_sql:
        print("- Learn SQL")