docker-compose exec web python smart/manage.py migrate

mutation {
  tokenAuth(username:"rocher2d2", password:"xxx") {
    token
  }
}

"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6InJvY2hlcjJkMiIsImV4cCI6MTU2MTUwMDc0MCwib3JpZ0lhdCI6MTU2MTUwMDQ0MH0.ezRfZBZ2rHl5RGMj74bPT1Dbbg-jseUtgMK981P8rM8"