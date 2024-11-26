import streamlit as st
import os
from constants import openai_key
from langchain_community.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

# Ensure the API key is set
os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit Framework
st.title("Movie Recommendation")
genre = st.text_input("Tell me the genre you like (optional)")
director = st.text_input("Tell me the Director's Name (optional)")
star = st.text_input("Tell me the Actor's Name (optional)")

# Initialize OpenAI LLM
llm = ChatOpenAI(temperature=0.8)

# Prompt Templates
first_input_prompt = PromptTemplate(
    input_variables=['genre'],
    template="Provide a list of top IMDb movies in the genre '{genre}'."
)

first_chain = LLMChain(
    llm=llm,
    prompt=first_input_prompt,
    verbose=True,
    output_key="movie_info"
)

second_input_prompt = PromptTemplate(
    input_variables=["genre", "director"],
    template="Provide a list of top IMDb movies in the genre '{genre}' directed by '{director}'."
)

second_chain = LLMChain(
    llm=llm,
    prompt=second_input_prompt,
    verbose=True,
    output_key="movie_info_director"
)

third_input_prompt = PromptTemplate(
    input_variables=["genre", "star"],
    template="Provide a list of top IMDb movies in the genre '{genre}' featuring the star '{star}'."
)

third_chain = LLMChain(
    llm=llm,
    prompt=third_input_prompt,
    verbose=True,
    output_key="movie_info_star"
)

fourth_input_prompt = PromptTemplate(
    input_variables=["genre", "director", "star"],
    template="Provide a list of top IMDb movies in the genre '{genre}' directed by '{director}' and featuring the star '{star}'."
)

fourth_chain = LLMChain(
    llm=llm,
    prompt=fourth_input_prompt,
    verbose=True,
    output_key="movie_info_full"
)

# Sequential Chain Setup
parent_chain = SequentialChain(
    chains=[first_chain, second_chain, third_chain, fourth_chain],
    input_variables=["genre", "director", "star"],
    output_variables=["movie_info", "movie_info_director", "movie_info_star", "movie_info_full"],
    verbose=True
)

# Check input conditions and choose the appropriate chain
if genre or director or star:  # Ensuring we only process if any input exists
    if director and not star:
        result = second_chain({"genre": genre, "director": director})
        st.markdown(f"### Movies based on Director: {director}")
        st.write(result["movie_info_director"])
    elif star and not director:
        result = third_chain({"genre": genre, "star": star})
        st.markdown(f"### Movies based on Actor: {star}")
        st.write(result["movie_info_star"])
    elif genre:
        if director and star:
            result = fourth_chain({"genre": genre, "director": director, "star": star})
            st.markdown(f"### Movies based on Genre, Director, and Actor:")
            st.write(result["movie_info_full"])
        elif director:
            result = second_chain({"genre": genre, "director": director})
            st.markdown(f"### Movies based on Genre and Director: {genre}, {director}")
            st.write(result["movie_info_director"])
        elif star:
            result = third_chain({"genre": genre, "star": star})
            st.markdown(f"### Movies based on Genre and Actor: {genre}, {star}")
            st.write(result["movie_info_star"])
        else:
            result = first_chain({"genre": genre})
            st.markdown(f"### Movies based on Genre: {genre}")
            st.write(result["movie_info"])
else:
    st.warning("Please enter at least one input (Genre, Director, or Actor) to get movie recommendations.")
