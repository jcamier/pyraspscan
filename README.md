# pyraspscan
Barcode Scanning for Raspberry Pi
created by Jim Vogel and Jacques Camier

# Install necessary packages to allow Raspberry Pi to run Python 3.7.2
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash

# Update bash to run pyenv
nano ~/.bashrc

export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

`source ~/.bashrc`

# Install Python 3.7.2 and create virtual environment
pyenv install 3.7.2
cd pyraspscan
pyenv global 3.7.2
pyenv virtualenv pyraspscan
pyenv local pyraspscan

# Git clone raspscan and install necessary python packages, assumes you already have git installed
git clone https://github.com/jcamier/pyraspscan.git
pip install -r requirements.txt

Instructions:

put barcode scanner in USB virtual COM mode

make sure you only have 1 serial device attached (for now)

start api in a terminal with hug -f api.py

start app in a separate terminal with python app.py

scan something... watch hug respond


