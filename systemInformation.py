import streamlit as st
import os 
import subprocess

"# Available resources"

"## CPU"
"### `os.cpu_count()`"
f"This machine has {os.cpu_count()} CPU available"

"### `lscpu`"
lscpu = subprocess.run(args=["lscpu"], capture_output=True).stdout.decode('utf-8')
st.code(f"{lscpu}")

"## Disk"
"### `df -H`"
dfH = subprocess.run(args=["df", "-H"], capture_output=True).stdout.decode('utf-8')
st.code(dfH)

"## Memory"
"### `free -h`"
freeg = subprocess.run(args=["free", "-h"], capture_output=True).stdout.decode('utf-8')
st.code(f"{freeg}")

