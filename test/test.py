import pandas as pd
import altair as alt
from vega_datasets import data

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


chart1 = (alt.Chart(df).mark_point().encode(
    # x="Interest Rate_percent",
    # y="Inflation Rate_percent",
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
            "Inflation Rate_percent",
            "Jobless Rate_percent"
        ]
    #).transform_filter(  # removes the regions from the legend as well so
    #catSelection
    ).add_params(
        catSelection
    ))

chart2 = chart1.encode(x="Interest Rate_percent", y="Inflation Rate_percent")
chart3 = chart1.encode(x="Jobless Rate_percent", y="Inflation Rate_percent")

chart4 = chart2 | chart3

chart4.save("interactive_scatter.html")

# chart1.save("global test.html")


countries = alt.topo_feature(data.world_110m.url, "countries")


#Grey background map displaying all countries
backgroundMap = alt.Chart(countries).mark_geoshape(
    fill='lightgray',
    stroke='white'
).properties(
    width=800,
    height=500
).project('equirectangular')
#Display all map layers
alt.layer(
    backgroundMap
)

# Choropleth map coloured by water quality
choropleth = alt.Chart(countries).mark_geoshape(
    stroke='white'
).encode(
    color=alt.Color(
        'Jobless Rate_percent:Q',
        title='Jobless Rate (%)',
        scale=alt.Scale(scheme='reds')
    ),
    tooltip=[
        alt.Tooltip('Name:N', title='Country'),
        alt.Tooltip('Jobless Rate_percent:Q', title='Jobless Rate (%)')
    ]
).transform_lookup(
    lookup='id',
    from_=alt.LookupData(
        df,
        'ID',
        ['Name', 'Jobless Rate_percent']
    )
).properties(
    width=800,
    height=500
).project('equirectangular')

# Combine map layers
mapChart = alt.layer(
    backgroundMap,
    choropleth
)

mapChart.save("map_test.html")