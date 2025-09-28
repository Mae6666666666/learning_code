SELECT * FROM Artist
-- this basically says in SQL (sequel) to select all (*) from whatever is in the table named Artist

SELECT * FROM Artist
where Name = "Gorillaz"
-- this is basically the same as the one above, but at the bottom its saying only give back the name
-- that is equals to Gorillaz. it has to be the
-- exact same spelling and case too or else it wont find anything

SELECT * FROM Artist
where Name like "%ll%"
-- using like in this is basically saying any word in name that has whatever is in that string in it.
-- the percentage at the start says it can be any characters no matter the length in front of the ll and
-- the percentage at the end says that it can be a crap ton of characters after the string as long as
-- the ll is in front of it. that way you can vaguely search for things

SELECT
    Artist.Name AS ArtistName,
    -- you're saying that Artist.Name can be referred to as ArtistName
    Album.Title AS AlbumTitle
    -- You can refer Album.Title as AlbumTitle
 FROM Artist
-- coming from the Artist table
 JOIN Album
-- this joins the album and the artist table together
 ON Artist.ArtistId = Album.ArtistId
--    artistid is the foreign key cuz its not part of the album table
--    it joins together the artist.artistid with album.artistid
where ArtistName like "All%"
-- just like before, you can look specifically for whatever is in the string and the percentage
-- just says that any other character(s) can be after that

-- you select ar (which is later set to be artist). name which tells you that
-- youre looking for the file named name in the table and you refer this bit AS artist, which
-- just says u can refer it to artist instead of typing it all out
-- and youre doing this with title and release year too
SELECT ar.name AS artist, al.title AS album, al.release_year
-- then youre going in the albums table (which u can refer to as al)
FROM albums al
-- youre connecting albums and artists. this line is also where you do ar.name at the top to
-- verify it means artist
JOIN artists ar ON ar.id = al.artist_id
-- then it just tells the thing to order by the artist and then release year.
-- the semicolon means the end of the code
ORDER BY artist, release_year;

-- select the title and duration of seconds
SELECT title, duration_seconds
-- get these things from the table songs
FROM songs
-- wherever the duration is more than 250
WHERE duration_seconds > 250
-- order the duration seconds in descending order so from highest to lowest amount of time
ORDER BY duration_seconds DESC;

-- select all
SELECT *
-- select it all from artist popularity
FROM artist_popularity
-- limit the amount of artists to five (so it limits it to the top five)
LIMIT 5;

-- select songs (yes the s is songs, its stated in the from songs bit) title and the streams
SELECT s.title, s.streams
-- get these from songs
FROM songs s
-- wherever song streams is more than...
WHERE s.streams > (
-- the average of streams from songs. select them
  SELECT AVG(streams) FROM songs
)
-- then order them by descending order of streams in songs. so highest to lowest
ORDER BY s.streams DESC;

-- okay so this one makes u download shit because you're adding things ti the database
-- so its basically saying whatever i put in the brackets, put that into a table called playlists
INSERT INTO playlists (name, created_at)
-- then name is well, named as my daughters playlist, and the created at value is set as now.
-- i dunno what the datetime thing does.
VALUES ('My Daughters Playlist', datetime('now'));

-- all of this has also officially added it to the table

-- this grabs artist name and says u can refer it to as artist. then grabs the number of song id's,
-- referring that to songs, and then grabs the total number of song streams and refers them to as
-- total streams
SELECT ar.name AS artist, COUNT(s.id) AS songs, SUM(s.streams) AS total_streams
-- then from artists, which can be referred to as ar
FROM artists ar
-- join the albums which are in the album artist id with artist id
JOIN albums al ON al.artist_id = ar.id
-- then join the songs in song album id with album id
JOIN songs s ON s.album_id = al.id
-- group these things by the artist name
-- so this means all the joins are joined together, so three things are joined together now
GROUP BY ar.name
-- order the total streams in descending order, so highest to lowest.
ORDER BY total_streams DESC;

-- this is just like a print statement. it shows everything from the playlists table
SELECT * FROM playlists

-- this says go into albums which has title, id, artist_id, release_year, and total_tracks
INSERT INTO albums (title, id, artist_id, release_year, total_tracks)
-- and then you add your own thing to these places.
-- (I put in plastic beach and not only remembered what year it came out, but also the total
-- number of tracks without needing to look 😎)
VALUES ("Plastic Beach", 11, 8, 2010, 16)