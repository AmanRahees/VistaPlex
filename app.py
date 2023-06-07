from flask import Flask, render_template, request, url_for
from main import rcmd, convert_to_list, get_suggestions
from bs4 import BeautifulSoup
import numpy as np
import urllib

app = Flask(__name__, static_folder='static')


@app.route('/')
@app.route('/home')
def home():
    suggestions = get_suggestions()
    return render_template('home.html', suggestions=suggestions)

@app.route('/similarity', methods=['POST'])
def similarity():
    movie = request.form['name']
    rmd = rcmd(movie)
    if type(rmd)==type('string'):
        return rmd
    else:
        m_str = "---".join(rmd)
        return m_str
    
@app.route("/recommend", methods=['POST'])
def recommend():
    title = request.form['title']
    cast_ids = request.form['cast_ids']
    cast_names = request.form['cast_names']
    cast_chars = request.form['cast_chars']
    cast_bdays = request.form['cast_bdays']
    cast_bios = request.form['cast_bios']
    cast_places = request.form['cast_places']
    cast_profiles = request.form['cast_profiles']
    imdb_id = request.form['imdb_id']
    poster = request.form['poster']
    genres = request.form['genres']
    overview = request.form['overview']
    vote_average = request.form['rating']
    vote_count = request.form['vote_count']
    release_date = request.form['release_date']
    runtime = request.form['runtime']
    status = request.form['status']
    rec_movies = request.form['rec_movies']
    rec_posters = request.form['rec_posters']

    suggestions = get_suggestions()

    rec_movies = convert_to_list(rec_movies)
    rec_posters = convert_to_list(rec_posters)
    cast_names = convert_to_list(cast_names)
    cast_chars = convert_to_list(cast_chars)
    cast_profiles = convert_to_list(cast_profiles)
    cast_bdays = convert_to_list(cast_bdays)
    cast_bios = convert_to_list(cast_bios)
    cast_places = convert_to_list(cast_places)

    cast_ids = cast_ids.split(',')
    cast_ids[0] = cast_ids[0].replace("[","]")
    cast_ids[-1] = cast_ids[-1].replace("]","")

    for i in range(len(cast_bios)):
        cast_bios[i] = cast_bios[i].replace(r'\n', '\n').replace(r'\n"','\"')

    movie_cards = {rec_posters[i]: rec_movies[i] for i in range(len(rec_posters))}

    casts = {cast_names[i]:[cast_ids[i], cast_chars[i], cast_profiles[i]] for i in range(len(cast_profiles))}

    cast_details = {cast_names[i]:[cast_ids[i], cast_profiles[i], cast_bdays[i], cast_places[i], cast_bios[i]] for i in range(len(cast_places))}
    

    return render_template('recommend.html',title=title,poster=poster,overview=overview,vote_average=vote_average,
        vote_count=vote_count,release_date=release_date,runtime=runtime,status=status,genres=genres,
        movie_cards=movie_cards,casts=casts,cast_details=cast_details)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')