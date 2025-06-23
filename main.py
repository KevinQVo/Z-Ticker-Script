import streamlit as st

st.title("Zticker Cleaner")

# Input field for ztickers
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
        st.code(output_string)
        st.text_input("Click the copy icon on the right:", value=output_string, label_visibility="collapsed")
