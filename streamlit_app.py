
##### This app is just an extremely simple example.
##### See the Streamlit documentation for how to create more complex apps.

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title( 'Brian(yt)\'s Glorious Table' )
df = pd.read_csv("National Universities Rankings.csv")
df['Tuition and fees'] = df['Tuition and fees'].str.replace(',', '').str.replace('$', '').astype(int)
df['In-state'] = df['In-state'].replace('nan', np.nan).str.replace(',', '').str.replace('$', '').astype(float)
df['Undergrad Enrollment'] = df['Undergrad Enrollment'].str.replace(',', '').astype(int)
df['state'] = df['Location'].str[-2:]

df['Private or Public'] = ""

for i in range(len(df)):
    if np.isnan(df.iloc[i, 5]):
        df.iloc[i,8] = 'Private'
    else:
        df.iloc[i,8] = 'Public'

df2 = df
 
constant_state = st.sidebar.multiselect('State', df.state.unique(), default=["MA"])
constant_state = list(constant_state)
range_of_list = st.sidebar.slider( label='Top X schools', min_value=1, max_value=20, value=10, step=1)
public_or_private_list = ["Public", "Private"]
private_or_public = st.sidebar.multiselect('Private or Public?', public_or_private_list, default=["Private"])
df2 = df2[df2["state"].isin(constant_state)]
df2 = df2[df2["Private or Public"].isin(private_or_public)]
df2 = df2.sort_values(by = "Rank")
df2 = df2.head(range_of_list)

st.write(df2)
fig , ax = plt.subplots()
ax.scatter(df2['Undergrad Enrollment'], df2['Tuition and fees'])
ax.set_xlabel('Undergrad Enrollment')
ax.set_ylabel('Tuition and Fees (in $)')
ax.set_title('Brian(yt)\'s Glorious Plot')
st.pyplot(fig)


# ##### Title and intro

# st.title( 'Example Streamlit App' )
# st.write( '''
# This app is very small and does almost nothing.
# It's just an example.
# ''' )


# ##### Inputs

# st.header( 'Choose two numbers' )
# a = st.slider( label='a', min_value=1, max_value=10, value=2, step=1 )
# b = st.slider( label='b', min_value=1, max_value=10, value=3, step=1 )


# ##### Output

# st.header( 'Tiny computations')
# st.write( f'{a} + {b} = {a+b}' )
# st.write( f'{a} - {b} = {a-b}' )
# st.write( f'{a} * {b} = {a*b}' )
# st.write( f'{a} / {b} = {a/b}' )
