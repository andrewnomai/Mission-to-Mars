# Import Splinter and BeautifulSoup

from splinter import Browser

from bs4 import BeautifulSoup as soup

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

import datetime as dt




# Set up Splinter

def scrape_all():

    # Initiate headless driver for deployment

    executable_path = {'executable_path': ChromeDriverManager().install()}

    browser = Browser('chrome', **executable_path, headless = False)


    news_title, news_paragraph = mars_news(browser)



    # Run all scraping functions and store results in a dictionary

    data = {

        "news_title": news_title,

        "news_paragraph": news_paragraph,

        "featured_image": featured_image(browser),

        "facts": mars_facts(),

        "last_modified": dt.datetime.now(),

        "hemispheres": hemisphere_scrape(browser)
    }


    # Stop webdriver and return data

    browser.quit()

    return data






def mars_news(browser):

    # Scrape Mars News

    # Visit the mars nasa news site

    url = 'https://redplanetscience.com'

    browser.visit(url)



    # Optional delay for loading the page

    browser.is_element_present_by_css('dv.list_text', wait_time = 1)


    # Convert the browser html to a soup object and then quit the browser

    html = browser.html

    news_soup = soup(html, 'html.parser')

    
    
    # Add try/except for error handling

    try:

        slide_elem = news_soup.select_one('div.list_text')

        # Use the parent element to find the first 'a' tag and save it as 'news_title'

        news_title = slide_elem.find('div', class_ = 'content_title').get_text()

        news_title

        # Use the parent element to find the paragraph text

        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

        news_p

    except AttributeErorr:

        return None, None



    return news_title, news_p


# #### JPL Space Images Featured Images


def featured_image(browser):

    # Visit URL

    url = 'https://spaceimages-mars.com'

    browser.visit(url)

    # Find and click the full image button

    full_image_elem = browser.find_by_tag('button')[1]

    full_image_elem.click()



    # Parse the resulting html with soup

    html = browser.html

    img_soup = soup(html, 'html.parser')



    # Add try/except for error handling
   
    try:
        
        # Find the relative image url
        
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        
        return None


    # Use the base URL to create an absolute URL

    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    
    
    return img_url


# ## Mars Facts

def mars_facts():

    # Add try/except for error handling
    
    try:
        
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        
        return None


 # Assign columns and set index of dataframe

    df.columns=['description', 'Mars', 'Earth']

    df.set_index('description', inplace=True)

    
    # Convert Dataframe into HTML format, add bootstrap

    return df.to_html(classes = "table table-striped")


def hemisphere_scrape(browser):

    # Use browser to visit the URL

    url = 'https://marshemispheres.com/'

    browser.visit(url)

    # Create a list to hold the images and titles.

    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere.

    html = browser.html
    hemisphere_soup = browser.find_by_css('a.product-item img')



    for i in range(len(hemisphere_soup)): 

        hemisphere = {}

        browser.find_by_css('a.product-item img')[i].click()
        
        element = browser.links.find_by_text('Sample').first
        
        img_url = element['href']
        
        title = browser.find_by_css("h2.title").text
        
        hemisphere["img_url"] = img_url
        
        hemisphere["title"] = title
        
        hemisphere_image_urls.append(hemisphere)
        
        browser.back()

    print("\n================")
    print(hemisphere_image_urls)
    print("=================\n")
    return hemisphere_image_urls 

if __name__ == "__main__":


    # If running as script, print scraped data

    print(scrape_all())





