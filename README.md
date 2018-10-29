### Remine Front End Interview Test

#### Environment

You may use whatever coding environment you would like, though, we will be testing your code with the following:

- Node version 8+ 
- Chrome browser version 60+

#### To Do

1. Fork this repo to your Github account
2. Clone your forked repo to your local environment
3. Create an API endpoint inside of `api-server.py` with the url `/locations` that returns the locations found in the file `db.json`.
4. Create an API endpoint inside of `api-server.py` with the url `/locations/:id` that returns the location specified in the url from the file `db.json`.
5. Create an API endpoint inside of `api-server.py` with the url `/buildingtypes` that returns the building types located in the file `db.json`.
6. Obtain the list of locations and building type categories from the endpoints you just created using the included `API.js`.
7. Populate the `RemineTable` component inside of `CHANGEME.js` with the locations obtained from step 1.
8. Build out the `CHANGEME.js` view to allow a user to filter the `RemineTable` contents based on whether the location has:
    * a number of beds in a user specified **range**
    * the same building type as the one specified by the user (the user can select from a list of building types that come from the API)

    If a user has not specified a bound in a range or a type for the building type, default to show all. If no filters are active or being applied, all locations should be shown in the `RemineTable`. 
9. When finished, commit/push your changes and send us a direct link to your forked repo

#### Starting the application

1. Install the JavaScript dependencies by running `npm install`
2. Install the Python dependencies by running `pip install flask`
3. In a terminal window, start your API server by running `npm run start-server`
4. In another terminal window, start your client server by running `npm run start-client`

#### Grading

**THIS SHOULD BE PRODUCTION LEVEL CODE** 

We will critique on UX and code quality, but not design. Testing your code is not required.

Good luck.

![](https://media.giphy.com/media/26DOs997h6fgsCthu/giphy.gif)
