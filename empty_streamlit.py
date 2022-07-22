#import std libraries
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns
import plotly.express as px

# Write a title
st.title('welcome to the Penguin EDA')
st.write("**Starting** the *bilid* of `penguin` app :penguin: :mag:")

# Write data taken from https://allisonhorst.github.io/palmerpenguins/
st.write("Data is taken from [palmerpenguin](https://allisonhorst.github.io/palmerpenguins/)")

# Put image https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png
st.image("https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/man/figures/lter_penguins.png")
# Write heading for Data
st.header('Data')
# Read csv file and output a sample of 20 data points
df = pd.read_csv('penguins_extra.csv')
st.write('Display 20 points in dataset',df.sample(20))
# Add a selectbox for species
species = st.selectbox("Select whcih species we want", df.species.unique())

# Display a sample of 20 data points according to the species selected with corresponding title
st.write(f'Dispalying data point of {species}',df[df['species']==species])

# Plotting seaborn
fig, ax =plt.subplots()
ax = sns.scatterplot(data=df, x='bill_length_mm', y='flipper_length_mm' ,hue='species')
st.pyplot(fig)

# Plotting plotly
fig = px.scatter(data_frame=df,x='bill_length_mm', y='flipper_length_mm' ,color='species', animation_frame='species',range_x=[0,100],range_y=[170,250])
st.plotly_chart(fig)


# Bar chart count of species per island
st.bar_chart(df.groupby('island')['species'].count())

# Maps
st.map(df)
st.write('fot mapping references checkout[deckgl](https://deckgl.readthedocs.io/en/latest/)')
# Reference https://deckgl.readthedocs.io/en/latest/
# Reference https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart
# sidebar comment
slider_choice= st.sidebar.select_slider('We can various',['yes','no'])

if slider_choice=='yes':
    st.write('yes selected')
else:
    st.write('no selected')

csv_variable= st.sidebar.file_uploader('Upload a csv file' ,type=['csv'])
if csv_variable is not None:
    df= pd.read_csv(csv_variable)
    st.write(df)

st.markdown(f"""
<style>
.stApp{{
    background-image: url(https://images.pexels.com/photos/209096/pexels-photo-209096.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)
}}
</style>
""",unsafe_allow_html=True)

