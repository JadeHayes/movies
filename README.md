INTRODUCTION
------------

This is an app that searches the imbd database for movie titles.  The app is created 
with react/typescipt on the frontend and python/flask on the backend. Ideally, a person
using this app would be able to search for a movie using the imbd API, click on the title and 
have a short description about the movie.  In addition to searching the imbd database, there is also
the ability to like/dislike the app.  There is no user login so we tally likes and dislikes
as a total count in our local database.


This is app was created by the most junior developer on the team and they've created a PR review for you.
We ask that you spend no more than 2 hours on this process, feel free to search for answers you 
are unsure of.  There is no need to fix the app and get it working but do comment on the areas
that are broken and give direction on how to fix them.


SETUP
------------
Once this repo is cloned locally follow the steps below.

`/backend`
- cd into the /backend directory.
- run `pipenv shell` to activate the virtual enviornment. 
- Install the requirements by running `pipenv install`.

`/frontend`
- cd into the frontend directory and run npm install.

RUNNING LOCALLY
------------
The backend runs on a flask server at port 5000 and the frontend runs on port 3000. 
To run this app locally, cd into the backend directory and run the command `python backend.py`,
In another terminal, cd into the `/frontend` directory and run `npm run start`.


SUCCESS CRITERIA
------------
The success criteria for this PR is listed below.
- Search for a movie using the imbd API.
- Click on the title and read a short description about the movie.
- Save an arbitrary like/dislike the db. 
- View the total number of likes/dislikes per movie.

