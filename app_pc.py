import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Hello Pycon Colombia 2025!", page_icon="🐍")

st.title("🐍 Hello Pycon Colombia 2025!")

# Create columns
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("**🎚️ Controls**") 

    # Sliders
    yes_value = st.slider("How many said 'Yes'?", min_value=0, max_value=100, value=75)
    no_value = st.slider("How many said 'No'?", min_value=0, max_value=100, value=25)

    st.markdown("**🎨 Colors**") 

    # Color selectors
    color_yes = st.selectbox("Color for 'Yes'", ["lightblue", "skyblue", "green", "lime", "gold"])
    color_no = st.selectbox("Color for 'No'", ["salmon", "red", "orange", "crimson", "gray"])

with col2:
    # Data and chart
    categories = ["Yes", "No"]
    values = [yes_value, no_value]
    colors = [color_yes, color_no]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.bar(categories, values, color=colors)
    ax.set_title("😊 Do you like the presentation so far? 😊", fontsize=12)
    st.pyplot(fig)




st.markdown("---")
st.caption("Made with ❤️ especially for PyCon Colombia 2025.")
