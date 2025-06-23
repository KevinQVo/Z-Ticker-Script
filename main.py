import streamlit as st

st.title("Zticker Cleaner")

user_input = st.text_area("Enter ztickers (one per line):", height=200)

if user_input:
    lines = user_input.strip().split('\n')
    total_entries = len([line for line in lines if line.strip()])  # Ignore blank lines

    cleaned = []
    for line in lines:
        line = line.strip()
        if len(line) > 1:
            cleaned.append(line[1:])
        else:
            st.warning(f"'{line}' is too short to clean")

    if cleaned:
        output_string = ' '.join(cleaned)

        # Display counts
        st.info(f"📝 Total entries: {total_entries} | ✅ Cleaned outputs: {len(cleaned)}")

        # Display cleaned output
        st.subheader("Cleaned Output:")
        st.code(output_string)
