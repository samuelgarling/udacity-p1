import fresh_tomatoes
import media

# A collection of 6 movies for the website.

toy_story = media.Movie("Toy Story", 
                        "A cowboy doll is profoundly threatened and jealous \
                        when a new spaceman figure supplants him as top toy in \
                        a boy's room.",
                        "http://ia.media-imdb.com/images/M/MV5BMTgwMjI4MzU5N15BMl5BanBnXkFtZTcwMTMyNTk3OA@@._V1_SY317_CR12,0,214,317_AL_.jpg", # noqa
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        [media.Character("Tom Hanks", "Woody"),
                         media.Character("Tim Allen", "Buzz Lightyear")])

avatar = media.Movie("Avatar",
                     "A paraplegic marine dispatched to the moon Pandora on \
                     a unique mission becomes torn between following his \
                     orders and protecting the world he feels is his home.",
                     "http://ia.media-imdb.com/images/M/MV5BMTYwOTEwNjAzMl5BMl5BanBnXkFtZTcwODc5MTUwMw@@._V1_SY317_CR0,0,214,317_AL_.jpg", # noqa
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     [media.Character("Sam Worthington", "Jake Sully"),
                      media.Character("Zoe Saldana", "Neytiri")])

gone_in_sixty_seconds = media.Movie("Gone in Sixty Seconds",
                        "A retired master car thief must come back to the \
                        industry and steal 50 cars with his crew in one \
                        night to save his brother's life.",
                        "http://ia.media-imdb.com/images/M/MV5BMTIwMzExNDEwN15BMl5BanBnXkFtZTYwODMxMzg2._V1_SY317_CR1,0,214,317_AL_.jpg", # noqa
                        "https://www.youtube.com/watch?v=o6AyAM1buQ8",
                        [media.Character("Nicolas Cage", "Memphis Raines"),
                         media.Character("Angelina Jolie", "Sara 'Sway' Waland"),
                         media.Character("Giovanni Ribisi", "Kip Raines")])

the_man_from_uncle = media.Movie("The Man from U.N.C.L.E.",
                                 "In the early 1960s, CIA agent Napoleon Solo \
                                 and KGB operative Illya Kuryakin participate \
                                 in a joint mission against a mysterious \
                                 criminal organization, which is working to \
                                 proliferate nuclear weapons.",
                                 "http://ia.media-imdb.com/images/M/MV5BMTc2NjQ4ODYyNF5BMl5BanBnXkFtZTgwODA3OTU5NTE@._V1_SX214_AL_.jpg", # noqa
                                 "https://www.youtube.com/watch?v=w_Ky4KPzKwY", # noqa
                                 [media.Character("Henry Cavill", "Solo")])

up = media.Movie("Up",
                 "Seventy-eight year old Carl Fredricksen travels to Paradise \
                 Falls in his home equipped with balloons, inadvertently \
                 taking a young stowaway.",
                 "http://ia.media-imdb.com/images/M/MV5BMTk3NDE2NzI4NF5BMl5BanBnXkFtZTgwNzE1MzEyMTE@._V1_SX214_AL_.jpg", # noqa
                 "https://www.youtube.com/watch?v=qas5lWp7_R0",
                 [media.Character("Edward Asner", "Carl Fredericksen"),
                  media.Character("Christopher Plummer", "Charles Muntz")])

zombieland = media.Movie("Zombieland",
                         "A shy student trying to reach his family in Ohio, \
                         a gun-toting tough guy trying to find the last \
                         Twinkie, and a pair of sisters trying to get to an \
                         amusement park join forces to travel across a \
                         zombie-filled America.",
                         "http://ia.media-imdb.com/images/M/MV5BMTU5MDg0NTQ1N15BMl5BanBnXkFtZTcwMjA4Mjg3Mg@@._V1_SY317_CR6,0,214,317_AL_.jpg", # noqa
                         "https://www.youtube.com/watch?v=c1-jFLlHLPw",
                         [media.Character("Jesse Eisenberg", "Columbus"),
                          media.Character("Woody Harrelson", "Tallahassee",),
                          media.Character("Emma Stone", "Wichita"),
                          media.Character("Abigail Breslin","Little Rock")])
# A list of the movies to pass to the website generator - fresh_tomatoes

the_movies = [toy_story, avatar, gone_in_sixty_seconds, the_man_from_uncle,
              up, zombieland]

# Create the website

fresh_tomatoes.open_movies_page(the_movies)
