Parser of 10 words in technology news trends. The parser collects all headlines from the front pages of the world's news sites in the "Technology" section, from which it selects 10 frequently mentioned words with the number of mentions in descending order and under each word prints 5 recent news stories from 'news.google.com/search'

to start it up, you need:  
git clone https://github.com/kali256/top_10_technological_news.git  
cd top_10_technological_news   
sudo apt install python3.11-venv  
python3 -m venv venv  
source venv/bin/activate  
pip3 install -r requirements.txt  
python3 main.py  

updating the repository:  
git remote -v update  
git pull  
