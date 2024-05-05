import streamlit as st
from st_pages import show_pages_from_config

from pathlib import Path
import pandas as pd

from components.utils import coeff_error, coeff_flip_signs, significance_error
  

if __name__ == '__main__':
  show_pages_from_config()
  
  data = pd.read_csv(Path('static/data/integrated_data.csv'))
  st.write(data.head())