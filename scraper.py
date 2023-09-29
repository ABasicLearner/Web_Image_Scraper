import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException


# Define a function to fetch image URLs
def fetch_image_urls(query: str, max_links_to_fetch: int, web_driver: webdriver, sleep_between_interactions: int = 1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)

    # Build the Google query URL
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # Load the page (Google search page with the specified query)
    web_driver.get(search_url.format(q=query))

    # Initialize variables to store image URLs and count
    image_urls = set()
    image_count = 0
    results_start = 0

    # Loop until the desired number of image links is fetched
    while image_count < max_links_to_fetch:
        scroll_to_end(web_driver)

        # Get all image thumbnail results using CSS selector
        thumbnail_results = web_driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")

        number_results = len(thumbnail_results)

        print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")

        for img in thumbnail_results:
            # Try to click every thumbnail, so we can get the real image behind it
            try:
                img.click()
                time.sleep(sleep_between_interactions)

            except ElementClickInterceptedException:
                print("Exception: Element click intercepted, skipping...")
                continue

            except Exception as e:
                print("Exception:", str(e))
                continue

            # Extract image URLs from the opened images
            actual_images = web_driver.find_elements(By.CSS_SELECTOR, "img.rg_i.Q4LuWd")

            for actual_image in actual_images:
                src = actual_image.get_attribute('src')
                if src and src.startswith('http'):
                    image_urls.add(src)

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links, done!")
                break
            else:
                print("Found:", len(image_urls), "image links, looking for more ...")
                time.sleep(30)

        # Move the result start point further down
        results_start = len(thumbnail_results)

    return list(image_urls)
