This document is about articles.

# Database schema


```sql
create table articles(
    id serial primary key, -- omit in model
    name varchar(64) not null, -- name of article
    about text not null, -- an abstract of the article
    content text not null,
    author varchar(64) not null, -- author's name of article
    cover varchar(255) not null, -- article's cover url.
    tags varchar(64) not null, -- tags of article, separated by `,`
    created_at timestamp,
    updated_at timestamp,
);
```
