import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Smart Analytics Tool")

uploaded_file = st.file_uploader(
    "Upload a CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.subheader("Dataset Preview")
    st.dataframe(df.head())

    st.subheader("Missing Value Analysis")
    st.write(df.isnull().sum())

    st.subheader("Statistical Summary")
    st.write(df.describe())

    numeric_columns = df.select_dtypes(
        include='number'
    ).columns

    if len(numeric_columns) > 0:

        column = st.selectbox(
            "Select Column",
            numeric_columns
        )

        st.subheader("Histogram")

        fig = px.histogram(
            df,
            x=column
        )

        st.plotly_chart(fig)

        st.subheader("Box Plot")

        fig = px.box(
            df,
            y=column
        )

        st.plotly_chart(fig)

        if len(numeric_columns) >= 2:

            st.subheader("Scatter Plot")

            fig = px.scatter(
                df,
                x=numeric_columns[0],
                y=numeric_columns[1]
            )

            st.plotly_chart(fig)