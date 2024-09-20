import sqlite3

conn=sqlite3.connect("concerts_database_database.db")
cursor=conn.cursor()


cursor.execute('''
    CREATE TABLE IF NOT EXISTS concerts (
        id INTEGER PRIMARY KEY,
        band_id INTEGER NOT NULL,
        venue_id INTEGER NOT NULL,
        date TEXT NOT NULL,
        FOREIGN KEY(band_id) REFERENCES bands(id),
        FOREIGN KEY(venue_id) REFERENCES venues(id)
    );
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS bands (
        id INTEGER PRIMARY KEY ,
        name TEXT ,
        hometown TEXT 
    );
    ''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS venues (
        id INTEGER PRIMARY KEY ,
        title TEXT,
        city TEXT 
    );
    ''')


conn.commit()
conn.close()



def inserting_data():
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    
    
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Sauti Sol', 'Kenya')")
    cursor.execute("INSERT INTO bands (name, hometown) VALUES ('Hart the Band', 'Uganda')")
    
    
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Carnivore', 'Nairobi')")
    cursor.execute("INSERT INTO venues (title, city) VALUES ('Syomikau', 'Machakos')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (1, 1, '2024-10-05')")
    cursor.execute("INSERT INTO concerts (band_id, venue_id, date) VALUES (2, 2, '2024-09-13')")
    
    conn.commit()
    conn.close()

inserting_data()


def get_all_concerts(band_id):
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * 
    FROM concerts
    WHERE band_id = ?;
        ''', (band_id, )) 
    rows = cursor.fetchall()
     
    conn.close()
     
    return rows
  

def get_distinct_bands_and_join(venue_id):
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT bands.name FROM concerts JOIN bands ON concerts.band_id=bands.id
    WHERE concerts.venue_id = ?;
        ''', (venue_id,))
    band = cursor.fetchall()

    conn.close()

    return band
 
def get_distinct_venues(band_id):
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT DISTINCT venues.title FROM concerts JOIN venues ON concerts.venue_id=venues.id
    WHERE concerts.band_id = ?;
        ''', (band_id,))
    venue = cursor.fetchall()

    conn.close()

    return venue


def get_venue_concerts(venue_id):
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM concerts
    WHERE venue_id = ?;
        ''', (venue_id,))
    concert = cursor.fetchall()

    conn.close()

    return concert


def get_concert_band(concert_id):
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT bands.name,bands.hometown FROM concerts JOIN bands ON concerts.band_id=bands.id
    WHERE concerts.id = ?;
        ''', (concert_id,))
    band = cursor.fetchall()

    conn.close()

    return band
  
def get_concert_venue(concert_id):
    conn = sqlite3.connect('concerts_database_database.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT venues.title,venues.city FROM concerts JOIN venues ON concerts.venue_id=venues.id
    WHERE concerts.id = ?;
        ''', (concert_id,))
    venue = cursor.fetchall()

    conn.close()

    return venue  
 
def Concert_hometown_show(concert_id):
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.hometown, venues.city 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE concerts.id = ?;
    ''', (concert_id,))
    
    hometown, city = cursor.fetchone()
    conn.close()
    return hometown == city

def concert_introduction(concert_id):
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, bands.hometown, venues.city 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    JOIN venues ON concerts.venue_id = venues.id 
    WHERE concerts.id = ?;
    ''', (concert_id,))
    
    band_name, band_hometown, venue_city = cursor.fetchone()
    conn.close()
    print(f"Hello {venue_city}!!!, We are {band_name} and we're from {band_hometown}")


def Band_play_in_venue(band_id, venue_id, date):
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO concerts (band_id, venue_id, date) VALUES (?, ?, ?);
    ''', (band_id, venue_id, date))
    
    conn.commit()
    conn.close()


def Band_all_introductions(band_id):
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()

    cursor.execute('''
    SELECT DISTINCT bands.name, bands.hometown, venues.city
    FROM concerts
    JOIN bands ON concerts.band_id = bands.id
    JOIN venues ON concerts.venue_id = venues.id
    WHERE bands.id = ?
    LIMIT 1;  -- Ensure we only fetch one venue for the introduction
    ''', (band_id,))
    
    band_name, band_hometown, venue_city = cursor.fetchone()
    print(f"Hello {venue_city}!!!!! We are {band_name} and we're from {band_hometown}")
    
    conn.close()



def Band_most_performances():
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, COUNT(concerts.id) AS num_concerts 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    GROUP BY bands.id 
    ORDER BY num_concerts DESC 
    LIMIT 1;
    ''')
    
    band = cursor.fetchone()
    conn.close()
    return band


def Venue_concert_on_date(venue_id, date):
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT * FROM concerts 
    WHERE venue_id = ? AND date = ? 
    LIMIT 1;
    ''', (venue_id, date))
    
    concert = cursor.fetchone()
    conn.close()
    return concert

def Venue_most_frequent_band(venue_id):
    conn = sqlite3.connect('concerts_database.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT bands.name, COUNT(concerts.id) AS num_concerts 
    FROM concerts 
    JOIN bands ON concerts.band_id = bands.id 
    WHERE concerts.venue_id = ? 
    GROUP BY bands.id 
    ORDER BY num_concerts DESC 
    LIMIT 1;
    ''', (venue_id,))
    
    band = cursor.fetchone()
    conn.close()
    return band
# sample usage
concert_introduction(1)
Band_all_introductions(2)   
print(get_concert_venue(1) ) 
print(Venue_concert_on_date(1,"2024-10-05"))
print(Venue_most_frequent_band(1))
print(Band_most_performances())
print(get_all_concerts(1))
print(get_concert_band(1))
print(Concert_hometown_show(2))
 