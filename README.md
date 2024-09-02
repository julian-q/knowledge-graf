# knowledge-graf

Knowledge graph generation from webcrawled natural language!

![](img/cover.png)

### Usage
```bash
# Clone, install dependencies
git clone https://github.com/julian-q/kgene.git
cd kgene
pip install -r requirements.txt
npm install http-server -g

# Crawl the desired webpage (hope this works)
scrapy crawl notes -a start_url=https://acquired.fm/episodes -a allowed_domain=acquired.fm -O webcrawling/notes.jl

# Extract and save entities
python ner.py

# (Optional) Remove nodes that contain common keywords (passed as args)
python remove_nodes.py ben david marvel

# Launch graph view (this might take a moment to load)
http-server
```
