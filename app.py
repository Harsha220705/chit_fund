import streamlit as st
import time
import pandas as pd
st.set_page_config(layout="wide")
st.title("Sri Guru Ragavendra Chit Funds")
st.markdown(
        """
        <style>
        pre code {
            font-size: 20px !important;
            line-height: 1.6;
        }
        .stDataFrame td {
        font-size: 16px;
    }

    /* Table header */
    .stDataFrame th {
        font-size: 16px;
        font-weight: 600;
    }
        </style>
        """,
        unsafe_allow_html=True
    )

st.code(
        "This chit fund encourages disciplined saving in an easy and organized manner.\n"
        "All payment details are clearly recorded, helping you track your money without confusion.\n"
        "It offers transparency, so you always know where your savings stand.\n"
        "This makes financial planning simpler and more reliable."
    )
def display_main():
    if st.button("13 Month",type="primary"):
        st.subheader("Welcome to 13 Month Plan: ")
        st.subheader("English")
        st.code(
            "English:\n"
            "Where you will be paying 6500 per month for up to 13 months, the breakdown will be displayed here.\n\n"
            "ಕನ್ನಡ:\n"
            "ಇಲ್ಲಿ ನೀವು ಪ್ರತಿ ತಿಂಗಳು 6500 ರೂಪಾಯಿಗಳನ್ನು 13 ತಿಂಗಳವರೆಗೆ ಪಾವತಿಸುತ್ತೀರಿ, ಅದರ ವಿವರಗಳನ್ನು ಇಲ್ಲಿ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ."
        )
        df = pd.DataFrame({
            "Serial Number": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
            "Date": [
                "01/05/2026", "02/05/2026", "03/05/2026", "04/05/2026",
                "05/05/2026", "06/05/2026", "07/05/2026", "08/05/2026",
                "09/05/2026", "10/05/2026", "11/05/2026", "12/05/2026",
                "01/05/2027"
            ],
            "Monthly_Payment": [6500] * 13,
            "Total_Amount": [
                70000, "Agent", 70000, 71000, 71000, 72000, 74000,
                76000, 78000, 80000, 84000, 90000, 100000
            ]
        })
        df.set_index('Serial Number')
        st.dataframe(df,use_container_width=True)


if __name__ == "__main__":
    display_main()

