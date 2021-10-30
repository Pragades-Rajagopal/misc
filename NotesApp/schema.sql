drop table if exists posts;

create table posts (
    id integer primary key autoincrement,
    -- created timestamp DATE not null default (datetime('now','localtime')),
    created text not null,
    title text not null,
    content text not null,
    priority text not null
)