# -*- coding: utf-8 -*-
"""Electric_Vehicle_IN9240844_SSC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cfSnxNz_6677VBY_FLEphzbS_-iMkds4

# ***Green Vechile EDA ***
## **Shiva Sai Chakradhar**
### **IN9240844**

# ***Objective***
we are going to Analysis on Electric Vehicle Population Data Which has one lakh+ rows and 15+ columns in the dataset where going to do univariate and bivariate analysis on the electric vechicle data also create map using plotypy and moving graph of the total vechiles sold by each company each year
"""

from google.colab import drive
drive.mount('/content/drive')

pip install bar-chart-race

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import bar_chart_race as bcr
import plotly.io as pio
import warnings

df=pd.read_csv(r"/content/drive/MyDrive/my projects/ELECTRIC_VECHILE/dataset.csv")

df.columns

df.head()



df.info()

df.describe()

df.shape

df.isnull().sum()

df.dropna(inplace = True)

df.shape

"""# **Univariate_Analysis**"""

pip install plotly

import plotly.express as px

Ev_type = px.density_heatmap(df["Electric Vehicle Type"].value_counts(), title = "Count of Ev Types")
Ev_type.show()

CAFV_eigibility = px.funnel(df["Clean Alternative Fuel Vehicle (CAFV) Eligibility"].value_counts(), title = "Count of CAFV Eligibility")
CAFV_eigibility.show()

E_range = px.histogram(df,x="Electric Range",nbins = 30,title = "Distribution of Electric Range")
E_range.show()

Base_msrp = px.histogram(df,
                         x="Base MSRP",
                         nbins=30,
                         range_x=[0, 210000],
                         color_discrete_sequence=px.colors.sequential.Viridis)
Base_msrp.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    bargap=0.3,
    title=dict(text="Distribution of Base MSRP", x=0.5)
)
Base_msrp.show()



company_counts = df['Make'].value_counts().reset_index()
company_counts.columns = ['Company', 'EV Count']
company_counts = company_counts.sort_values(by='EV Count', ascending=False)

fig_bar = px.bar(company_counts, x='Company', y='EV Count',
                 title='No of Electric Vehicles by Company',
                 color='Company',
                 color_discrete_sequence=px.colors.qualitative.Prism)


fig_bar.update_layout(
    plot_bgcolor='#f0f0f0',
    paper_bgcolor='#ffffff',
    title=dict(text='No of Electric Vehicles by Company', x=0.5),  # Center the title
)
fig_bar.show()

county_counts = df['County'].value_counts().reset_index()
county_counts.columns = ['County', 'EV Count']
county_counts = county_counts.sort_values(by='EV Count', ascending=False)
fig_bar = px.bar(county_counts,
                 x='County',
                 y='EV Count',
                 color='County',
                 color_discrete_sequence=px.colors.qualitative.Pastel)
fig_bar.update_layout(
    plot_bgcolor='#808080',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title=dict(text='No of Electric Vehicles by Country', x=0.5)
)
fig_bar.show()





import plotly.express as px
model_year_counts = df['Model Year'].value_counts().reset_index()
model_year_counts.columns = ['Model Year', 'Count']
model_year_counts.sort_values(by='Model Year', inplace=True)
fig_model_year = px.bar(model_year_counts,
                        x='Model Year',
                        y='Count',
                        labels={'Model Year': 'Model Year', 'Count': 'Count'},
                        color='Model Year',
                        color_discrete_sequence=px.colors.qualitative.Dark2)


fig_model_year.update_layout(
    plot_bgcolor='#FFFFE0',
    paper_bgcolor='#FFFFE0',
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title=dict(text='Electric Vehicles Count by Model Year', x=0.5)  # Center the title
)
fig_model_year.show()



ev_type_counts = df['Electric Vehicle Type'].value_counts().reset_index()
ev_type_counts.columns = ['Electric Vehicle Type', 'EV Count']
ev_type_counts = ev_type_counts.sort_values(by='EV Count', ascending=False)
fig_bar = px.bar(ev_type_counts,
                 x='Electric Vehicle Type',
                 y='EV Count',
                 title='No of Electric Vehicles by EV Type',
                 color='Electric Vehicle Type',
                 color_discrete_sequence=['pink',"black"])

fig_bar.update_layout(
    barmode='group',
    bargap=0.3,
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title=dict(text='No of Electric Vehicles by EV Type', x=0.5)
)

fig_bar.show()

electric_utility_counts = df['Electric Utility'].value_counts().reset_index()
electric_utility_counts.columns = ['Electric Utility', 'EV Count']
top_10_utilities = electric_utility_counts.head(10)

fig_bar = px.bar(top_10_utilities,
                 x='Electric Utility',
                 y='EV Count',
                 title='Electric Vehicles Count by Electric Utility',
                 color_discrete_sequence=['red'])  # Red bars

fig_bar.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title=dict(text='Electric Vehicles Count by Electric Utility', x=0.5),
     height=800,
    width=1400
)

fig_bar.show()

"""### Bivariate analysis"""

import plotly.express as px
scatter_ev_range_msrp = px.scatter(df,
                                    x='Electric Range',
                                    y='Base MSRP',
                                    title='Electric Range vs Base MSRP',
                                    color='Electric Vehicle Type',
                                    size='Base MSRP',
                                    hover_name='Electric Vehicle Type',
                                    trendline='ols',
                                    color_discrete_sequence=px.colors.qualitative.Plotly)
scatter_ev_range_msrp.update_traces(marker=dict(opacity=0.8, line=dict(width=2, color='DarkSlateGrey')),
                                     selector=dict(mode='markers'))
scatter_ev_range_msrp.update_layout(
    plot_bgcolor='#eaeaf2',
    paper_bgcolor='#ffffff',
    xaxis=dict(showgrid=False, title='Electric Range (miles)', title_font=dict(size=14)),
    yaxis=dict(showgrid=False, title='Base MSRP ($)', title_font=dict(size=14)),
    title=dict(text='Electric Range vs Base MSRP', x=0.5, font=dict(size=20)),
)
scatter_ev_range_msrp.show()

""" Most vehicles are clustered at the lower end of both axes, indicating that many BEVs and PHEVs have a lower electric range and are priced lower. There is an outlier among BEVs with a significantly higher price but not necessarily a longer range."""



scatter_ev_range_model_year = px.scatter(df, x='Model Year', y='Electric Range', title='Electric Range vs Model Year')
scatter_ev_range_model_year.update_traces(
    marker=dict(symbol='triangle-up', size=10, color='red', opacity=0.7)
)

scatter_ev_range_model_year.update_layout(
    plot_bgcolor='#f0f0f0',
    paper_bgcolor='#ffffff',
    title=dict(text='Electric Range vs Model Year', x=0.5, font=dict(size=20)),
    xaxis=dict(title='Model Year', title_font=dict(size=14), showgrid=False),
    yaxis=dict(title='Electric Range (miles)', title_font=dict(size=14), showgrid=False),
)

scatter_ev_range_model_year.show()

Box_Ev_type_range = px.box(df, x='Electric Vehicle Type', y='Electric Range', title='Vehicle_Type vs Electric_Range')
Box_Ev_type_range.show()

scatter_model_year_ev_count = px.scatter(df['Model Year'].value_counts(), title='Number_of_Electric_Vehicles_by_Model_Year')
scatter_model_year_ev_count.show()

Box = px.box(df, x='Electric Vehicle Type', y='Base MSRP', title='Vehicle Type vs Base MSRP')
Box.show()

scatter_model_year = px.scatter(df, x='Model Year', y='Base MSRP', title='Model Year vs Base MSRP')
scatter_model_year.show()

Violin_ev_type = px.violin(df, x='Electric Vehicle Type', y='Electric Range', title='Vehicle Type vs Electric Range')
Violin_ev_type.show()

Fig_box = px.box(df, x='Clean Alternative Fuel Vehicle (CAFV) Eligibility', y='Electric Range',
                 title='Clean Alternative Fuel Vehicle Eligibility vs Electric Range',
                 labels={'Clean Alternative Fuel Vehicle (CAFV) Eligibility': 'CAFV Eligibility',
                         'Electric Range': 'Electric Range (miles)'})

Fig_box.show()

Mean_Electric_Range = df.groupby('Model Year')['Electric Range'].mean().reset_index()

Fig_line = px.line(Mean_Electric_Range, x='Model Year', y='Electric Range', title='Model Year vs Mean Electric Range',
                   labels={'Model Year': 'Model Year', 'Electric Range': 'Mean Electric Range (miles)'})

Fig_line.show()

df_counts = df.groupby(['Model Year', 'Electric Vehicle Type']).size().reset_index(name='Count')

fig_bar = px.bar(df_counts, x='Model Year', y='Count', color='Electric Vehicle Type',
                 title='Count of Different Vehicle Types based on Model Year',
                 color_discrete_sequence=px.colors.qualitative.Set3
                 )

fig_bar.update_layout(
    xaxis=dict(showgrid=False),
    yaxis=dict(showgrid=False),
    title=dict(x=0.5, font=dict(size=20)),
)

fig_bar.show()

"""# **Task 2**
showing that how many number of green vechiles sold each year in the each location from 1998 to 2023 according to the data availabe
displayed using choropleth which is in plotyexpress
"""

ev_count_by_pincode = df.groupby(['Postal Code', 'Model Year', 'State']).size().reset_index(name='Number_of_EV_Vehicles')
state_df = ev_count_by_pincode[ev_count_by_pincode['State'] == 'WA']
state_df.sort_values(by='Model Year', inplace=True)
Fig = px.choropleth_mapbox(state_df,
                           geojson="https://raw.githubusercontent.com/OpenDataDE/State-zip-code-GeoJSON/master/wa_washington_zip_codes_geo.min.json",
                           locations='Postal Code',
                           color='Number_of_EV_Vehicles',
                           featureidkey="properties.ZCTA5CE10",
                           mapbox_style="carto-positron",
                           zoom=5,  # Adjust zoom level
                           center={"lat": 47.7511, "lon": -120.7401},
                           title="Number of EV vehicles based on location Washington Over Time",
                           animation_frame="Model Year",
                           color_continuous_scale="Cividis",
                           hover_data=['Number_of_EV_Vehicles']
                          )
Fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
Fig.show()

"""# ***Task 3 Moving bar Chart***
going to visualize using bar chart how may vechiles sold by each company in each year from 1998 to 2023 which will be moving from 2023 to 1998
"""

a = df.groupby(['Make', 'Model Year']).size().reset_index(name='Number_of_Vehicles')
a.sort_values(by='Model Year',ascending=False,inplace=True)
fig = px.bar(a,
             y='Make',
             x='Number_of_Vehicles',
             animation_frame='Model Year',
             orientation='h',
             title='EV Makes and their Count Over the Years',
             labels={'Number_of_Vehicles': 'Number of EV Vehicles'},
             range_x=[0, 3000],
             color='Make',
             color_discrete_map={
                 'Tesla': 'red',
                 'Toyota': 'blue',
                 'Ford': 'green',
             }
             )
top_year = a['Model Year'].max()
if (a['Model Year'] == top_year).any():
    make_2023 = a.loc[a['Model Year'] == top_year, 'Make'].iloc[0]
    fig.add_annotation(x=2500, y=make_2023,
                       text=f"Most EVs: {top_year}",
                       showarrow=False,
                       font_size=18)
else:
    print("Year 2023 not found in data")
fig.update_layout(
    xaxis=dict(showgrid=True, gridcolor='LightGray'),
    yaxis_title='EV Makes',
    xaxis_title='Number of EV Vehicles',
    showlegend=False,
    title_x=0.5,
    title_font=dict(size=20),
    margin=dict(l=50, r=50, t=50, b=50),
    width=800,
    height=600,
    bargap=0.1)
fig.update_traces(
    texttemplate='%{x}',
    textposition='outside',
    textfont_size=16,
    width=1
)
fig.show()

"""according to visualisation done using electric vechile dataset the most vechiles were sold in 2023"""



