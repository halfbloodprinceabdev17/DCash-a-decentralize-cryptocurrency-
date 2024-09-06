from block import Block
from flask import Flask, jsonify, request
from flask import Flask, request, render_template
import sync
import requests
import os
import time
from threading import Thread
 
import json
import sys
import mine
from config import *
import random
node = Flask(__name__)

sync.sync(save=True) #want to sync and save the overall "best" blockchain from peers
 
def Only_data(json_blocks):
   d=[]
   data = json.loads(json_blocks)
   for i in data:
     data1= dict(i)
     d.append(data1['data'])
   return d
def issame(list1,list2):
  if(list1 == list2):
    return True
  else:
    return False


def select_random_elements(lst, n):
    random_elements = random.sample(lst, n)
    return random_elements
def BroadCast(s_port,message,node_list):
  ports = node.config['ports']
  ports_list = list(ports.keys())
  sender_port = int(s_port) 
  recipient1 = select_random_elements(node_list,2)
  recipient1 = list(recipient1)
  print(recipient1)
  print(sender_port,"/n",recipient1,"/n",ports_list)
  for recipient in recipient1:
    if sender_port in ports_list and recipient in ports_list and sender_port != recipient:
      ports[recipient].append(message)
      r = str(recipient)
      f = open("NodeData/ChainData"+r+".txt", "w")
      f.write(message)
      f.close()
      return True
  return False
#@node.route('/check',methods=['GET'] )
#def check():

def reload():
  time.sleep(10)
  blockchain()

@node.route('/blockchain.json', methods=['GET'])
def blockchain():
  reload_thread = Thread(target=reload)
  reload_thread.start()
  local_chain = sync.sync_local() #update if they've changed
  # Convert our blocks into dictionaries
  # so we can send them as json objects later
  json_blocks = json.dumps(local_chain.block_list_dict())
  f = open("ChainData.txt", "w")
  f.write(json_blocks)
  print("\n New Eppoch \n")
  print(BroadCast(port,json_blocks,ports))
  print(node.config['ports'])
  f.close()
 
  return json_blocks

@node.route('/mined', methods=['POST'])
def mined():
  possible_block_data = request.get_json()
  print (possible_block_data)
  #validate possible_block
  possible_block = Block(possible_block_data)
  if possible_block.is_valid():
    #save to file to possible folder
    index = possible_block.index
    nonce = possible_block.nonce
    filename = BROADCASTED_BLOCK_DIR + '%s_%s.json' % (index, nonce)
    with open(filename, 'w') as block_file:
      json.dump(possible_block.to_dict(), block_file)
    return jsonify(confirmed=True)
  else:
    #ditch it
    return jsonify(confirmed=False)

 
@node.route("/")
@node.route("/index")
def index():
    return render_template('node.html')

if __name__ == '__main__':
 
  ports = [5001, 5002, 5003]  # List of ports to run the Flask app
  node.config['ports'] = {port: [] for port in ports}
  print(node.config['ports'])   
  if len(sys.argv) >= 2:
    port = sys.argv[1]
  else:
    port = 5001
  node.run(port=port)
  
