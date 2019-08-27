#!/usr/bin/python
################################################################################
# PYDOORS FOR BBS                                                              #
# VERSION 0.0.0.1                                                              #
################################################################################
#                                                                              #
# PyDoors is free software: you can redistribute it and/or modify              #
# it under the terms of the GNU General Public License as published by         #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# PyDoors is distributed in the hope that it will be useful,                   #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU General Public License for more details.                                 #
#                                                                              #
# You should have received a copy of the GNU General Public License            #
# along with PyDoors.  If not, see <http://www.gnu.org/licenses/>.             #
#                                                                              #
################################################################################

#####################
###               ###
###   API CALLS   ###
###               ###
#####################
## version A000x001 #
#####################

from datetime import datetime as dt
import sys
import os
sys.path.insert(0, (os.environ['PYDOORS']+'/lib'))
from flask import Flask, jsonify, request, render_template 

template_dir = os.path.join(os.environ['PYDOORS'],'templates')
static_dir = os.path.join(os.environ['PYDOORS'],'static')
app = Flask(__name__,template_folder=template_dir,static_url_path='/static')

###################
###   INDEX     ###
###################
@app.route('/')
def index():
  return render_template('root.html')

###
### MAIN
###

if __name__ == '__main__':
  app.run(debug=True,host='127.0.0.1',port=3210)
