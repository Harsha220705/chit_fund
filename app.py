import streamlit as st
import pandas as pd

# Page config
st.set_page_config(layout="wide")
st.title("Sri Guru Ragavendra Chit Funds")

# Styling
st.markdown(
    """
    <style>
    pre code {
        font-size: 20px !important;
        line-height: 1.6;
    }

    .stDataFrame td {
        font-size: 17px;
    }

    .stDataFrame th {
        font-size: 17px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Description
st.code("""
This chit fund encourages disciplined saving in an easy and organized manner.
All payment details are clearly recorded, helping you track your money without confusion.
It offers transparency, so you always know where your savings stand.
This makes financial planning simpler and more reliable.
""")

def display_main():
    if st.button("13 Month", type="primary"):
        st.subheader("Welcome to 13 Month Plan")

        st.code(
            "English:\n"
            "Where you will be paying 6500 per month for up to 13 months, the breakdown will be displayed here.\n\n"
            "ಕನ್ನಡ:\n"
            "ಇಲ್ಲಿ ನೀವು ಪ್ರತಿ ತಿಂಗಳು 6500 ರೂಪಾಯಿಗಳನ್ನು 13 ತಿಂಗಳವರೆಗೆ ಪಾವತಿಸುತ್ತೀರಿ, ಅದರ ವಿವರಗಳನ್ನು ಇಲ್ಲಿ ಪ್ರದರ್ಶಿಸಲಾಗುತ್ತದೆ."
        )

        # DataFrame with REQUIRED date format
        df = pd.DataFrame({
            "Serial Number": list(range(1, 14)),
            "Date": [
                "05/01/2026", "05/02/2026", "05/03/2026", "05/04/2026",
                "05/05/2026", "05/06/2026", "05/07/2026", "05/08/2026",
                "05/09/2026", "05/10/2026", "05/11/2026", "05/12/2026",
                "05/01/2027"
            ],
            "Monthly_Payment": ["6500"] * 13,
            "Total_Amount": [
                "70000", "Agent", "70000", "71000", "71000", "72000",
                "74000", "76000", "78000", "80000", "84000", "90000", "100000"
            ]
        })

        df.set_index("Serial Number", inplace=True)

        st.dataframe(df, width="stretch")

if __name__ == "__main__":
    display_main()