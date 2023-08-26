import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)
'Done!'

st.write('DataFrame')

df = pd.DataFrame({
    '1列目': [1, 2, 3, 4],
    '2列目': [10, 20, 30, 40]
    })

# st.dataframe(df.style.highlight_max(axis=0), width=300, height=300)
st.table(df.style.highlight_max(axis=0))

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""

df = pd.DataFrame(np.random.rand(20, 3), columns=['a', 'b', 'c'])

st.dataframe(df)

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

df = pd.DataFrame(np.random.rand(100, 2)/50 + [35.69, 139.70], columns=['lat', 'lon'])
st.map(df)

if st.checkbox('Show Image'):
    img = Image.open('sample.png')
    st.image(img, caption='sample', use_column_width=True)

option = st.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたが好きな数字は', option, 'です'

