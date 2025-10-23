import streamlit as st 
import requests 



###                        FUNCTIONS
def pokemon_assistant(question:str):
    
    response = requests.post(url="http://localhost:8000/pokemon_assistant/invoke",
                             json={"input":{"question":question}})
    result = response.json()
    return result['output']['text']

def pokemon_details(pokemon_name:str):
    
    response = requests.post(url="http://localhost:8000/pokemon_details/invoke",
                             json={"input":{"pokemon_name":pokemon_name}})
    result = response.json()
    return result['output']['text']

def pokemon_dex(pokemon_name:str):
    
    response = requests.post(url="http://localhost:8000/pokemon_dex/invoke",
                             json={"input":{"pokemon_name":pokemon_name}})
    result = response.json()
    return result['output']['text']





st.set_page_config(
    page_title="Insight_serve",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.title("Insight Serve(Chain-to-API System)👨‍💻")

with st.sidebar:
    st.title("Options")
    option = st.sidebar.radio(label="Select the option",options=["pokemon_assistant","pokemon_details","pokemon_dex"])
    
if option == "pokemon_assistant":
    text = st.text_input(label="Enter the question whatever you needed to know about the pokemon")
    with st.expander("💡 Click here to see suggested questions you can ask"):
        st.markdown("""
        - 🧠 *General questions*
        - "Who is Pikachu?"
        - "Tell me about Charmander."
        - "What type is Bulbasaur?"
        - 📍 *Region details*
        - "From which region is Lucario?"
        - "Which region does Piplup belong to?"
        - 📜 *Dex data & moves*
        - "What are Gengar's moves?"
        - "Show me the weaknesses of Dragonite."
        - "What are the abilities of Mimikyu?"
        - 🔍 *Comparisons*
        - "Compare Charizard and Blastoise."
        - "Which Pokémon is stronger: Garchomp or Salamence?"
        """)
    if st.button(label="Search🔍"):
        with st.spinner("please wait untill finish"):
            result = pokemon_assistant(question=text)
        with st.container():
            st.markdown(result, unsafe_allow_html=True)
        
        st.success(f"Generation Completed")
 
if option == "pokemon_details":
    text = st.text_input(label="Enter the question whatever you needed to know about the pokemon")
    with st.expander("📍 Pokémon details & region of appearance — Suggested questions"):
        st.markdown("""
        - 🐉 *Details about specific Pokémon*
        - "Tell me about Lucario."
        - "Describe Eevee in detail."
        - "What are the unique features of Greninja?"
        - 🌎 *Region-related questions*
        - "From which region is Lucario?"
        - "Which region does Rowlet belong to?"
        - "What is the home region of Garchomp?"
        - 🗺 *Region + details combined*
        - "Tell me the region and special abilities of Snorlax."
        - "Which region did Froakie first appear in and what are its evolutions?"
        """)
    if st.button(label="Search🔍"):
        with st.spinner("please wait untill finish"):
            result = pokemon_details(pokemon_name=text)
        with st.container():
            st.markdown(result, unsafe_allow_html=True)
        
        st.success(f"Generation Completed")  
        
if option == "pokemon_dex":
    text = st.text_input(label="Enter the question whatever you needed to know about the pokemon")
    with st.expander("📜 Pokémon moves, weaknesses & Dex data — Suggested questions"):
        st.markdown("""
        - ⚔ *Moves*
        - "What are Gengar's moves?"
        - "List the moves Charizard can learn."
        - "Show me the best moves for Lucario."
        - ❌ *Weaknesses*
        - "What are the weaknesses of Dragonite?"
        - "Which types is Mimikyu weak against?"
        - 📖 *Dex data & abilities*
        - "Show me Snorlax's Pokédex entry and abilities."
        - "Give me the Pokémon type, abilities, and dex data for Blastoise."
        - "Tell me Pikachu's Pokédex details, type, and abilities."
        """)
    if st.button(label="Search🔍"):
        with st.spinner("please wait untill finish"):
            result = pokemon_dex(pokemon_name=text)
        with st.container():
            st.markdown(result, unsafe_allow_html=True)
        
        st.success(f"Generation Completed")

            
    

