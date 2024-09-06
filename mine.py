import datetime as date
import time
import sync
import json
import hashlib
import requests
import os
import glob
from block import Block
#from blockchain import Block #-------------------> changed later
from config import *
import utils

 

def mine_for_block(data):
  print ("mine for block sync")
  current_chain = sync.sync_local() #gather last node
  print ("mine for block sync done")
  prev_block = current_chain.most_recent_block()
  new_block = mine_blocks(prev_block,data)
  new_block.self_save()
  return new_block

def mine_blocks(last_block,data1):
  index = int(last_block.index) + 1
  timestamp = date.datetime.now().strftime('%S')
  data = data1 
  previous = last_block.hash
  nonce = 0

  block_info_dict = utils.dict_from_block_attributes(index=index, timestamp=timestamp, data=data, previous=previous, nonce=nonce)
  new_block = Block(block_info_dict) #--------------------------->integrated later
  return find_valid_nonce(new_block)

def find_valid_nonce(new_block):
  print ("mining for block %s" % new_block.index)
  new_block.update_self_hash()#calculate_hash(index, prev_hash, data, timestamp, nonce)
  while str(new_block.hash[0:NUM_ZEROS]) != '0' * NUM_ZEROS:
    new_block.nonce += 1
    new_block.update_self_hash()

  print ("block %s mined. Nonce: %s" % (new_block.index, new_block.nonce))

  assert new_block.is_valid()
  return new_block #we mined the block. We're going to want to save it

  #return True

 

