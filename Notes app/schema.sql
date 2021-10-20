drop table if exists posts;

create table posts (
    id integer primary key autoincrement,
    created timestamp DATE not null default (datetime('now','localtime')),
    title text not null,
    content text not null
)