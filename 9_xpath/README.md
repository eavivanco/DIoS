# XPath

Online validation tool : [Validation XPath](http://xpather.com/)

Here you will find :

1. What is the artist id?
   1. Code : ```.//artist/@*[self::id]```
   2. Response : 76c9a186-75bd-436a-85c0-823e3efddb7f
   3. Validation Screenshot : ```1_Val1.png```
   
2. What is the duration of the track Summertime ? (i have no idea why is not working)
   1. Code : ```.//recording[title = "Summertime"]/length```
   2. Response : 241000

3. What is the duration of the longest track? (i have no idea why is not working)
   1. Code : ```.//recording[length = max(/recording/length)]/length```
   2. Response : 480000

4. What is the total duration of the album?
   1. Code : ```sum(.//recording/length)```
   2. Response : 2503305
   3. Validation Screenshot : ```4_Val4.png```

5. What are the names of the tracks that were first released before 01/01/1970 ?
   1. Code : ```.//recording[number(translate(first-release-date,'-','')) < 19700101]/title```
   2. Response : Piece of My Heart, Summertime, Try (Just a Little Bit Harder), Bye Bye Baby
   3. Validation Screenshot : ```5_Val5.png```
