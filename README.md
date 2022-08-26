# KGene

KG generation from webcrawled natural language!

![](img/cover.png)

### Usage
```bash
# Clone, install dependencies
git clone https://github.com/julian-q/kgene.git
cd kgene
conda env create -f kg_env.py
conda activate kg
brew install node
npm install http-server -g

# Crawl the desired webpage
scrapy runspider spider.py -a start_urls=['https://www.deepmind.com/blog'] -o webcrawling/notes.jl

# Extract and save entities
python ner.py

# Launch graph view (this might take a moment to load)
http-server
```
You should then be able to view the app at `http://127.0.0.1:8080`.
