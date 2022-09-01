#!/usr/bin/env python
# coding: utf-8

# In[33]:


# Import Splinter and BeautifulSoup

from splinter import Browser

from bs4 import BeautifulSoup as soup

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd


# In[34]:


executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless = False)


# In[35]:


# Visit the mars nasa news site

url = 'https://redplanetscience.com'

browser.visit(url)

# Optional delay for loading the page

browser.is_element_present_by_css('dv.list_text', wait_time = 1)


# In[36]:


html = browser.html

news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[37]:


slide_elem.find('div', class_ = 'content_title')


# In[38]:


# Use the parent element to find the first 'a' tag and save it as 'news_title'

news_title = slide_elem.find('div', class_ = 'content_title').get_text()

news_title


# In[39]:


# Use the parent element to find the paragraph text

news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

news_p


# #### Featured Images

# In[40]:


# Visit URL

url = 'https://spaceimages-mars.com'

browser.visit(url)


# In[41]:


# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]

full_image_elem.click()


# In[42]:


# Parse the resulting html with soup

html = browser.html

img_soup = soup(html, 'html.parser')


# In[43]:


# Find the relative image url

img_url_rel = img_soup.find('img', class_ = 'fancybox-image').get('src')

img_url_rel


# In[44]:


# Use the base URL to create an absolute URL

img_url = f'https://spaceimages-mars.com/{img_url_rel}'

img_url


# In[45]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['description', 'Mars', 'Earth']

df.set_index('description', inplace=True)

df


# In[46]:


browser.quit()


# CHALLENGE CODE

# In[47]:


# Import Splinter, BeautifulSoup, and Pandas

from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager


# In[48]:


# Set the executable path and initialize Splinter

executable_path = {'executable_path': ChromeDriverManager().install()}

browser = Browser('chrome', **executable_path, headless=False)


# ### Visit the NASA Mars News Site

# In[49]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[50]:


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')


# In[51]:


slide_elem.find('div', class_='content_title')


# In[52]:


# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()

news_title


# In[53]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

news_p


# ### JPL Space Images Featured Image

# In[54]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[55]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[56]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup


# In[57]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

img_url_rel


# In[58]:


# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Mars Facts

# In[59]:


df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()


# In[60]:


df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df


# In[61]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# ### Hemispheres

# In[62]:


# Use browser to visit the URL

url = 'https://marshemispheres.com/'

browser.visit(url)


# In[63]:


# Create a list to hold the images and titles.

hemisphere_image_urls = []

# Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
hemisphere_soup = browser.find_by_css('a.product-item img')



for i in range(len(hemisphere_soup)): 

    hemispheres = {}

    browser.find_by_css('a.product-item img')[i].click()
    
    element = browser.links.find_by_text('Sample').first
    
    img_url = element['href']
    
    title = browser.find_by_css("h2.title").text
    
    hemispheres["img_url"] = img_url
    
    hemispheres["title"] = title
    
    hemisphere_image_urls.append(hemispheres)
    
    browser.back()


# In[64]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[65]:


# Quit the browser browser

browser.quit()

