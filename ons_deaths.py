import matplotlib.animation as animation
import pandas as pd
import matplotlib.pyplot as plt

# https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/weeklyprovisionalfiguresondeathsregisteredinenglandandwales

data_filename_2020 = "publishedweek302020.xlsx"
data_filename_2019 = "publishedweek522019.xls"


def get_2020(filename):
    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name="Weekly figures 2020",
                                  nrows=20,
                                  skiprows=20,
                                  index_col=2)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name="Weekly figures 2020",
                                          nrows=1,
                                          skiprows=5,
                                          index_col=2)

    return join_clean_df(ons_deaths_columns_df, ons_deaths_df)


def get_2019(filename):
    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name="Weekly figures 2019",
                                  nrows=7,
                                  skiprows=14,
                                  index_col=2)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name="Weekly figures 2019",
                                          nrows=1,
                                          skiprows=4,
                                          index_col=2)

    return join_clean_df(ons_deaths_columns_df, ons_deaths_df)


def join_clean_df(df_cols, df_values):
    df = pd.DataFrame(data=df_values.values, columns=df_cols.columns)
    df.where(pd.notnull(df), None, inplace=True)
    df.drop(labels="Week ended", axis=1, inplace=True)
    df.rename(columns={"Unnamed: 1": 'age_group'}, inplace=True)
    df.set_index('age_group', inplace=True)
    print(df)
    return df


raw_dataframe_2020 = get_2020(data_filename_2020)
# data_file_name_2020.T.plot(xlabel="Weeks ending", ylabel="Deaths", title='2020, Deaths by age group (Source: ONS)')
# plt.show()
dataframe_2019 = get_2019(data_filename_2019)
# data_file_name_2019.T.plot(xlabel="Weeks ending", ylabel="Deaths", title='2019, Deaths by age group (Source: ONS)')
# plt.show()

dataframe_2020 = pd.DataFrame(columns=raw_dataframe_2020.columns)

dataframe_2020.loc["Under 1 year"] = raw_dataframe_2020.loc["<1"]
dataframe_2020.loc["01-14"] = (raw_dataframe_2020.loc["1-4"] +
                               raw_dataframe_2020.loc["5-9"] +
                               raw_dataframe_2020.loc["10-14"])
dataframe_2020.loc["15-44"] = (raw_dataframe_2020.loc["15-19"] +
                               raw_dataframe_2020.loc["20-24"] +
                               raw_dataframe_2020.loc["25-29"] +
                               raw_dataframe_2020.loc["30-34"] +
                               raw_dataframe_2020.loc["35-39"] +
                               raw_dataframe_2020.loc["40-44"])
dataframe_2020.loc["45-64"] = (raw_dataframe_2020.loc["45-49"] +
                               raw_dataframe_2020.loc["50-54"] +
                               raw_dataframe_2020.loc["55-59"] +
                               raw_dataframe_2020.loc["60-64"])
dataframe_2020.loc["55-74"] = (raw_dataframe_2020.loc["55-59"] +
                               raw_dataframe_2020.loc["60-64"] +
                               raw_dataframe_2020.loc["65-69"] +
                               raw_dataframe_2020.loc["70-74"])
dataframe_2020.loc["75-84"] = (raw_dataframe_2020.loc["75-79"] +
                               raw_dataframe_2020.loc["80-84"])
dataframe_2020.loc["85+"] = (raw_dataframe_2020.loc["85-89"] +
                             raw_dataframe_2020.loc["90+"])
print(dataframe_2020)
dataframe_2020.T.plot(xlabel="Weeks ending", ylabel="Deaths", title='2020, Deaths by age group (Source: ONS)')
plt.show()
