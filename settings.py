from dotenv import load_dotenv

load_dotenv()

from os import getenv
from dotmap import DotMap

config = DotMap()

config.endpoint = getenv("ENDPOINT", "http://localhost:8000/scan")
config.serial_port = getenv("SERIAL_PORT", "/dev/ttyACM0")
config.baud = int(getenv("BAUD", "115200"))
config.machine_id = getenv("MACHINE_ID", "dev_machine")
config.magic_str = getenv("MAGIC_CHARS", "cv")

config.api_key = getenv("API_KEY", "jackjim")

if __name__ == "__main__":
    with open(".env", "w") as f:
        for key, value in config.items():
            f.write(f"{str(key).upper()}={value}\n")
