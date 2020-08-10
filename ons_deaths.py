import matplotlib.animation as animation
import pandas as pd
import matplotlib.pyplot as plt

# https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/weeklyprovisionalfiguresondeathsregisteredinenglandandwales

data_path = "ons_data_files/"
data_filename_2020 = (data_path + "publishedweek302020.xlsx", "Weekly figures 2020")
data_filename_2019 = (data_path + "publishedweek522019.xls", "Weekly figures 2019")
data_filename_2018 = (data_path + "publishedweek522018withupdatedrespiratoryrow.xls", "Weekly figures 2018")
data_filename_2017 = (data_path + "publishedweek522017.xls", "Weekly figures 2017")
data_filename_2016 = (data_path + "publishedweek522016.xls", "Weekly figures 2016")
data_filename_2015 = (data_path + "publishedweek2015.xls", "Weekly Figures 2015")
data_filename_2014 = (data_path + "publishedweek2014.xls", "Weekly Figures 2014")
data_filename_2013 = (data_path + "publishedweek2013.xls", "Weekly Figures 2013")
data_filename_2012 = (data_path + "publishedweek2012.xls", "Weekly Figures 2012")
data_filename_2011 = (data_path + "publishedweek2011.xls", "Weekly Figures 2011")
data_filename_2010 = (data_path + "publishedweek2010.xls", "Weekly Figures 2010")


def homog_ageranges_2020(raw_df):
    local_dataframe_2020 = pd.DataFrame(columns=raw_df.columns)

    local_dataframe_2020.loc["Under 1 year"] = raw_df.loc["<1"]
    local_dataframe_2020.loc["01-14"] = (raw_df.loc["1-4"] + raw_df.loc["5-9"] +
                                         raw_df.loc["10-14"])
    local_dataframe_2020.loc["15-44"] = (raw_df.loc["15-19"] + raw_df.loc["20-24"] +
                                         raw_df.loc["25-29"] + raw_df.loc["30-34"] +
                                         raw_df.loc["35-39"] + raw_df.loc["40-44"])
    local_dataframe_2020.loc["45-64"] = (raw_df.loc["45-49"] + raw_df.loc["50-54"] +
                                         raw_df.loc["55-59"] + raw_df.loc["60-64"])
    local_dataframe_2020.loc["65-74"] = (raw_df.loc["65-69"] + raw_df.loc["70-74"])
    local_dataframe_2020.loc["75-84"] = (raw_df.loc["75-79"] + raw_df.loc["80-84"])
    local_dataframe_2020.loc["85+"] = (raw_df.loc["85-89"] + raw_df.loc["90+"])

    print(local_dataframe_2020)
    return local_dataframe_2020


def get_data_for_year(filename, sheetname, **kwargs):
    print(filename, sheetname, kwargs)

    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name=sheetname,
                                  nrows=kwargs["num_value_rows"],
                                  skiprows=kwargs["value_skiprows"],
                                  index_col=0)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name=sheetname,
                                          nrows=1,
                                          skiprows=kwargs["col_skiprows"],
                                          index_col=0
                                          )

    df = pd.DataFrame(data=ons_deaths_df.values, columns=ons_deaths_columns_df.columns)
    df.where(pd.notnull(df), None, inplace=True)
    df.rename(columns={"Unnamed: 1": 'age_group'}, inplace=True)
    df.set_index('age_group', inplace=True)
    print(df)
    return df


def get_data_for_year_201_543210(filename, sheetname, **kwargs):
    print(filename, sheetname, kwargs)
    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name=sheetname,
                                  nrows=7,
                                  skiprows=kwargs["value_skiprows"],
                                  index_col=0)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name=sheetname,
                                          nrows=0,
                                          skiprows=kwargs["col_skiprows"],
                                          index_col=0)

    df = pd.DataFrame(data=ons_deaths_df.values, columns=ons_deaths_columns_df.columns, index=ons_deaths_df.index)
    df.where(pd.notnull(df), None, inplace=True)
    df.index.name = "age_group"
    print(df)
    return df


dataframe_2020 = homog_ageranges_2020(get_data_for_year(*data_filename_2020, num_value_rows=20, col_skiprows=5, value_skiprows=20))
dataframe_2019 = get_data_for_year(*data_filename_2019, num_value_rows=7, col_skiprows=4, value_skiprows=14)
dataframe_2018 = get_data_for_year(*data_filename_2018, num_value_rows=7, col_skiprows=4, value_skiprows=14)
dataframe_2017 = get_data_for_year(*data_filename_2017, num_value_rows=7, col_skiprows=4, value_skiprows=14)
dataframe_2016 = get_data_for_year(*data_filename_2016, num_value_rows=7, col_skiprows=4, value_skiprows=14)
dataframe_2015 = get_data_for_year_201_543210(*data_filename_2015, col_skiprows=4, value_skiprows=14)
dataframe_2014 = get_data_for_year_201_543210(*data_filename_2014, col_skiprows=3, value_skiprows=14)
dataframe_2013 = get_data_for_year_201_543210(*data_filename_2013, col_skiprows=4, value_skiprows=14)
dataframe_2012 = get_data_for_year_201_543210(*data_filename_2012, col_skiprows=4, value_skiprows=14)
dataframe_2011 = get_data_for_year_201_543210(*data_filename_2011, col_skiprows=4, value_skiprows=15)
dataframe_2010 = get_data_for_year_201_543210(*data_filename_2010, col_skiprows=4, value_skiprows=14)

frames = [dataframe_2010.T, dataframe_2011.T,
          dataframe_2012.T, dataframe_2013.T,
          dataframe_2014.T, dataframe_2015.T,
          dataframe_2016.T, dataframe_2016.T,
          dataframe_2017.T, dataframe_2018.T,
          dataframe_2019.T, dataframe_2020.T]

df_2010_2020 = pd.concat(frames)
print(df_2010_2020)
df_2010_2020.plot(xlabel="Weeks ending", ylabel="Deaths", title=f"2010 - 2020 Deaths by age group (Source: ONS)")
plt.show()
