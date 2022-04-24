import streamlit as st

def app():

    
    # title
    st.title('Main Page')
    st.subheader('Welcome to Employment Checker 👋!')
    st.markdown(
        """
    Employment Checker is an interactive web application that helps you to check the employment status across countries. Here at Employment Checker, we visualized the changing trend of employment situation in both the United States and China, compared employment situation with COVID-19, and predicted using recurrent neural network. 
        
        """
    )

    # expander
    with st.expander("Where to find our data?"):
        st.markdown(
            """
            - **Github:** <https://github.com/yuxi-fan/empolyment-web>
            """
        )

    st.title("Sitemap")

    # intro of pages
    st.subheader('📊 Visualizations')
    st.write('In this page, we dive into the employment level across different industries and companies. We also cast light on the  unemployement rate, as well as employment level, together with COVID-19 situation from Jan 2020 to Feb 2022.')
    with st.expander("See details"):
        st.write("""
            The image below shows the overview of the page visualizations.
        """)
        st.image('pics/page2.png')

    st.subheader('👔 Unemployment rate for major cities')   
    st.write('In this page, we explore the detailed unemployement rate of 7 major cities in the United States. By selecting the citites on the left sidebar, you can easily see the line graph of chosen city, as well as the comparison between different major cities.')
    with st.expander("See details"):
        st.write("""
            The image below shows the overview of the page Unemployment rate for major cities.
        """)
        st.image('pics/page3.png')

    st.subheader('📈 Prediction Model')
    st.write('In this page, we apply Long Short-Term Memory (LSTM) to predict employment level of the United States based on previous COVID-19 cases and time series.')
    with st.expander("See details"):
        st.write("""
            The image below shows the overview of the prediction model.
        """)
        st.image('pics/page4.png')

    st.subheader('🇺🇸 US Heatmap')
    st.write('In this page, we present the heatmap that depicts the latest unemployment rate in the United Stats. Each cell reports a numeric count of unemployment rate, with larger counts associated with darker colorings. By clicking the color palette on the left side, you can see the corresponding states that falls into the chosen unemployment range.')
    with st.expander("See details"):
        st.write("""
            The image below shows the overview of the US Heatmap.
        """)
        st.image('pics/page5.png')

    st.subheader('🌎 China and the US comparison')
    st.write('In this page, we compare the unemployment rate in both China and the United States through water drop visualization effect. By clicking different year button, you can see the change in unemployment rate across countries.')
    with st.expander("See details"):
        st.write("""
            The image below shows the overview of unemployment rate of China vs US.
        """)
        st.image('pics/page6.png')

    