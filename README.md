# Image Search and Download Web Application

## Objective
The Image Search and Download web application is designed to provide users with a simple and intuitive platform for searching and downloading images. Built with a user-friendly interface, this application streamlines the process of finding and saving images based on specific search queries.

## Technology Stack
- **Web Application Framework:** Flask
- **Frontend:** HTML, CSS
- **Backend Development:** Python

## Project Workflow

1. **User Interface:** Users access the web application through a user-friendly interface.

2. **User Input:** Users input their search query and specify the number of images they want to retrieve.

3. **Backend Processing:** The backend of the application processes the user's input and initiates a request to a search engine, utilizing the Chrome web driver for automation.

4. **Web Scraping:** Advanced web scraping techniques are employed to extract image search results that match the user's query.

5. **Image Display:** The retrieved images are dynamically displayed on the web page, allowing users to view their search results effortlessly.

6. **Local Saving:** As soon as the images are displayed on the user's screen, they are automatically saved to a local directory on the user's device. This feature ensures that users can conveniently store the images they find without the need for manual downloads.

## Getting Started
To use the Image Search and Download web application, follow these steps:

1. Clone this repository to your local machine.

2. Install the required dependencies using pip.

3. Start the Flask application.
   
4. Access the web application in your browser by navigating to `http://localhost:5000`.

5. Input your search query and the desired number of images to retrieve, then click "Search."

6. Explore the retrieved images, and they will be automatically saved to your local directory.

## Dependencies
- Flask
- Selenium (for web automation)
- Chrome Web Driver
- Beautiful Soup (for web scraping)
- Requests


