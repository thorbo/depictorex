import tkinter as tk
from PIL import ImageTk, Image
import urllib.request, scrapy, globals
from io import BytesIO
from scrapy.crawler import CrawlerProcess

# Global variables scoped to this module.
# Dictionary of 9 images and UI window.
_d = {}
_window = tk.Tk()


class TestSpider(scrapy.Spider):
    """Scrapy spider to crawl url and load images 1 thru 9 into _d"""
    name = "test"
    custom_settings = {'DOWNLOAD_DELAY': 2}
    start_urls = []

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        global _d
        h = response.xpath("//img/@src").extract()
        h = [item for i, item in enumerate(h) if 0 < i < 10]
        _d = dict(enumerate(h))
        return 0


def draw_search(index):
    """load globals.PIC with selected image"""
    global _d
    globals.PIC = _d[index][0]
    _window.destroy()
    return 0


def handle_search(search_term):
    # Builds google url for search term, adding 'GET' modifiers to narrow search
    q = "q={}".format(search_term)
    # q += "+clipart"
    tbm = "tbm=isch"
    # chips = "chips=q:{},g_1:black+and+white".format(q[2:])
    chips = "tbs=itp:lineart"
    url = "https://google.com/search?" + q + '&' + tbm + '&' + chips

    # Creates scrapy spider, starts crawl process and twisted reactor
    spider1 = TestSpider()
    spider1.start_urls.append(url)
    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()

    # Build Frame B to hold 9 buttons with first 9 google image search results
    frm_b = tk.Frame(relief=tk.GROOVE, borderwidth=5)
    global _d

    for i in range(3):
        for j in range(3):
            frm = tk.Frame(master=frm_b, relief=tk.RAISED, borderwidth=3)
            frm.grid(row=i, column=j)
            response = urllib.request.urlopen(_d[3*i + j]).read()
            img = Image.open(BytesIO(response))
            img2 = img.resize((200, 200))
            img2 = ImageTk.PhotoImage(img2)
            _d[3*i + j] = [img, img2]
            btn_img = tk.Button(master=frm, image=_d[3*i + j][1], command=lambda m=(3*i + j): draw_search(m))
            btn_img.pack()
    frm_b.pack()


def depicto_window():
    global _d, _window

    # Frame A to hold image search term, submit button
    _window.title("DEPICTOREX")
    frm_a = tk.Frame(relief=tk.GROOVE, borderwidth=5)
    
    lbl_search = tk.Label(text="Search Term:", master=frm_a)
    ent_search = tk.Entry(master=frm_a)
    btn_search = tk.Button(master=frm_a, text="Search!", width=8, height=2, bg="black", fg="white", padx=5, pady=5, 
                           command=lambda: handle_search(ent_search.get()))
    lbl_search.pack(side=tk.LEFT)
    ent_search.pack(side=tk.LEFT)
    btn_search.pack(side=tk.LEFT)
    frm_a.pack()

    _window.mainloop()
