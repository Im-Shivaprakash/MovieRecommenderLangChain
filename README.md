# Movie Recommendation System with LangChain and OpenAI

A dynamic movie recommendation system built using LangChain and OpenAI's GPT models. The app allows users to input a genre, director, or actor to receive movie recommendations. The recommendations are generated based on IMDb data, with the flexibility to search by genre, director, or star name.

---

## Features

- **Flexible Search**: Users can input any combination of genre, director, or star name to receive personalized movie recommendations.
- **LangChain Integration**: Utilizes LangChain to create a sequence of chains for processing user inputs and generating movie recommendations.
- **IMDb Data**: Recommendations are based on top-rated IMDb movies in the specified genre, director, or star.
- **Streamlit UI**: A simple and interactive user interface built with Streamlit for easy use and visualization.
- **Movie Information Display**: Displays the top recommended movies along with their IMDb ratings, and neatly formatted results.

---

## Requirements



Ensure that you have the following installed:

- **Python 3.x** (Recommended Python 3.7 or higher)
- **Streamlit**: For the interactive user interface
- **LangChain**: For chaining language model prompts and processing
- **OpenAI**: For using GPT models

You can install the required libraries using `pip`:

```bash
pip install -r requirements.txt
```
The requirements.txt file includes all necessary dependencies.

## Setup

Clone this repository:

```bash
git clone https://github.com/Im-Shivaprakash/MovieRecommenderLangChain.git

cd movie-recommendation-langchain 
```

Replace the constants.py file with your OpenAI API key :

```bash
openai_key = 'sk-xxx'  # Replace with your OpenAI API key
```

Add your OpenAI API key to the constants.py file as shown above.

## Run the application:

```bash
streamlit run app.py
```

The app will open in your browser. Follow the instructions to input the genre, director, or actor to get recommendations.

## Project Structure
1. app.py: Main Streamlit app that runs the recommendation system.
2. constants.py: Contains your OpenAI API key.
3. movie_recommendation.mp4: A demo video explaining how to run and use the application.
4. requirements.txt: Lists the necessary libraries to run the app.

## Example Usage

Input 1: Genre: "Science Fiction"
Output: Top movies in the Science Fiction genre.

Input 2: Director: "Christopher Nolan"
Output: Movies directed by Christopher Nolan.

Input 3: Actor: "Leonardo DiCaprio"
Output: Movies featuring Leonardo DiCaprio.

Input 4: Genre: "Action", Director: "James Cameron"
Output: Top Action movies directed by James Cameron.

## Acknowledgements
1. LangChain: For providing the chain-based framework to link multiple language models.
2. OpenAI GPT: For the powerful language models that power the recommendation system.
3. IMDb API: For serving as the source of movie data.
4. Streamlit: For the easy-to-use UI framework.

## Demo
Watch a demo of the application in action:

[Movie Recommendation Demo Video](movie_recommendation.mp4)


