# pyraspscan

Barcode Scanning for Raspberry Pi
created by Jim Vogel and Jacques Camier

This has only been tested against python 3.7.2, it may work for other versions.

## Installation

We use pyenv on raspberry pi to manage the python version

the instructions following include installing pyenv on a virgin raspberry pi image.

### Install necessary packages to allow Raspberry Pi to run Python 3.7.2

build requirements

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python-openssl git
```

pyenv installer

```bash
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

### Update bashrc to run pyenv

run `vim ~/.bashrc`

add this to the end of the file

```bash
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "\$(pyenv virtualenv-init -)"
```

then run:

`source ~/.bashrc`

### Clone the repo

```bash
git clone https://github.com/jcamier/pyraspscan.git
```

### Install Python 3.7.2 and create virtual environment

run these commands

```bash
pyenv install 3.7.2
cd pyraspscan
pyenv global 3.7.2
pyenv virtualenv pyraspscan
pyenv local pyraspscan
```

### install necessary python packages

```bash
pip install -r requirements.txt
```

## Usage

1. put barcode scanner in USB virtual COM mode (should be an option in the instructions booklet)
2. start api in a terminal with `hug -f api.py`
3. start app in a separate terminal with `python app.py`
4. scan something and watch the console logs of both apps

## env file

example env file with all the default values

```env
ENDPOINT=http://localhost:8000/scan
SERIAL_PORT=/dev/ttyACM0
BAUD=115200
MACHINE_ID=dev_machine
MAGIC_STR=cv
API_KEY=jackjim
```
