## Brewery Explorer

### Description:
This project is still under development and not all the mechanisms mentioned below will work appropriately.

This is a Flask web application designed to explore breweries using the Open Brewery DB API. 
It allows users to search for breweries, view details about specific breweries (like localization), and contact brewery via phone number.

### Features:
1. **Home Page:** 
   - Displays the main page of the application.

2. **Search Brewery:**
   - Users can input text to search for breweries.
   - The application queries the Open Brewery DB API based on the user input.
   - If the search response contains brewery objects, the user is redirected to a sub-site with information about the brewery.
   
3. **Localization Details:**
   - Shows localization of given brewery.
   
4. **Phone Details:**
   - User can access phone number of searched brewery. 
   
### Usage:
1. Clone the repository:
   ```bash
   https://github.com/Pawlik-Lukasz/BreweryWebsite
   ```

2. Install dependencies:
    ```bash
   pip install -r requirements.txt
    ```

### File Structure:
- main.py: Contains the Flask application code.
- templates/: Directory containing HTML templates.
  - index.html: Home page template.
  - search.html: Brewery search template.
  - navbar.html: Navigation bar template.
- static/: Directory for static files (e.g., CSS, images).
- requirements.txt: List of Python dependencies.
### Contributions:
This project is still under development. Some of the templates mentioned above still doesn't exist.
If you have any suggestions or improvements, feel free to open an issue or submit a pull request.
