#Packages
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

#App Title
st.title("Do you need to pickle your dice?") #This is a reference to the not another dnd podcast podcast


#Need to have a place to store data

if 'roll' not in st.session_state: 
    st.session_state['roll'] = []


#Place to put in the dice roll/add in

new_roll = st.number_input("Enter your d20 roll here: ")


#We want a button here - to add the number in

if st.button("Add Number"):
    st.session_state['roll'] = []

#Button to reset all the rolls

if st.button("New session! (Reset)"): 
    st.session_state['roll'] = []

#Plotting logic

if st.session_state['roll']: 
    #We want a histogram plot of dice rolls
    fig, ax = plt.subplots()
    ax.hist(st.session_state['roll'], bins = 10, density=True, alpha = 0.6, color = 'lightblue')

    #Plot the density curve
    density = np.histogram(st.session_state['data'], bins = 10, density = True )
    count,bins,ignored = density
    center = (bins[:1] + bins[1:])/2
    ax.plot(center, count, 'k--', linewidth = 2)

    st.pyplot(fig)