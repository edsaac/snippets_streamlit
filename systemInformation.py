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

"## Processes"
"### `top -b -n 1 | head -n 30`"
sortBy = st.radio("Sort by", ["%MEM", "%CPU"])
topn = subprocess.run(args=f"top -bc -w 300 -n 1 -o +{sortBy}".split(), capture_output=True).stdout.decode('utf-8').splitlines()[4:50]
st.code("\n".join(topn))

