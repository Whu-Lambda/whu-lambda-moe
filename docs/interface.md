# Authenticate

Base address: /api/v1

| Method | Route            | Description                                 |
| ------ | ---------------- | ------------------------------------------- |
| GET    | /login           | Return `302 /login/Microsoft`.              |
| GET    | /login/Microsoft | OAuth for Microsoft. Redirect to auth page. |
| GET    | /login/GitHub    | OAuth for GitHub. Redirect to auth page.    |
| GET    | /logout          | Logout.                                     |
