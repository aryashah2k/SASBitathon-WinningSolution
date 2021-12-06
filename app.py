import streamlit as st
import matplotlib.pyplot as plt
import spacy
from spacy.lang.el.stop_words import STOP_WORDS
from wordcloud import WordCloud
import base64

main_bg="6803.png"
main_bg_ext="png"
st.markdown(
    f"""
    <style>
    .reportview-container{{
        background:url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg,"rb").read()).decode()})
    }}
    """,
    unsafe_allow_html=True
)

@st.cache(allow_output_mutation=True)
def get_nlp_model(path):
    return spacy.load(path)

def generate_output(text):
     cats = nlp(text).cats
     if cats['DISPUTED'] > cats['NOT DISPUTED']:
         st.markdown("<h1><span style='color:red'>THE CUSTOMER IS LIKELY TO DISPUTE😡</span></h1>",
                     unsafe_allow_html=True)
     else:
         st.markdown("<h1><span style='color:green'>THE CUSTOMER IS UNLIKELY TO DISPUTE😌</span></h1>",
                     unsafe_allow_html=True)

     q_text = '> '.join(text.splitlines(True))
     q_text = '> ' + q_text
     st.markdown(q_text)

     wc = WordCloud(width = 1000, height = 600,
                    random_state = 1, background_color = 'white',
                    stopwords = STOP_WORDS).generate(text)

     fig, ax = plt.subplots()
     ax.imshow(wc)
     ax.axis('off')
     st.pyplot(fig)
     print(cats)
     st.markdown("<h3><span style='color:yellow'>Chances of Customer Disputing/Not Disputing</span></h3>",
                     unsafe_allow_html=True)
     st.markdown(cats)

nlp = get_nlp_model('finalmodelmini')

desc = "This web app predicts the probability of a customer disputing or not based on his/her complaint.\
        You can enter the customer complaint in English in the text box below and get the final verdict along with the probability for both the cases."

st.title("Predict Whether A Customer Will Open A Dispute Or Not!")
st.markdown(desc)
st.subheader("Enter the customer complaint/narrative in English")
text = st.text_area("Text", height=300)
if st.button("Run"):
    generate_output(text)


st.markdown("<br><br><hr><center>Made with ❤️ for SAS | GIM, Bitathon by <a href='https://github.com/aryashah2k'><strong>Arya Shah</strong></a></center><hr>", unsafe_allow_html=True)
