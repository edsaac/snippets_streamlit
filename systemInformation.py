import streamlit as st
import os 
import subprocess

NCPUS = os.cpu_count()
"# CPU"
st.header(f"This machine has {NCPUS} CPU available")

"# Memory"
NMEMORY = subprocess.run(args=["free", "-g"], capture_output=True).stdout.decode('utf-8').splitlines()
lmemo = "".join([l+'\n' for l in NMEMORY])
st.code(f"{lmemo}")

"# Disk"
NDISK = subprocess.run(args=["df", "-H"], capture_output=True).stdout.decode('utf-8').splitlines()
ldisk = "".join([l+'\n' for l in NDISK])
st.code(f"{ldisk}")
