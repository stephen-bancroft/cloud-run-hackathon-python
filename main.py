
# Copyright 2020 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# F <- move Forward
# R <- turn Right
# L <- turn Left
# T <- Throw

import os
import logging
import random
import json
import sys
from flask import Flask, request

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
logger = logging.getLogger(__name__)

app = Flask(__name__)
moves = ['F', 'T', 'L', 'R']
FILENAME = 'move.txt'
API = 'https://cloud-run-hackathon-python-hjvbqrp67q-uc.a.run.app'

@app.route("/", methods=['GET'])
def index():
    return "Let the battle begin!"

@app.route("/", methods=['POST'])
def move():
    request.get_data()
    logger.info(request.json)
    #return moves[random.randrange(len(moves))]
    
    # Get my position on the grid
    X = request.json["arena"]["state"][API]['x']
    Y = request.json["arena"]["state"][API]['y']
    DIR = request.json["arena"]["state"][API]['direction']
    
    try:
      with open(FILENAME) as f:
        lines = f.read()
      if lines == 'R':
        MOVE = 'T'
      if lines == 'T':
        MOVE = 'R'
    except IOError: 
        MOVE = 'T'

    filehandle = open(FILENAME, 'w')
    filehandle.write(MOVE)
    filehandle.close()
    return (MOVE)
    

if __name__ == "__main__":
  app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
  
