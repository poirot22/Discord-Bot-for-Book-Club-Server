from english_words import english_words_lower_alpha_set
import random



class Hangman:
  
  def __init__(self):
    self.word=random.choice(list(english_words_lower_alpha_set))
    self.chances=len(self.word)+10
    self.dash=["-" for i in range(len(self.word))]
    self.win=False
    self.began=False
  



  def guess(self,word,dash,chances,a):
    for i in range(len(self.word)):
      if self.word[i]==a.lower() and self.chances>=0:
        self.dash[i]=a
    return self.dash
  
  def wordSolved(self,dash):
    if "-" not in self.dash:
      return True
    return False
  
  def newWord(self,word,dash,chances):
    self.word=random.choice(list(english_words_lower_alpha_set))
    self.dash=["-" for i in range(len(self.word))]
    self.chances=len(self.word)+10
  

   


