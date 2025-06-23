import streamlit as st

st.title("Zticker Cleaner")

user_input = st.text_area("Enter ztickers (one per line):", height=200)

if user_input:
    lines = user_input.strip().split('\n')

    cleaned = []
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            cleaned.append(line[1:])
        else:
            st.warning(f"'{line}' is too short to clean")

    if cleaned:
        output_string = ' '.join(cleaned)
        st.subheader("Cleaned Output:")
        st.code(output_string)  # This has the built-in copy icon
