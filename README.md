# lctranslate
LangChain Translate App

LangChain を使って翻訳アプリを作成します。


## setup

```
python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
pip install langchain==0.3.2
pip install langchain-openai==0.2.2
pip install langchain-google-genai=2.0.0
pip install streamlit==1.35.0
```

### Google API キーを取得

- https://aistudio.google.com/app/apikey

取得したAPIキーをファイルに保存

```
mkdir ~/.googleai
vi ~/.googleai/gapikey20241007
```

環境変数を設定

```
export GOOGLE_API_KEY=`cat ~/.googleai/gapikey20241007`
```


### openai API キーを取得

- https://openai.com/api

取得したAPIキーをファイルに保存

```
mkdir ~/.openai
vi ~/.penai/apikey20241007
```

環境変数を設定

```
export OPENAI_API_KEY=`cat ~/.openai/apikey20241007`
```

## アプリの起動方法

```
streamlit run main.py
```