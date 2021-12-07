# JSONPath

Online validation tool : [Validation JSONPath](http://jsonpath.com/)

Here you will find :

1. What is the rating value of the movie? 
   1. Code : ```$..aggregateRating.ratingValue```
   2. Response : 8.4
   3. Validation Screenshot : ```1_Val1.png```
   
2. What is the IMDB identifier for Rebecca Ferguson?
   1. Code : ```$..actor[?(@.name == "Rebecca Ferguson")].url```
   2. Response : "/name/nm0272581/"
   3. Validation Screenshot : ```2_Val2.png```

3. Who rated the film with only 1 star
   1. Code : ```$.reviews[?(@.reviewRating.ratingValue == 1)].author.name```
   2. Response : "wmnac-84309"
   3. Validation Screenshot : ```3_Val3.png```


