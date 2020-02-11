#!/usr/bin/env bash

set -euo pipefail

# Download 'Zooplankton of Lebanon' dataset
wget http://ipt.vliz.be/eurobis/archive.do?r=zoo_lebanon
unzip archive.do?r=zoo_lebanon -d data
rm archive.do?r=zoo_lebanon
