#!/usr/bin/python3
#
# PyDoors is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Lisa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Lisa.  If not, see <http://www.gnu.org/licenses/>.

### ENTER HOSTNAME OR IP HERE IN PARENTHIS "

url = "http://127.0.0.1:3210"

import requests

def getVer():
  try:
    res=requests.get(url)
    print(res.text)
  except Exception:
    print ("ERR [ FAILED TO EXECUTE REQUEST ] A0001x0001 (1) : Can't get url via requests")
    exit()
  input("Press ENTER to continue.")

if __name__ == '__main__':
  getVer()
