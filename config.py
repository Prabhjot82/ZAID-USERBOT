import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "11886515")) #optional
API_HASH = getenv("API_HASH", "eb1a12b864dc44bceb02611d190425f5
") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5037708203").split()))
OWNER_ID = int(getenv("OWNER_ID", "2133969720"))
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "5405451628:AAF7i8Xg4GP3YBSU2JMm5sgFnj0qLKjr3CA")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER")
LOG_GROUP = getenv("LOG_GROUP")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "AQBiMZkAS92U-jt4ch1WhC0sW-N46Dsadk7jSpOgoHgzdEP4oHORFYAp6EX0SScimtSUEXY_0YAkKtlSMBlPVApg5YdTKEEQft2qP2Midj0B-ZqGKczPEp3rwi1MjDC1RmVI3MYQwH-WhVCsJoZngEorwidtvz0nmd2q1NSMcQc4SrWzRIatIo56wQMrNwuAHwJylpkZJOmefK7xRThYxsjydm2DtuZN5DYwqJp4LHSYWC-l4o3pCh9DRC6_DzWnOyvV029r8fbt9B_vLtuqWKyuX6ChkzgEkoWr56EXYpR9K1FHbxrSfyB7yfhA6iZdngVR9FUAjUuHra-6oFmznk9H6yAawgAAAAB_Mcs4AA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
