# seleniumのインポート
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import random
import numpy as np
import time
import copy as cp
from Agent.Montecarlo_Player import Montecarlo_Player

#Montecarlo_Player
player = Montecarlo_Player(100)

# Chromeの起動と2048の起動
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/') #「2048」のページのURL

#HTMLのelement取得
html_elem = browser.find_element_by_tag_name('html')
game_message_elem = browser.find_element_by_class_name('game-message')
tile_container_elem = browser.find_element_by_class_name('tile-container')
score_container_elem = browser.find_element_by_class_name('score-container')

#盤面ディクショナリ
board = np.zeros((4,4),dtype = int)#現在の盤面

#キーディクショナリ
#0 1 2 3 
#↑↓←→
Key_List = {"u":Keys.UP, "d":Keys.DOWN, "l":Keys.LEFT, "r":Keys.RIGHT}

def get_board():
	for y in range(1,5):
		for x in range(1,5):
			try:
				pos = str(x)+"-"+str(y)
				tile_pos = "tile-position-"+pos
				tile = tile_container_elem.find_elements_by_class_name(tile_pos)
				try:
					board[y-1][x-1] = int(tile[2].text)
				except:
					board[y-1][x-1] = int(tile[0].text)
			except:
				board[y-1][x-1] = 0

def print_score():
	score = score_container_elem.text.split("\n")
	print("score:",score[0])

def send_allows():
    while game_message_elem.text == "":
        print_score()
        get_board()
        print(board)
        action = player.select_action(board)
        html_elem.send_keys(Key_List[action])

if __name__ =="__main__":
	start = time.time()
	send_allows()
	print_score()
	#browser.quit()
	end = time.time()
	print("time:",end - start)
	
	