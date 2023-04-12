import streamlit as st
from st_aggrid import AgGrid, GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
from streamlit_player import st_player
import pandas as pd

# =============================================================================
# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)
# =============================================================================

cosmo_language = 'english'

cosmo_language = st.radio('', ('english', 'german'), horizontal=True)

if cosmo_language == 'english':
    st.subheader('Welcome to the Introduction to Cosmochemistry')
else:
    st.subheader('Willkommen zur Einführung in die Kosmochemie')
    
# st.write('*für Mineralogen, Kosmo-/Geochemiker, Petrologen & den ganzen Rest*')

#---------------------------------#
#------ Vorlesungen & Übungen ----#
#---------------------------------#

@st.cache_data
def import_cosmo_videos():
    imp = pd.read_csv('data_cosmochemistry/videos_cosmochemistry.csv')
    return imp[imp['done'] == 'yes']
st.session_state.cosmo_videos = import_cosmo_videos()

@st.cache_data
def import_cosmo_glossary():
    return pd.read_csv('data_cosmochemistry/glossary_cosmochemistry.csv')
st.session_state.cosmo_glossary = import_cosmo_glossary()

cosmo_reviews_quiz_eng=st.session_state.cosmo_videos['Reviews & Quiz'][0].split('<task>')
cosmo_reviews_quiz_ger=st.session_state.cosmo_videos['Reviews & Quiz (german)'][0].split('<task>')

tab1, tab2, tab3 = st.tabs(['Videos', 'Assignments', 'Glossary'])
with tab1:
    if cosmo_language == 'english':
        video_sel = st.selectbox('', st.session_state.cosmo_videos['Title'])
        st.video(st.session_state.cosmo_videos[st.session_state.cosmo_videos['Title']==video_sel]['Youtube Number'].values[0])
        st.write(st.session_state.cosmo_videos[st.session_state.cosmo_videos['Title']==video_sel]['Blurb'].values[0])
    else:
        video_sel = st.selectbox('', st.session_state.cosmo_videos['Title (german)'])
        st.video(st.session_state.cosmo_videos[st.session_state.cosmo_videos['Title (german)']==video_sel]['Youtube Number (german)'].values[0])
        st.write(st.session_state.cosmo_videos[st.session_state.cosmo_videos['Title (german)']==video_sel]['Blurb (german)'].values[0])

with tab2:
    st.write('coming soon')

with tab3:
    gloss_sel = st.selectbox('', st.session_state.cosmo_glossary['Term'])
    # st.write(st.session_state.cosmo_glossary[st.session_state.cosmo_glossary['Term']==gloss_sel]['Synonym'].values[0])
    st.write(st.session_state.cosmo_glossary[st.session_state.cosmo_glossary['Term']==gloss_sel]['Explanation'].values[0])

st.divider()
if cosmo_language == 'english':
    st.subheader('Flashcards')
    st.write('Write your answer on a piece of paper, then expand the Textboxes and compare your answer with the answer in the box.')
else:
    st.subheader('Karteikarten')
    st.write('Schreibe Deine Antwort auf eine Stück Papier, öffne dann das Textfeld und vergeliche Deine Antwort mit der in der Box.')

if cosmo_language == 'english':
    cosmo_reviews_quiz = cosmo_reviews_quiz_eng
else:
    cosmo_reviews_quiz = cosmo_reviews_quiz_ger

for i in cosmo_reviews_quiz:
    if '(*R*)' in i:
        with st.expander(i[8:i.rfind('<q>')]):
            st.write(i[i.find('<e>')+3:-3])

st.divider()
if cosmo_language == 'english':
    st.subheader('Mulitple Choice Questions')
else:
    st.subheader('Mulitple Choice Fragen')
z=0
for i in cosmo_reviews_quiz:
    if '(*M*)' in i:
        z = z + 10
        st.write(i[8:i.rfind('<q>')])
        l = i[i.find('<a>')+3:i.rfind('<a>')].split('<i>')
        for j in range(len(l)-1):
            st.checkbox(l[j], key=z+j)
        with st.expander('The correct answers are:'):
            st.write(i[i.find('<l>')+3:i.rfind('<l>')])
            st.write(i[i.find('<e>')+3:i.rfind('<e>')])
st.sidebar.image('data_microanalysis/Goethe-Logo.jpg', width=150)
st.sidebar.write("Viele Wege führen zum Erfolg.")