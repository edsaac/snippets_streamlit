import streamlit as st
import os 
import subprocess

"# Available resources"

"## CPU"
st.header(f"This machine has {os.cpu_count()} CPU available")
lscpu = subprocess.run(args=["lscpu"], capture_output=True).stdout.decode('utf-8').splitlines()
st.code("\n".join(lscpu))

"## Disk"
dfH = subprocess.run(args=["df", "-H"], capture_output=True).stdout.decode('utf-8').splitlines()
ldisk = "\n".join(dfH)
st.code(f"{ldisk}")

"## Memory"
freeg = subprocess.run(args=["free", "-g"], capture_output=True).stdout.decode('utf-8').splitlines()
lmemo = "".join([l+'\n' for l in freeg])
st.code(f"{lmemo}")

