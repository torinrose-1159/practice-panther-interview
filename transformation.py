import pandas as pd
import datetime as dt

def assignedTo(initials):
    match initials:
        case "GM":
            return "Gabe Michel"
        case "AA":
            return "Aaron Artsen"
        case "BL":
            return "Bond Liver"
        case "IC":
            return "Individual Contributor"
        case "TM":
            return "Tim Mint"
    
    # Checks for any initials outside of the expected values and does NOT assign to Gabe Michel - needs to be reviewed
    if(type(initials) == str):
        print(f"Unrecognized initials found in the 'Assigned' row: {initials}")
        return
    
    # Assigns blank values to Gabe Michel
    return "Gabe Michel"


# Provided file type was .xlsx, but same solution for .csv using pd.read_csv()
df = pd.read_excel("./Migration_Interview_Data (Python) (1).xlsx")
df.drop_duplicates(inplace=True)
df["First Name"] = df["First Name"].apply(lambda x: x.capitalize())
df["Middle Name"] = df["Middle Name"].apply(lambda x: x.capitalize())
df["Last Name"] = df["Last Name"].apply(lambda x: x.capitalize())
df["Date of Birth"] = df["Date of Birth"].apply(lambda x: dt.datetime.strptime(x, "%d/%m/%Y") if type(x) == str else x).apply(lambda x: dt.datetime.strftime(x, "%m/%d/%Y"))
df["Assigned"] = df["Assigned"].apply(lambda x: assignedTo(x))
df["ID"] = range(1, len(df)+1)
df = df.add_prefix("Contact: ")

df.to_csv("pythonOutput.csv", index=False)
