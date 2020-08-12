# ons_deaths_data

A data processing Python Notebook for [Office of National Statistics Deaths](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/weeklyprovisionalfiguresondeathsregisteredinenglandandwales) data.

This data covers England and Wales.

The code extracts the relevant data from the spreadsheets that have been downloaded from the above ONS site. For the year 2020 we homogenise the age groups to match that used in the previous years.

The data is collated into one large dataframe and I create a sum column for all age ranges.
(This may differ from the official published deaths as some deaths may be missing from the agre group data if the age was not known etc.) More details are in the colab notebook.

![Graph of Deaths 2010-2020](ONS_2010_2020_deaths_by_age.png)

To view the notebook [open in Google Colab](https://colab.research.google.com/github/phoughton/ons_deaths_data/blob/master/ONS_deaths_England_wales_2010_thru_2020.ipynb). (There is aslso a link in the notebook itself, at the top.)
