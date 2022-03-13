from get_books import *


class BOTM:

  botm = dict(
    bread_host="Buddy Read Host",
    avatar_url="https://www.nme.com/wp-content/uploads/2021/07/RickAstley2021.jpg",
    title="Not found",
    description="Not found",
    url="",
    author_name="Not Found",
    author_url="",
    author_icon_url="",
    genres="Not found",
    num_pages="Not found",
    rating="Not found",
    thumbnail="",
    )

  def __init__(self,link):
    self.link = link
    self.scrapebook=scrape_book(self.link)
  
  def setDetails(self,link=None,author=None,pages=None,rating=None,thumbnail=None,description=None,title=None,author_icon_url=None):
    self.botm["author_name"] = self.scrapebook['author']
    self.botm["num_pages"] =self.scrapebook['num_pages']
    self.botm["rating"] =self.scrapebook['average_rating']
    self.botm["thumbnail"]=self.scrapebook['book_thumbnail']
    self.botm["description"] =self.scrapebook["description"]
    self.botm["title"]=self.scrapebook["book_title"]
    self.botm["author_icon_url"]=self.scrapebook['author_thumbnail']
    self.botm["author_url"]=self.scrapebook["author_url"]
    self.botm["genres"]=self.scrapebook['genres']
    self.botm["url"]=self.link