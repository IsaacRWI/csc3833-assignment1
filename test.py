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

catSelection = alt.selection_point(
    fields=["Region"],
    bind="legend"
)

catColor = alt.condition(
    catSelection,
    alt.Color("Region:N"),
    alt.value("lightgray")
)


chart1 = alt.Chart(df).mark_point().encode(
    x="Interest Rate_percent",
    y="Inflation Rate_percent",
    # color = "Region:N"
    # color = alt.Color(
    #     "Region:N",  # "Region" is both the name in the legend and the reference for the data
    #     scale=alt.Scale(
    #         domain=["Europe", "Asia", "Africa", "Americas", "Oceania"],
    #         range=["blue", "red", "green", "orange", "purple"]
    #    )
    color=catColor,
        tooltip=[
            "Name",
            "Region",
            "Interest Rate_percent",
            "Inflation Rate_percent"
        ]
    ).add_params(
        catSelection
    )

chart1.save("interactive_scatter.html")

# chart1.save("global test.html")