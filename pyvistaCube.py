import streamlit as st
import pyvista as pv
from stpyvista import stpyvista

"Behavior of other images stays unaltered"
st.image("https://placekitten.com/g/500/400", caption="Hello")

plotter = pv.Plotter(window_size=[250,250])
mesh = pv.Cube()
plotter.add_mesh(mesh)
plotter.set_background("pink")
stpyvista(plotter, caption="Holi"*500)