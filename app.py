"""
# 2024 Streamlit Cheat Sheet

2024 Streamlit Cheatsheet App v1.31.0

https://github.com/themindfuldude/2024-streamlit-cheat-sheet-app

v1.31.0 August 2024

Author:
* @themindfuldude : https://github.com/themindfuldude/

# Version
* 2024 Streamlit v1.31.0
* Python 3.11

"""

# Import necessary libraries
import streamlit as st
from pathlib import Path
import base64

# Set initial page configuration
st.set_page_config(
     page_title='2024 Streamlit cheat sheet',
     layout="wide",
     initial_sidebar_state="expanded",
)

# Define the main function
def main():
    # Display the sidebar
    cs_sidebar()
    # Display the main body of the cheat sheet
    cs_body()

    return None

# Function to convert image to bytes
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

# Function to display the sidebar content
def cs_sidebar():
    # Display the logo and header
    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](https://streamlit.io/)'''.format(img_to_bytes("logomark_website.png")), unsafe_allow_html=True)
    st.sidebar.header('2024 Streamlit Cheat Sheet')

    # Display author information
    st.sidebar.markdown('''
<small>Gregory Kennedy [Linkedin](https://www.linkedin.com/in/gregorykennedymindfuldude/), [Github](https://github.com/themindfuldude).</small>
    ''', unsafe_allow_html=True)

    # Display installation and import instructions
    st.sidebar.markdown('__Install and import__')
    st.sidebar.code('$ pip install streamlit')
    st.sidebar.code('''
# Import convention
>>> import streamlit as st
''')

    # Display adding widgets to sidebar instructions
    st.sidebar.markdown('__Add widgets to sidebar__')
    st.sidebar.code('''
# Just add it after st.sidebar:
>>> a = st.sidebar.radio(\'Choose:\',[1,2])
    ''')

    # Display magic commands
    st.sidebar.markdown('__Magic commands__')
    st.sidebar.code('''
'_This_ is some __Markdown__'
a=3
'dataframe:', data
''')

    # Display command line instructions
    st.sidebar.markdown('__Command line__')
    st.sidebar.code('''
$ streamlit --help
$ streamlit run your_script.py
$ streamlit hello
$ streamlit config show
$ streamlit cache clear
$ streamlit docs
$ streamlit --version
    ''')

    # Display pre-release features and links
    st.sidebar.markdown('__Pre-release features__')
    st.sidebar.code('''
pip uninstall streamlit
pip install streamlit-nightly --upgrade
    ''')
    st.sidebar.markdown('<small>Learn more about [experimental features](https://docs.streamlit.io/library/advanced-features/prerelease#beta-and-experimental-features)</small>', unsafe_allow_html=True)

    # Display footer
    st.sidebar.markdown('''<hr>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<small>[2024 Cheat sheet v1.31.0](https://github.com/themindfuldude/2024-streamlit-cheat-sheet-app)  | Apr 2024 | [Gregory Kennedy](https://github.com/themindfuldude)</small>''', unsafe_allow_html=True)

    return None

# Main body of the cheat sheet
def cs_body():
    # Create three columns
    col1, col2, col3 = st.columns(3)

    # COLUMN 1
    # Display text instructions
    col1.subheader('Display text')
    col1.code('''
st.write("Most objects") # df, err, func, keras!
st.write(["st", "is <", 3]) # see *
...
    ''')

    # Display data instructions
    col1.subheader('Display data')
    col1.code('''
st.dataframe(my_dataframe)
st.table(data.iloc[0:10])
...
    ''')

    # Display media instructions
    col1.subheader('Display media')
    col1.code('''
st.image("./header.png")
st.audio(data)
...
    ''')

    # Display instructions for two equal columns
    col1.subheader('Two Equal Columns')
    col1.code('''
col1, col2, col3 = st.columns([3,1,1])
# col1 is larger
...
    ''')

    # Display tabs instructions
    col1.subheader('Tabs')
    col1.code('''
# Insert containers separated into tabs:
>>> tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
...
    ''')

    # Display control flow instructions
    col1.subheader('Control flow')
    col1.code('''
# Stop execution immediately:
st.stop()
...
    ''')

    # Display personalize apps for users instructions
    col1.subheader('Personalize apps for users')
    col1.code('''
# Show different content based on the user's email address.
>>> if st.user.email == 'jane@email.com':
...
    ''')

    # COLUMN 2
    # Display interactive widgets instructions
    col2.subheader('Display interactive widgets')
    col2.code('''
st.button("Click me")
...
    ''')

    # Display build chat-based apps instructions
    col2.subheader('Build chat-based apps')
    col2.code('''
# Insert a chat message container.
>>> with st.chat_message("user"):
...
    ''')

    # Display mutate data instructions
    col2.subheader('Mutate data')
    col2.code('''
# Add rows to a dataframe after
...
    ''')

    # Display display code instructions
    col2.subheader('Display code')
    col2.code('''
st.echo()
>>> with st.echo():
...
    ''')

    # Display placeholders, help, and options instructions
    col2.subheader('Placeholders, help, and options')
    col2.code('''
# Replace any single element.
>>> element = st.empty()
...
    ''')

    # COLUMN 3
    # Display connect to data sources instructions
    col3.subheader('Connect to data sources')
    col3.code('''
st.connection("pets_db", type="sql")
...
    ''')

    # Display optimize performance instructions
    col3.subheader('Optimize performance')
    col3.write('Cache data objects')
    col3.code('''
# E.g. Dataframe computation, storing downloaded data, etc.
>>> @st.cache_data
...
    ''')
    col3.write('Cache global resources')
    col3.code('''
# E.g. TensorFlow session, database connection, etc.
>>> @st.cache_resource
...
    ''')
    col3.write('Deprecated caching')
    col3.code('''
>>> @st.cache
...
    ''')

    # Display progress and status instructions
    col3.subheader('Display progress and status')
    col3.code('''
# Show a spinner during a process
>>> with st.spinner(text="In progress"):
...
    ''')

    return None

# Run main function
if __name__ == '__main__':
    main()
