import streamlit as st
from pygwalker.api.streamlit import StreamlitRenderer


def main():

    # Set up Streamlit interface
    st.set_page_config(
        page_title="📈 Interactive Visualization Tool", page_icon="📈", layout="wide"
    )

    st.header("📈 Interactive Visualization Tool")
    st.write("### Welcome to interactive visualisation tool")

    # Render pygwalker
    if st.session_state.get("df") is not None:
        pyg_app = StreamlitRenderer(st.session_state.df)
        pyg_app.explorer()

    else:
        st.info("Please upload a dataset to use the interactive visualization tools")


if __name__ == "__main__":
    main()