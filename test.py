import pandas as pd

df = pd.read_csv("country_economics_data.csv")

print(df["Name"])

# europe = df.sort_values(by="Region")
europe = df[df["Region"] == "Europe"]
print(europe[["Name", "Region"]])