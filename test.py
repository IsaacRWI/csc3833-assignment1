import pandas as pd
import altair as alt

df = pd.read_csv("country_economics_data.csv")

print(df["Name"])

# europe = df.sort_values(by="Region")
europe = df[df["Region"] == "Europe"]
print(europe[["Name", "Interest Rate_percent"]])
# print(europe)
# print(europe.head(10))

chart = alt.Chart(europe).mark_point().encode(
    x="Interest Rate_percent",
    y="Inflation Rate_percent"
)

chart.save("europe test.html")