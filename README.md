# Siphon
Siphon is a simple, multi-threaded webpage downloading engine. I built Siphon to scrape as broad of a set of webpages as possible, from static site and news outlets, to social profiles and search results. Siphon can also pickup a `user_agents.txt` file to rotate the User Agents with which it requests each page, along with a randomized delay.

### How to

Siphon is super simple to use: `siphon.py urls.txt ./data_out/`

- Urls: Provide a text file containing the series of URLs you want to download
- Destination (optional): The path to the folder where you'd like to save these webpages

### Dependencies (Included in `requirements.txt`)

- arrow (0.10.0)
- requests (2.13.0)
- selenium (2.48.0)
- splinter (0.7.3)
- tldextract (2.0.2)