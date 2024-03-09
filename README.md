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

### Example Data
![image](https://github.com/josephsookim/valorwin-model/assets/13972507/9a23b71f-af5c-4b57-ad18-76baf0ed05a0)


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

## Classification Report
![image](https://github.com/josephsookim/valorwin-model/assets/13972507/fd38daef-d956-48ed-bd4d-69fca61c9a39)

## How To Use
### 1. Import dependencies and load model
![image](https://github.com/josephsookim/valorwin-model/assets/13972507/a3af80c9-f3cc-4b03-bc41-14c1374b0239)

### 2. Input Data [Must be in this order!]
![image](https://github.com/josephsookim/valorwin-model/assets/13972507/1a60505f-257e-4b64-8596-f52f939ae285)

### 3. Predict probabilities
![image](https://github.com/josephsookim/valorwin-model/assets/13972507/65524bd0-e4c8-46df-8f9b-45d1c3db877e)

### 4. Output results
![image](https://github.com/josephsookim/valorwin-model/assets/13972507/23f196e6-653f-40b9-a223-7cdd1a7c87b3)




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
