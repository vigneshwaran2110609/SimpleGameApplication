import numpy as  np
import tkinter as tk
root2=tk.Tk()
root2.title('Game of Cards')
root2.geometry('700x300')
prompt1 = tk.Label(root2, text = 'Rules are: ')
prompt1.pack()
prompt2 = tk.Label(root2, text = '1. Its a 2 player game of cards where each player randomly gets 26 cards...')
prompt2.pack()
prompt3 = tk.Label(root2, text = '2. All the Symbols on the cards are considered equal and the real game is based on number on the face of the cards')
prompt3.pack()
prompt4 = tk.Label(root2, text = '3. Two cards are released by both the players at the same time.. The player whose cards has the lesser should take both the cards')
prompt4.pack()
prompt5 = tk.Label(root2, text = '4. If the number on the cards match, the cards are discarded...')
prompt5.pack()
prompt6 = tk.Label(root2, text = '5. The player who wins the first 50 hands wins first!!!')
prompt6.pack()
prompt7 = tk.Label(root2, text = '6. The player who reaches 0 cards before reaching 20 fins wins ...')
prompt7.pack()
root2.mainloop()
"""A class for creation of card objects"""

symbol = np.array(['Hearts','Clubs','Spade','Diamond'])
rank = np.array(['2','3','4','5','6','7','8','9','10','J','Q','K','A'])
class CardObject:
  def __init__(self,rank,symbol):
    self.rank=rank
    self.symbol=symbol
  def __str__(self):
    return self.rank+" of "+self.symbol

class Cards:
  """A class that creates and stores all card objects"""
  def __init__(self):
    self.cards=[]
    for i in symbol:
      for j in rank:
        self.cards.append(CardObject(j,i))
    self.cards=np.array(self.cards)
  def shuffle(self):
    np.random.shuffle(self.cards)


class Players:
  """A class that creates players and allows us to plays the game """
  def __init__(self):
    self.Player1=np.array([])
    self.Player2=np.array([])
    cardslist=Cards()
    cardslist.shuffle()
    for i in range(0,26):
      self.Player1=np.append(self.Player1,cardslist.cards[i])
      self.Player2=np.append(self.Player2,cardslist.cards[i+26])

  def shufflehands(self):
    np.random.shuffle(self.Player1)
    np.random.shuffle(self.Player2)

  def play(self):
    Player1_win=0
    Player2_win=0
    lis=[["Player1 Card","Player2 Card"]]
    while True:
      if len(self.Player1)==0 or Player1_win == 20:
        newwindow=tk.Tk()
        newwindow.title('Results')
        text_widget = tk.Text(newwindow, width = 50, height =len(lis), font =('Arial',12))
        for i in lis:
          text_widget.insert(tk.END, i[0]+" vs "+i[1]+"\n")
        text_widget.insert(tk.END,'Player 1 wins')
        text_widget.pack(pady = 20)
        newwindow.mainloop()
        return 1
      elif len(self.Player2)==0 or Player2_win == 20:
        newwindow=tk.Tk()
        newwindow.title('Results')
        text_widget = tk.Text(newwindow, width = 40 , height =len(lis), font =('Arial',12))
        for i in lis:
          text_widget.insert(tk.END, i[0]+" vs "+i[1]+"\n")
        text_widget.insert(tk.END,'Player 2 wins')
        text_widget.pack(pady = 20)
        newwindow.mainloop()
        return 2
      Player1_Card=self.Player1[0]
      self.Player1=self.Player1[1:]
      Player2_Card=self.Player2[0]
      self.Player2=self.Player2[1:]
      lis.append([Player1_Card.symbol+" "+Player1_Card.rank,Player2_Card.symbol+" "+Player2_Card.rank])
      if np.where(rank == Player1_Card.rank) > np.where(rank == Player2_Card.rank):
        self.Player2=np.append(self.Player2,Player1_Card)
        self.Player2=np.append(self.Player2,Player2_Card)
        Player1_win+=1
      elif np.where(rank == Player1_Card.rank) < np.where(rank == Player2_Card.rank):
        self.Player1=np.append(self.Player1,Player1_Card)
        self.Player1=np.append(self.Player1,Player2_Card)
        Player2_win+=1
      else:
        self.shufflehands()
def exit_game(win):
  win.destroy()
def play_againf(win):
  global entry
  win.destroy()
  root = tk.Tk()
  root.title('Card Game...')
  root.geometry('300x150')
  prompt = tk.Label(root, text = 'Predict who will win this game 1 or 2: ')
  prompt.pack(pady = 10)
  entry = tk.Entry(root, width =20)
  entry.pack()
  submit = tk.Button(root, text = 'Play', command =  lambda: get_input(root))
  submit.pack(pady = 10)
  root.mainloop()
def get_input(win):
    global entry
    user_input = entry.get()
    win.destroy()
    game = Players()
    if int(user_input) == game.play():
      root1 = tk.Tk()
      root1.title('Card Game...')
      root1.geometry('300x150')
      prompt = tk.Label(root1, text = 'You have predicted correctly!!! ')
      prompt.pack(pady = 10)
      exitbutton = tk.Button(root1, text = 'Exit', command = lambda: exit_game(root1))
      play_again = tk.Button(root1, text = 'Play Again', command = lambda: play_againf(root1))
      exitbutton.pack(pady = 10)
      play_again.pack(pady = 10)
      root1.mainloop()
    else:
      root2 = tk.Tk()
      root2.title('Card Game...')
      root2.geometry('300x150')
      prompt = tk.Label(root2, text = 'Better luck next time!!!')
      prompt.pack(pady = 10)
      exitbutton = tk.Button(root2, text = 'Exit', command = lambda: exit_game(root2))
      play_again = tk.Button(root2, text = 'Play Again', command = lambda: play_againf(root2))
      exitbutton.pack(pady = 10)
      play_again.pack(pady = 10)
      root2.mainloop()
root = tk.Tk()
root.title('Card Game...')
root.geometry('300x150')
prompt = tk.Label(root, text = 'Predict who will win this game: ')
prompt.pack(pady = 10)
entry = tk.Entry(root, width =20)
entry.pack()
submit = tk.Button(root, text = 'Play', command =  lambda: get_input(root))
submit.pack(pady = 10)
root.mainloop()
