import matplotlib.animation as animation
import pandas as pd
import matplotlib.pyplot as plt

# https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/weeklyprovisionalfiguresondeathsregisteredinenglandandwales

data_path = "ons_data_files/"
data_filename_2020 = data_path + "publishedweek302020.xlsx"
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


def get_2020(filename):
    print(filename)
    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name="Weekly figures 2020",
                                  nrows=20,
                                  skiprows=20,
                                  index_col=0)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name="Weekly figures 2020",
                                          nrows=1,
                                          skiprows=5,
                                          index_col=0)

    return join_clean_df(ons_deaths_columns_df, ons_deaths_df)


def homogenise_age_ranges_2020(raw_df):
    local_dataframe_2020 = pd.DataFrame(columns=raw_df.columns)

    local_dataframe_2020.loc["Under 1 year"] = raw_df.loc["<1"]
    local_dataframe_2020.loc["01-14"] = (raw_df.loc["1-4"] +
                                   raw_df.loc["5-9"] +
                                   raw_df.loc["10-14"])
    local_dataframe_2020.loc["15-44"] = (raw_df.loc["15-19"] +
                                   raw_df.loc["20-24"] +
                                   raw_df.loc["25-29"] +
                                   raw_df.loc["30-34"] +
                                   raw_df.loc["35-39"] +
                                   raw_df.loc["40-44"])
    local_dataframe_2020.loc["45-64"] = (raw_df.loc["45-49"] +
                                   raw_df.loc["50-54"] +
                                   raw_df.loc["55-59"] +
                                   raw_df.loc["60-64"])
    local_dataframe_2020.loc["55-74"] = (raw_df.loc["55-59"] +
                                   raw_df.loc["60-64"] +
                                   raw_df.loc["65-69"] +
                                   raw_df.loc["70-74"])
    local_dataframe_2020.loc["75-84"] = (raw_df.loc["75-79"] +
                                   raw_df.loc["80-84"])
    local_dataframe_2020.loc["85+"] = (raw_df.loc["85-89"] +
                                    raw_df.loc["90+"])
    return local_dataframe_2020


def get_data_for_year(filename, sheetname):
    print(filename, sheetname)

    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name=sheetname,
                                  nrows=7,
                                  skiprows=14,
                                  index_col=0)
    # print(ons_deaths_df)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name=sheetname,
                                          nrows=1,
                                          skiprows=4,
                                          index_col=0)

    return join_clean_df(ons_deaths_columns_df, ons_deaths_df)


def get_data_for_year_201_543210(filename, sheetname, col_skiprows, value_skips=14):
    print(filename, sheetname)
    ons_deaths_df = pd.read_excel(filename,
                                  sheet_name=sheetname,
                                  nrows=7,
                                  skiprows=value_skips,
                                  index_col=0)

    ons_deaths_columns_df = pd.read_excel(filename,
                                          sheet_name=sheetname,
                                          nrows=0,
                                          skiprows=col_skiprows,
                                          index_col=0)

    df = pd.DataFrame(data=ons_deaths_df.values, columns=ons_deaths_columns_df.columns, index=ons_deaths_df.index)
    df.where(pd.notnull(df), None, inplace=True)

    df.index.name = "age_group"

    return df


def join_clean_df(df_cols, df_values):
    df = pd.DataFrame(data=df_values.values, columns=df_cols.columns)
    df.where(pd.notnull(df), None, inplace=True)
    df.rename(columns={"Unnamed: 1": 'age_group'}, inplace=True)
    df.set_index('age_group', inplace=True)
    # print(df)
    return df


# raw_dataframe_2020 = get_2020(data_filename_2020)
# # print(raw_dataframe_2020)
#
dataframe_2020 = homogenise_age_ranges_2020(get_2020(data_filename_2020))
# # print(dataframe_2020)
# # # data_file_name_2020.T.plot(xlabel="Weeks ending", ylabel="Deaths", title='2020, Deaths by age group (Source: ONS)')
# # # plt.show()
#
dataframe_2019 = get_data_for_year(*data_filename_2019)
# # print(data_filename_2019)
# # # data_file_name_2019.T.plot(xlabel="Weeks ending", ylabel="Deaths", title='2019, Deaths by age group (Source: ONS)')
# # # plt.show()
#
dataframe_2018 = get_data_for_year(*data_filename_2018)
# # print(data_filename_2018)
#
#
dataframe_2017 = get_data_for_year(*data_filename_2017)
# # print(data_filename_2017)
#
dataframe_2016 = get_data_for_year(*data_filename_2016)
print(dataframe_2016)


dataframe_2015 = get_data_for_year_201_543210(*data_filename_2015, 4, 14)
# print(dataframe_2015)
# print(data_filename_2015)
# dataframe_2015.T.plot(xlabel="Weeks ending", ylabel="Deaths", title=f"{data_filename_2015[1]}, Deaths by age group (Source: ONS)")
# plt.show()
#
dataframe_2014 = get_data_for_year_201_543210(*data_filename_2014, 3, 14 )
# print(dataframe_2014)

dataframe_2013 = get_data_for_year_201_543210(*data_filename_2013, 4, 14)
# print(dataframe_2013)

dataframe_2012 = get_data_for_year_201_543210(*data_filename_2012, 4, 14)
# print(dataframe_2012)

dataframe_2011 = get_data_for_year_201_543210(*data_filename_2011, 4, 15)
print(dataframe_2011)

dataframe_2010 = get_data_for_year_201_543210(*data_filename_2010, 4, 14)
print(dataframe_2010)

frames = [dataframe_2010.T,
          dataframe_2011.T,
          dataframe_2012.T,
          dataframe_2013.T,
          dataframe_2014.T,
          dataframe_2015.T,
          dataframe_2016.T,
          dataframe_2016.T,
          dataframe_2017.T,
          dataframe_2018.T,
          dataframe_2019.T,
          dataframe_2020.T]

df_2010_2020 = pd.concat(frames)

df_2010_2020.plot(xlabel="Weeks ending", ylabel="Deaths", title=f"2010 - 2020 Deaths by age group (Source: ONS)")
plt.show()
