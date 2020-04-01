import os
import random
import sys
import wx

MAX_TRIES = 6

def local_filename(filename):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

class HangmanWindow(wx.Frame):
    def __init__(self, words, parent=None, title="Hangman", size=(640, 480)):
        super(HangmanWindow, self).__init__(parent, title=title, size=size)
        self.words = words
        self.InitUI()

    def InitUI(self):
        # load the graphics
        self.bitmaps = {
                (MAX_TRIES - x): wx.Bitmap(local_filename('hangman-%d.gif' % x), wx.BITMAP_TYPE_GIF) for x in range(MAX_TRIES + 1)
        }

        # preset colours
        self.colours = wx.ColourDatabase()

        # create the main panel
        self.panel = wx.Panel(self)

        # create the text field
        self.guessWordText = wx.StaticText(self.panel, label="C______R", pos=(20, 20))
        self.guessWordText.SetFont(wx.Font(32, wx.DEFAULT, wx.NORMAL, wx.BOLD))

        # create the bitmap control
        self.image = wx.StaticBitmap(self.panel, pos=(20, 100))

        # create the keyboard
        self.keyboardButtons = self.CreateKeyboardButtons(350, 100, 40, 10, 5)

        # create the menu bar
        self.SetMenuBar(self.CreateMenuBar())

        # create a status bar
        self.CreateStatusBar()

        # reset the game to a valid state
        self.ResetGame()

    def CreateMenuBar(self):
        # set up the menu
        filemenu = wx.Menu()
        menuNew = filemenu.Append(wx.ID_NEW, "&New\tCTRL+N", "Start a new game")
        menuAbout= filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT, "E&xit", "Terminate the program")

        # create the menu bar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu,"&File")

        # events
        self.Bind(wx.EVT_MENU, self.OnNew, menuNew)
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        return menuBar

    def OnNew(self, e):
        if (self.triesLeft == 0) or (wx.YES == wx.MessageBox(
                "Do you want to start a new game?", "Confirm", wx.YES_NO)):

            self.ResetGame()

    def OnAbout(self, e):
        wx.MessageBox("This app was created by Simona Dimitrova (c) 2020", "About")

    def OnExit(self, e):
        self.Close()

    def CreateKeyboardButtons(self, offsetX, offsetY, size, margin, columns):
        def generateKey(id, ch):
            row = id // columns
            column = id % columns
            pos = (offsetX + size * column, offsetY + size * row)
            button = wx.ToggleButton(self.panel, id, label=ch, pos=pos, size=(size, size))
            button.Bind(wx.EVT_TOGGLEBUTTON, self.KeyboardButtonPressed)
            return button

        alphabet = [ x for x in range(ord('A'), ord('Z') + 1) ]
        return [ generateKey(id, chr(ch)) for id, ch in enumerate(alphabet) ]

    def KeyboardButtonPressed(self, e):
        # No need to check the pressed state:
        # The button is disabled as soon as it is pressed,
        # so if it were pressed it was OFF.
        btn = e.GetEventObject()
        btn.Disable()
        self.GuessChar(btn.GetLabel())
        self.UpdateUI()

    def GuessChar(self, ch):
        if self.triesLeft:
            self.guessedChars.add(ch)

            # Penalty
            if ch not in self.word:
                self.triesLeft -= 1

    def ResetGame(self):
        # select a new word
        self.word = random.choice(self.words).upper()
        self.triesLeft = MAX_TRIES
        self.guessedChars = set()

        # reset the keyboard buttons
        for b in self.keyboardButtons:
            b.SetValue(False)
            b.Enable(True)

        # now update the UI state
        self.UpdateUI()

    def UpdateUI(self):
        word = self.word # to save a few keystrokes

        # Create a visual representation of the guessed state of the word
        # first and last chars are always visible
        # the ones in the middle are visible if already guessed
        word = [ word[0] ] + [ w if w in self.guessedChars else "_" for w in word[1:-1]] + [ word[-1] ]

        # Check whether won or not (no words have _ in them)
        won = "_" not in word
        lost = self.triesLeft == 0

        # Fill in the guess word text field
        self.guessWordText.SetLabelText(" ".join(word))

        # Fill in the status bar
        if won:
            statusText = "Congratulations. You have won"
            color = self.colours.Find("Forest Green")
        elif lost:
            statusText = "You have lost"
            color = self.colours.Find("Red")
        else:
            statusText = "You have {} tries left. Guessed: {}".format(
                    self.triesLeft, ", ".join(self.guessedChars))
            color = self.colours.Find("Black")

        self.StatusBar.SetStatusText(statusText)
        self.guessWordText.SetForegroundColour(color)

        # Disable buttons if game over
        if lost or won:
            # Disable all buttons
            for b in self.keyboardButtons:
                b.Disable()

        # Update the image
        self.image.SetBitmap(self.bitmaps[self.triesLeft])

def parseWords(filename):
    # split the file by white space
    with open(filename, 'r') as f:
        return f.read().split()

words = parseWords(local_filename("words.txt") if len(sys.argv) == 1 else sys.argv[1])

# Create an application object.
app = wx.App()

# Create and show the main window
frm = HangmanWindow(words)
frm.Show()

# Start the event loop.
app.MainLoop()
