from flask import Flask, render_template
import openpyxl
from collections import Counter

app = Flask(__name__)

# Load song data from the Excel file
def load_excel_data(filename):
    workbook = openpyxl.load_workbook(filename)
    sheet = workbook.active
    headers = [cell.value for cell in sheet[1]]  # Extract column headers
    return [dict(zip(headers, row)) for row in sheet.iter_rows(min_row=2, values_only=True)]  # Convert rows to dictionaries

# Count genre appearances
def count_genres(songs):
    genre_counter = Counter()
    for song in songs:
        genres = song['GENRE'].split(", ")  # Handle multiple genres separated by commas
        for genre in genres:
            genre_counter[genre.strip()] += 1
    return genre_counter

# Define the Excel file path
EXCEL_FILE = "Top_50_Songs.xlsx"

@app.route("/")
def show_songs():
    songs = load_excel_data(EXCEL_FILE)  # Load song data
    return render_template("index.html", songs=songs)

@app.route("/artists_charts")
def artists_charts():
    songs = load_excel_data(EXCEL_FILE)  # Load song data
    artist_counts = Counter(song['ARTIST'] for song in songs)  # Count occurrences of artists
    labels = list(artist_counts.keys())  # Artist names
    values = list(artist_counts.values())  # Counts
    return render_template("artists_charts.html", labels=labels, values=values)

@app.route("/genre")
def genre():
    songs = load_excel_data(EXCEL_FILE)  # Load song data
    genre_counts = count_genres(songs)  # Get genre counts
    labels = list(genre_counts.keys())  # Genre names
    values = list(genre_counts.values())  # Counts
    return render_template("genre.html", labels=labels, values=values)

if __name__ == "__main__":
    app.run(debug=True)
