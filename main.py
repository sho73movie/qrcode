import streamlit as st
import qrcode
from PIL import Image

#タイトル設定
st.title('QRコード生成アプリ')

#テキストボックスにURL記載
URL = st.text_input('変換したいURLを入力')

#URLをQRコードに変換
#保存して表示させる
if st.button('QRコード生成'):
    _img = qrcode.make(URL)
    _img.save('qrcode.png')
    img = Image.open('qrcode.png')
    st.image(img)
