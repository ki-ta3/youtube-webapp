import streamlit as st
import time

st.title('streamlit 超入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()#空を追加
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)


#st.write('DataFrame')

#df = pd.DataFrame({
    #'1列目':[1,2,3,4],
    #'2列目':[10,20,30,40]
#})

#st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)
#縦横の引数を指定できるのはdataframeのみ。writeはできない

#上書き保存　ctrl+S

#st.table(df.style.highlight_max(axis=0))
#tableとdataframeの違い、tableはソートできない

#"""
# 章
## 節
### 項
#```python
#import streamlit as st
#import numpy as np
#import pandas as pd
#```
#"""

#df = pd.DataFrame(
    #np.random.rand(100,2)/[50,50]+[35.69,139.70],
    #columns=['lat','lon']
#)
#st.line_chart(df)
#st.area_chart(df)
#st.bar_chart(df)
#緯度、経度を実際のマップ上に表示する
#st.map(df)

#st.write('Display Image')

#img = Image.open('ファイル_002.jpeg')
#st.image(img,caption='ゆるきゃん',use_column_width=True)

#インタラクティブなウィジェット

st.write('Display Image')

# if st.checkbox('Show Image'):
#     img = Image.open('ファイル_002.jpeg')
#     st.image(img,caption='ゆるきゃん',use_column_width=True)

#一括コメントアウト
#ctrl+k押してctrl+c

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# con = st.sidebar.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味:',text,'です。'
# 'コンディション:',con


left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')


# text = st.text_input('あなたの趣味を教えてください')
# con = st.slider('あなたの今の調子は？',0,100,50)

# 'あなたの趣味:',text,'です。'
# 'コンディション:',con
