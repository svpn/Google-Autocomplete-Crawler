# Google Suggest Crawler

Google Suggest Crawler contains a script to automatically mine suggestions off Google Suggest. This repo contains a main script to crawl data off Google Suggest. It takes in a list of keywords (which I will call Seed-words) and then generate approx 200+ suggestions by appending prefixes and suffixes to the original seed-word.

Note that everything breaks the moment google changes their endpoint. 

### Usage


#### Suggest.py

Crawling your own data

```
git clone https://github.com/ytay2/GoogleSuggestCrawler.git
cd GoogleSuggestCrawler
```

Note:Python 3 and above is required to run GSC.
A python 3.4 virtual environment is provided in this repo.
```
source env/bin/activate
```

Script takes an input CSV file, specify the file name
Script outputs a txt file of crawled suggested queries

To run script from shell:

```
python suggest.py -i input.csv -o output.txt
```
example.csv provides an example of how to structure your "seedwords"

this script saves all your crawled data into a file called persistSeeds.txt. Think of it like a persistent storage for all the keywords you have crawled. This is useful if you experience a
disconnect in the midst of running this script. 

Optionally you may run,
```
python suggest.py -i input.csv -o output.txt -d
```
This will disable persistent storage if you're running test and do not want to save your crawling logs.

Running the script without arguments will take seedwords from example.csv and write it to a new file "results.txt". If you do not specify output arguments, it will make a new file called results.txt

Note the currently supported file formats are only CSV for input (it uses a CSV parser) and a txt file for output. (I think you may output to CSV too if you like but I have not tested it).

#### Cutter.py

You might want to use the cutter to slice up a long txt file after crawling. 

For example, google adwords only allows max of 3000 per input file. 

Run
```
python cutter.py -i example.txt -n 3000

```
Where n is the segmented file size and i is the input file. If no input file is specified, result.txt is used by default.
if the file is empty or too small, the script will not run.

Make sure the file is in the same directory as cutter.py before running. 

All sliced files are then created in the cut-files directory


### Explanation of other files and utilities
1. UtlityScript folder contains several scripts I use for cleaning data. They are not packaged for easy usage just yet. It is on the to-do list for now. It is also very customised to one specific use-case. You may need to hack around a little to use it for what you need. Not all these scripts have their dependencies installed in the virtual env. They might be in the future. 
2. Do not look into deprecated. They are lots of junk in there. You should not find anything useful
3. ProcessedData are crawled CSVs files that have already been successfully crawled.
4. Deliverables contain crawled data. 

### Version
0.0.2

