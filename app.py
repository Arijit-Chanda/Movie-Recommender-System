from flask import Flask,render_template,request
import pickle

movies_list = pickle.load(open('movies.pkl','rb'))
movies = movies_list['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',movies=movies)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    selected_movie = request.form['movie']
    movie_i = movies_list[movies_list['title'] == selected_movie].index[0]
    m_list = sorted(list(enumerate(similarity[:, movie_i])), reverse=True, key=lambda x: x[1])[1:8]
    print("YOU SHOULD GO FOR THIS MOVIES NEXT -----> 🎬")
    recommended_movies = []
    for i in m_list:
        recommended_movies.append(movies_list.iloc[i[0]]['title'])
    return render_template('index.html', recommended_movies=recommended_movies)

@app.route('/submit')
def home():
    return redirect(url_for('index'))  # Redirect to the index route




if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)