import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

_, col, _ = st.columns([2,6,2])
col.header("Streamlit 시각화")
# 실행 streamlit run iris.py
''# 한칸 띄우기
dfIris =sns.load_dataset('iris')
st.write(dfIris.head())
colors={'setosa':'red','virginica':'green','versicolor':'blue'}
st.sidebar.title('Iris Species')

with st.sidebar:
    selectX = st.selectbox("X 변수선택:",['sepal_length','sepal_width','petal_length','petal_width'])
    ''
    selectY = st.selectbox("Y 변수선택:",['sepal_length','sepal_width','petal_length','petal_width'])
    ''
    selectSpecies = st.multiselect("붓꽃 유형 선택(:blue[다중]):",[
        "setosa","versicolor",'virginica'])
    ''
    selectAlpha = st.slider("alpha 설정:",0.1,1.0,0.5)
    
    # 선택된 붓꽃 유형별로 산점도로 시각화 표현
    
if selectSpecies:
    fig = plt.figure(figsize=(7,5))
    for aSpecies in selectSpecies:
        df = dfIris[dfIris.species == aSpecies]
        plt.scatter(df[selectX],df[selectY],color = colors[aSpecies],alpha=selectAlpha, label=aSpecies)
    plt.legend(loc='lower right')
    plt.xlabel(selectX)
    plt.ylabel(selectY)
    plt.title("Iris Scatter Plot")
    st.pyplot(fig)
else:
    st.warning("붓꽃의 유형을 선택해주세요")