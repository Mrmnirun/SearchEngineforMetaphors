# SearchEngineforMetaphors

The proposed search engine will focus on providing a comprehensive collection of metaphors from popular Tamil movie songs released between 2000 and 2020 by the composers A.R.Rahman, Ilayaraja, Vidyasagar, Yuvan Shankar Raja and Aniruth. This search engine will include the following fields related to the songs for the users to easily identify and explore the metaphors within the lyrics.
1.	Name - Name of the song
2.	Lyrics - Lyrics of the song in tamil
3.	Composer - Music director of the song (A.R.Rahman/ Ilayaraja/ Vidyasagar/Yuvan Shankar Raja/ Aniruth)
4.	Lyricist - Lyricist of the song
5.	Album - Movie name which has the song
6.	Artist - Singer of the song
7.	Year - Album released year
8.	Metaphor - Metaphors of the song (can be more than one metaphor)
a.	Source domain - It is the conceptual domain from which we draw metaphorical expressions.
b.	Target domain - It is the quality or experience described by or identified with the source domain
c.	Type of metaphor - Metaphors can be characterized as being based on characteristics, actions, or benefits.
d.	Interpretation - Meaning of the metaphor

Scope of the project is to assist users who are interested in discovering metaphors
from Tamil songs.
1.	Search Engine for metaphors of Tamil songs can be used to get the idea about the metaphors for the requested subject
2.	User can use it to search based on the source domain or target domain of the metaphor
3.	User can use it to search based on the type of metaphor for the subject
4.	User can use it to get the metaphors based on the rhyming.

Implementation: I am planning to use a minimum of 100 songs for the initial implementation where each song should have at least one metaphor. I am planning to collect this data from the Musixmatch. If there are any lyrics of the song in English, then I will preprocess and translate the fields which are in English to Tamil. I am planning to use Apache Solr for indexing and querying and planning to implement wildcard matching, keyword matching and range searching. I am going to use this repo as a project repository.
