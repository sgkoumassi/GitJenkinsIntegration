__author__ = 'rudi'

import httplib2
import re
import wx
import wx.html as hw
import sys

class HTTPConnection:
    PYVERSION = 2

    def __init__(self, langue):
        if langue not in ['fr', 'en', 'de']:
            raise Exception("la langue n'existe pas")
        else:
            self.langue = langue
        HTTPConnection.PYVERSION =  sys.version_info[0]

    def get(self, page):
        h = httplib2.Http(".cache")

        self.url = "http://{0}.wikipedia.org/wiki/{1}".format(
            self.langue,
            page.replace(' ', '_')
        )
        reponse, contenu = h.request(self.url, "GET")

        m = re.search('charset=(\S+)',reponse['content-type'], re.IGNORECASE)

        contenu = contenu.decode(m.group(1))

        cles = ['content-location', 'age', 'status', 'last-modified']
        mareponse = { c: reponse[c] for c in cles }

        for t in mareponse.items():
            print('{0} = {1}'.format(*t))

        self.page = contenu



class MyFrame(wx.Frame):
    ID_CLOSE = 1

    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(400, 290))
        self.panel = wx.Panel(self, wx.ID_ANY)

        self.__do_layout()

    def __do_layout(self):
        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        htmlwin = hw.HtmlWindow(self.panel, -1, style=wx.NO_BORDER)
        htmlwin.SetBackgroundColour(wx.RED)
        htmlwin.SetStandardFonts()

        self.httpConnection = HTTPConnection('fr')
        self.httpConnection.get('Kruder und Dorfmeister')
        htmlwin.SetPage(self.httpConnection.page)

        vbox.Add((-1, 10), 0)
        vbox.Add(htmlwin, 1, wx.EXPAND | wx.ALL, 9)

        buttonOk = wx.Button(self.panel, MyFrame.ID_CLOSE, 'Ok')

        self.Bind(wx.EVT_BUTTON, self.OnClose, id=MyFrame.ID_CLOSE)

        hbox.Add((100, -1), 1, wx.EXPAND | wx.ALIGN_RIGHT)
        hbox.Add(buttonOk, flag=wx.TOP | wx.BOTTOM | wx.RIGHT, border=10)
        vbox.Add(hbox, 0, wx.EXPAND)

        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def OnClose(self, event):
        self.Close()

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, -1, "v2bPedia")
    app.MainLoop()
