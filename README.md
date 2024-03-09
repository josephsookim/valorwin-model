# valorwin-model

## Brief Summary

An AI model utilizing random forest classification to assess the likelihood of winning individual rounds and entire matches in Valorant.

Download link for .pkl and .csv files:
https://drive.google.com/drive/folders/1rjTZpR41E4Q9DpxqqX8VDf53y9XsvwgK?usp=sharing

## Data

- Our data will be scraped from https://www.vlr.gg/
- We have been given permission to scrape their website.
- This dataset has been created with data from over 10,000 bo3 and bo5 matches from the T1, T2, and collegiate scene.
- There are almost 500,000 rounds of data that cover every map on Valorant.

## Input Variables

- Team Loadout
- Enemy Loadout
- Team Rounds Won
- Enemy Rounds Won
- Map

### Notes

- Eco: 0-5k
- Semi Eco: 5-10k
- Semi Buy: 10-20k
- Full Buy: 20k+

## Output Variable

- Match Outcome
  or
- Round Outcome

## Built With

- [Requests](https://requests.readthedocs.io/en/master/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [Python-DotEnv](https://pypi.org/project/python-dotenv/)
- [PyMongo](https://pypi.org/project/pymongo/)
- [scikit-learn](https://scikit-learn.org/stable/install.html)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

## Contributing

Feel free to submit a [pull request](https://github.com/josephsookim/valorwin-model/pull/new/master) or an [issue](https://github.com/josephsookim/valorwin-model/issues/new)!

## License

The MIT License (MIT)
