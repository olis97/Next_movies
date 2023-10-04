import spacy

description_compare = description_compare = 'Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.'
suggested_movie = None

# Setup spacy models
nlp = spacy.load('en_core_web_md')

# Token Planet Hulk Movie description
token_compare = nlp(description_compare)

with open('movies.txt', 'r') as read_movie_description:
    descriptions = read_movie_description.readlines()
    comparing_description = None
    highest_similarity = 0


    # Loop over movies description
    for description in descriptions:
        movie_descriptions = description.split(' :') 
        comparing_description = movie_descriptions[1]
        token_comparing = nlp(comparing_description)
        
        # Compare token with Planet Hulk Movie description
        similarities_result = token_comparing.similarity(token_compare)

    
        if similarities_result > highest_similarity:
            highest_similarity = similarities_result
            suggested_movie =description
# Print suggested movie
print('suggested to watch:', suggested_movie)
