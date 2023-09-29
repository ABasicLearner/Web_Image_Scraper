from selenium import webdriver
from flask import Flask, render_template, request
from scraper import fetch_image_urls

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', images=None)


@app.route('/search', methods=['POST'])
def search():

    query = request.form.get('query')
    num_images = int(request.form.get('num_images'))  # Get the number of images from user input

    # Create a WebDriver instance
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    options.add_argument('--disable-gpu')
    web_driver = webdriver.Chrome(options=options)

    # Fetch image URLs
    image_urls = fetch_image_urls(query=query, max_links_to_fetch=num_images, web_driver=web_driver, sleep_between_interactions=2)

    # Close the WebDriver
    web_driver.quit()

    # List image URLs
    images = [img for img in image_urls]

    return render_template('results.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)
