# valorwin-model

## Brief Summary

A model to estimate the probability of your round and match win chance using classification methods.

## Where we get our data

Our data will be scraped from https://www.vlr.gg/
We have been given permission to scrape their website accordingly.

## Features

```
Eco: 0-5k $ Semi-eco: 5-10k $$ Semi-buy: 10-20k $$$ Full buy: 20k+
```

- Loadout Credits of Entire Team (Eco, Semi-eco, semi-buy, full buy)
- Map
- Current Score (Rounds vs Enemy)
- Match Outcome
- Round Outcome

## Things To Do

- Get Data Set for Training and Validation (Aiming for 10,000 games minimum)
- Preprocess the data
- Decide between Decision Trees, Random forests, SVMs, Neural Networks
- Implement the chosen AI model

## Progress/Notes

- Finishing up scraper for the site VLR.gg

## Built With

- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Python-DotEnv](https://pypi.org/project/python-dotenv/)
- [PyMongo](https://pypi.org/project/pymongo/)

## Contributing

Feel free to submit a [pull request](https://github.com/josephsookim/valorwin-model/pull/new/master) or an [issue](https://github.com/josephsookim/valorwin-model/issues/new)!

## License

The MIT License (MIT)
