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
