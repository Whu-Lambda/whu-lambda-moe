This document is about activities.

# Database schema


```sql
create table activities(
    id serial primary key, -- omit in model
    name varchar(64) not null, -- name of activity
    content text not null, -- markdown down text
    summary text not null, -- suammary of activity, markdown text
    author varchar(64) not null, -- author's name of activity
    cover varchar(255) not null, -- activity's cover url.
    tags varchar(64) not null, -- tags of activity, separated by `,`
    status varchar(64) default 'open', -- status of activity
    time_slot varchar(64) not null, -- time of activity, like '2022-01-20 18:30-22:30'
    place varchar(64) not null, -- place of activity
    created_at timestamp,
    updated_at timestamp,
);
```
