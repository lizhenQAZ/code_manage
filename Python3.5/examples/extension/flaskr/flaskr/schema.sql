DROP TABLE IF EXISTS entries;
CREATE TABLE entries(
  id INTEGER PRIMARY KEY autoincrement,
  title text not null,
  'text' text not null
)