#   Copyright 2013 Nathan C. Keim
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import sys

from workflow import Workflow

def main(wf):
    arg = wf.args[0]
    try:
        port = int(arg)
    except ValueError:
        newserv = arg
    else:
        newserv = 'http://localhost:%i' % port

    wf.settings['server'] = newserv
    wf.clear_cache()

    sys.stdout.write(newserv)  # For notification
    return 0

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))
