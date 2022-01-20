# Database schema

The `accounts` table stores user's data.

```sql
create table accounts(
  id serial  primary key, -- omit in model
  username varchar(150) unique default uuid_generate_v4(),
  avatar varchar(255) default 'avatar/default.jpg',
  bio varchar(255),
  reputation int default 0,
  email varchar(64) unique not null,
  password varchar(150) not null, -- omit in model
  phone varchar(15) unique,
  is_active bool,
  is_staff bool,
  is_superuser bool, -- omit in model
  created_at timestamp,
  updated_at timestamp,
  last_login timestamp -- omit in model
);
```