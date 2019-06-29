1. BackEnd: Django
*     - smart: main Directory, define url, all configurations & installed applications are found in settings.py 
*     - case: application
*         - models.py: define the data model of our keywords with their explication fields
*         - schema.py: define the schema for graphql Query
*     - docxs: application
*         - models.py: define the data model of docx file ( history of uploaded docx file by registered member)
*         - schema.py: define the schema for graphql Query
*     - users: aplliocation
*         - schema.py: define the schema for graphql Query


1. FrontEnd: React
1. Query: GraphQL

1. How to connecte react front end with django backend ?     
2.  - django-cors-headers  + react axios


*     reference link:  https://www.jianshu.com/p/e9bc8b819075
*     link traslated : https://translate.google.com/translate?hl=fr&sl=auto&tl=fr&u=https%3A%2F%2Fwww.jianshu.com%2Fp%2Fe9bc8b819075

* #spacy model
*  docker-compose exec web python3 -m spacy download en_core_web_sm
