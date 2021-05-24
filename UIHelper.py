import tkinter as tk
from PIL import ImageTk, Image
import urllib.request, scrapy, globals
from io import BytesIO
from scrapy.crawler import CrawlerProcess

_d = {}
_window = tk.Tk()

class TestSpider(scrapy.Spider):
    name = "test"
    custom_settings = { 'DOWNLOAD_DELAY': 2}
    start_urls = []


    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)


    def parse(self, response):
        global _d

        h = response.xpath("//img/@src").extract()
        h = [item for i, item in enumerate(h) if 0 < i < 10]
        _d = dict(enumerate(h))


def draw_search(index):
    global _d
    p = _d[index][0]
    globals.PIC = p
    _window.destroy()
    return 0


def handle_search(searchTerm):
    q = "q={}".format(searchTerm) #+clipart
    tbm = "tbm=isch"
    # chips = "chips=q:{},g_1:black+and+white".format(q[2:])
    chips = "tbs=itp:lineart"
    url = "https://google.com/search?" + q + '&' + tbm + '&' + chips
    spider1 = TestSpider()
    spider1.start_urls.append(url)

    process = CrawlerProcess()
    process.crawl(TestSpider)
    process.start()

    # Frame B to hold 9 buttons with first 9 google image search results
    frmB = tk.Frame(relief=tk.GROOVE, borderwidth=5)
    global _d

    for i in range(3):
        for j in range(3):
            frm = tk.Frame(master=frmB, relief=tk.RAISED, borderwidth=3)
            frm.grid(row=i, column=j)
            response = urllib.request.urlopen(_d[3*i + j]).read()
            img = Image.open(BytesIO(response))
            img2 = img.resize((200, 200))
            img2 = ImageTk.PhotoImage(img2)
            _d[3*i + j] = [img, img2]
            btnI = tk.Button(master=frm, image=_d[3*i + j][1], command=lambda m=(3*i + j): draw_search(m))
            btnI.pack()
    frmB.pack()


def depictoWindow():
    global _d, _window

    _window.title("DEPICTOREX")
    # Frame A to hold image search term, submit button
    frmA = tk.Frame(relief=tk.GROOVE, borderwidth=5)

    lblSearch = tk.Label(text="Search Term:", master=frmA)
    entSearch = tk.Entry(master=frmA)
    btnSearch = tk.Button(master=frmA, text="Search!", width=8, height=2, bg="black", fg="white", padx=5, pady=5, command=lambda: handle_search(entSearch.get()))
    lblSearch.pack(side=tk.LEFT)
    entSearch.pack(side=tk.LEFT)
    btnSearch.pack(side=tk.LEFT)
    frmA.pack()

    _window.mainloop()

