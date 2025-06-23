import streamlit as st

st.title("Zticker Cleaner")

user_input = st.text_area("Enter ztickers (one per line):", height=200)

if user_input:
    lines = user_input.strip().split('\n')
    numbers = []

    for line in lines:
        line = line.strip()
        if line.startswith('z') and len(line) > 1:
            number = line[1:]
            if number.isdigit():
                numbers.append(number)
            else:
                st.warning(f"'{line}' is not valid (non-numeric after 'z')")
        else:
            st.warning(f"'{line}' is not a valid zticker")

    if numbers:
        output_string = ' '.join(numbers)

        st.subheader("Cleaned Output:")

        # Create two columns: one for display, one for copy
        col1, col2 = st.columns([3, 2])

        with col1:
            st.code(output_string)

        with col2:
            st.text_input("Copy", value=output_string, label_visibility="collapsed")
