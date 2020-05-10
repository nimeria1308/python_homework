import xml.etree.ElementTree as ET
import wx
import wx.html

# import urlopen both in Python 2 and 3
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

NBU_RSS_URL = 'http://rss.slashdot.org/Slashdot/slashdot'
NS = { "rss" : "http://purl.org/rss/1.0/" }

class MainWindow(wx.Frame):
    def __init__(self, items, *args, **kw):
        super(MainWindow, self).__init__(*args, **kw)
        self.InitUI(items)

    def InitUI(self, items):
        # create the main panel
        panel = wx.Panel(self)

        self.items = items

        # create the listbox
        self.list = wx.ListBox(panel, choices=[ item[0] for item in items])

        # create the HTML view
        self.html = wx.html.HtmlWindow(panel)

        # Automatically resize the listbox/html
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.list, 1, wx.EXPAND)
        sizer.Add(self.html, 4, wx.EXPAND)
        panel.SetSizer(sizer)

        # bind the listbox to the event handler
        self.Bind(wx.EVT_LISTBOX, self.OnListBox, self.list)

    def OnListBox(self, e):
        # Get the index
        index = self.items[e.GetInt()][1]

        # set the HTML content using the description matching that index
        self.html.SetPage(index)

def get_items():
    # request RSS data
    with urlopen(NBU_RSS_URL) as rss:
        # parse the request (file object)
        tree = ET.parse(rss)
        root = tree.getroot()

        # fill in the items
        return [
            (c.find("rss:title", NS).text, c.find("rss:description", NS).text)
                for c in root.findall("rss:item", NS)]

def main():
    # get the items from the RSS
    items = get_items()

    # Create an application object.
    app = wx.App()

    # Create and show the main window
    frm = MainWindow(items, None, title="NBU RSS feed explorer", size=(640, 480))
    frm.Show()

    # Start the event loop.
    app.MainLoop()

if __name__ == '__main__':
    main()
