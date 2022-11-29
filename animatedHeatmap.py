# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import numpy as np
# import streamlit as st
# from itertools import cycle

# ## Generate some data
# randomdata = np.random.random(size=(5,3,3))
# harvest_cycle = cycle([i for i in randomdata])
# harvest = next(harvest_cycle)

# ## Initialize figure
# fig,ax = plt.subplots(figsize=[3,3])
# ax.set_aspect('equal')
# ax.grid(which = 'minor',color='w', linestyle='-', linewidth=2)
# heatmap = ax.imshow(harvest)

# # st.markdown("## :camera: Initial condition")
# # st.pyplot(fig)

# ## Animate 
# def update(frame_number):
#     ## Clears the data passed to the axes
#     ##  This is important so the final figure does not store
#     ##  every single frame and slows everything down 
#     ax.cla()

#     ax.imshow(next(harvest_cycle))
#     ax.set_title(f"Frame: {frame_number}",fontsize=24)

# animation = FuncAnimation(fig,update,frames=10)

# ## Saved mp4 video
# # animation.save("movie.mp4")

# ## Keep jshmtl representation
# animjs = animation.to_jshtml()

# ### Inject JS for autoplay
# import re

# click_on_play = """document.querySelector('.anim-buttons button[title="Play"]').click();"""
# pattern = re.compile(r"(setTimeout.*?;)(.*?})", re.MULTILINE | re.DOTALL)
# newanimjs = pattern.sub(rf"\1 \n {click_on_play} \2", animjs)

# # # st.markdown("## :movie_camera: Enconded MP4 movie")
# # # st.video("movie.mp4")

# #st.code(animjs)

# st.markdown("## :control_knobs: Using `jshtml` from matplotlib")

# cols = st.columns(2)

# with cols[0]:
#     "### No modification"
#     st.components.v1.html(animjs,height=600)

# with cols[1]:
#     "### Autoplay"
#     st.components.v1.html(newanimjs,height=600)

# # st.code(animjs, language="html")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import streamlit as st
from itertools import cycle

st.set_page_config(layout="wide")

## Generate some data
randomdata = np.random.random(size=(5,3,3))
harvest_cycle = cycle([i for i in randomdata])
harvest = next(harvest_cycle)

## Initialize figure
fig,ax = plt.subplots(figsize=[3,3])
ax.set_aspect('equal')
ax.grid(which = 'minor',color='w', linestyle='-', linewidth=2)
heatmap = ax.imshow(harvest)

## Animate 
def update(frame_number):
    ## Clears the data passed to the axes
    ##  This is important so the final figure does not store
    ##  every single frame and slows everything down 
    ax.cla()

    ax.imshow(next(harvest_cycle))
    ax.set_title(f"Frame: {frame_number}",fontsize=24)

animation = FuncAnimation(fig,update,frames=10)

## Export jshmtl representation
animjs = animation.to_jshtml()

### Inject JS for autoplay
import re

click_on_play = """document.querySelector('.anim-buttons button[title="Play"]').click();"""
pattern = re.compile(r"(setTimeout.*?;)(.*?})", re.MULTILINE | re.DOTALL)
new_animjs = pattern.sub(rf"\1 \n {click_on_play} \2", animjs)

st.markdown("## :control_knobs: Using `jshtml` from matplotlib")

cols = st.columns(2)

with cols[0]:
    "### 🛑 No modification"
    st.components.v1.html(animjs,height=600)

with cols[1]:
    "### ▶️ Autoplay"
    st.components.v1.html(new_animjs,height=600)

# st.code(animjs, language="html")

