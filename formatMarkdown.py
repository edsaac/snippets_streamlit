import streamlit as st
import re 
import pandas as pd 

stack = """And this difficulty attaches itself more closely to an age in which
    progress has gained a strong ascendency over prejudice, and in which
    persons and things are, day by day, finding their real level, in lieu
    of their conventional value. The same principles which have swept away
    traditional abuses, and which are making rapid havoc among the revenues
    of sinecurists, and stripping the thin, tawdry veil from attractive
    superstitions, are working as actively in literature as in society. The
    credulity of one writer, or the partiality of another, finds as
    powerful a touchstone and as wholesome a chastisement in the healthy
    scepticism of a temperate class of antagonists, as the dreams of
    conservatism, or the impostures of pluralist sinecures in the Church.
    History and tradition, whether of ancient or comparatively recent
    times, are subjected to very different handling from that which the
    indulgence or credulity of former ages could allow. Mere statements are
    jealously watched, and the motives of the writer form as important an
    ingredient in the analysis of his history, as the facts he records.
    Probability is a powerful and troublesome test; and it is by this
    troublesome standard that a large portion of historical evidence is
    sifted. Consistency is no less pertinacious and exacting in its
    demands. In brief, to write a history, we must know more than mere
    facts. Human nature, viewed under an induction of extended experience,
    is the best help to the criticism of human history. Historical
    characters can only be estimated by the standard which human
    experience, whether actual or traditionary, has furnished. To form
    correct views of individuals we must regard them as forming parts of a
    great whole—we must measure them by their relation to the mass of
    beings by whom they are surrounded, and, in contemplating the incidents
    in their lives or condition which tradition has handed down to us, we
    must rather consider the general bearing of the whole narrative, than
    the respective probability of its details.
"""
needle = st.text_input("What to look for?")

if needle:
    pretty_stack = re.sub(f"({needle})",r"**\1**",stack,flags=re.IGNORECASE)
else: 
    pretty_stack = stack

cols = st.columns(2)

with cols[0]:
    "## Bold text"
    st.markdown(pretty_stack, unsafe_allow_html=True)   

with cols[1]:
    "## Bold words in a table"
    stack_as_dataframe = pd.DataFrame({"Text":pretty_stack.split("\n")})
    st.markdown(stack_as_dataframe.to_markdown(None))