.read data.sql


CREATE TABLE bluedog AS
  SELECT color, pet FROM students WHERE COLOR = "blue" AND pet = "dog" ;

CREATE TABLE bluedog_songs AS
  SELECT color, pet, song FROM students WHERE COLOR = "blue" AND pet = "dog" ;


CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color,b.color FROM students AS a, students AS b WHERE a.pet == b.pet AND a.song == b.song AND a.time<b.time;


/*The following SQL is from Cs61a */
CREATE TABLE sevens AS
  SELECT s.seven FROM students AS s, numbers AS c WHERE s.number = 7 AND c.'7' = 'True' AND s.time = c.time;


/*The following SQL is from Cs61a */
CREATE TABLE smallest_int_having AS
  SELECT time, smallest FROM students GROUP BY smallest HAVING COUNT(*) = 1;


