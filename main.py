import streamlit as st

st.title("Zticker Cleaner")

# Input field for ztickers
user_input = st.text_area("Enter ztickers (one per line):", height=200)

if user_input:
    lines = user_input.strip().split('\n')

    cleaned = []
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            cleaned.append(line[1:])  # Remove only the first character
        else:
            st.warning(f"'{line}' is too short to clean")

    if cleaned:
        output_string = ' '.join(cleaned)
        st.subheader("Cleaned Output (click to copy):")
        st.text_input("Cleaned Output", value=output_string, label_visibility="collapsed")
