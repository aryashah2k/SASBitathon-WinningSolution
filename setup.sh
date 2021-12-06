mkdir -p ~/.streamlit/
echo "[general]
email = \"aryashah.0616@gmail.com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml