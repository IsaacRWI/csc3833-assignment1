import pandas as pd
import altair as alt
from vega_datasets import data

from test.test import catColor

df = pd.read_csv("country_economics_data.csv")

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
    color=catColor,
        tooltip=[
            "Name",
            "Region",
            "Interest Rate_percent",
            "Inflation Rate_percent",
            "Jobless Rate_percent"
        ]
    ).add_params(
        catSelection
    ))

chart4 = alt.Chart(df).mark_boxplot(extent=1.5,outliers=False).encode(
    x=alt.X("Region:N",title="Region",axis=alt.Axis(labelAngle=0)),
    y=alt.Y("GDP Growth_percent", title="GDP Growth (%)"),
    color=alt.Color('Region:N', legend=None),
    tooltip=["Region:N"],
).properties(
    width=400,
    height=400,
    title='GDP Growth by Region'
)


chart4.save("chart4.html")

# chart2 = chart1.encode(x="Jobless Rate_percent", y="Interest Rate_percent")
chart3 = chart1.encode(x="Jobless Rate_percent", y="Inflation Rate_percent")

final = alt.vconcat(chart4, chart3).resolve_legend(
    color='independent'
)

final.save("final.html")

