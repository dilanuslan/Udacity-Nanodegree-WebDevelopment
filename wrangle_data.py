import pandas as pd
import plotly.graph_objs as go

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`
import pandas as pd
import plotly.graph_objs as go


def cleandata():
    data = pd.read_csv("/home/data/survey-results-public.csv")
    # Keep only the columns of interest (years and country name)
    
    data = data[['Country', 'Salary', 'FormalEducation', 'MajorUndergrad', 'Professional']]

    return data

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # first chart plots arable land from 1990 to 2015 in top 10 economies 
  # as a line chart
    #df = pd.read_csv("/home/data/survey-results-public.csv")
    df = cleandata()    
    graph_one = []
    #df.columns = ['Country','Year','hectaresarablelandperperso'Country','Year',
    top10country = ['United States', 'Poland', 'Australia', 'Germany', 'United Kingdom', 'India', 'France', 'Russia', 'Spain', 'Canada']
    df = df[df['Country'].isin(top10country)]    
    df = df.dropna(subset=['Salary'], axis=0)
    df = df.groupby(['Country'], as_index=False)['Salary'].mean()
    df.sort_values('Salary', ascending=False, inplace=True)
    countrylist = df.Country.unique().tolist()
    
    for country in countrylist:
      x_val = df[df['Country'] == country].Country.tolist()
      y_val =  df[df['Country'] == country].Salary.tolist()
      graph_one.append(
          go.Bar(
          x = x_val,
          y = y_val,
          name = country,
          #mode = 'lines'
          )
      )

    layout_one = dict(title = 'Average Salary for Top 10 Countries',
                xaxis = dict(title = 'Country',
                  autotick=False),
                yaxis = dict(title = 'Salary'),
                )
    
    df3 = cleandata()
    graph_two = []
    df3 = df3.groupby(['MajorUndergrad'], as_index=False)['Salary'].mean()
    print(df3)
    df3.sort_values('Salary', ascending=False, inplace=True)
    mun = df3.MajorUndergrad.unique().tolist()
    
    for m in mun:
      x_val = df3[df3['MajorUndergrad'] == m].MajorUndergrad.tolist()
      y_val =  df3[df3['MajorUndergrad'] == m].Salary.tolist()
      graph_two.append(
          go.Bar(
          x = x_val,
          y = y_val,
          name = m,
          #mode = 'lines'
          )
      )

    layout_two = dict(title = 'Average Salary for Undergrad Major',
                xaxis = dict(title = 'Undergrad Major',
                  autotick=False, showticklabels=False),
                yaxis = dict(title = 'Salary'),
                )
    
    df2 = cleandata() 
    
    graph_three = []
    df2 = df2.groupby(['FormalEducation'], as_index=False)['Salary'].mean()
    df2.sort_values('Salary', ascending=False, inplace=True)
    fed = df2.FormalEducation.unique().tolist()
    
    for ed in fed:
      x_val = df2[df2['FormalEducation'] == ed].FormalEducation.tolist()
      y_val =  df2[df2['FormalEducation'] == ed].Salary.tolist()
      graph_three.append(
          go.Bar(
          x = x_val,
          y = y_val,
          name = ed,
          #mode = 'lines'
          )
      )

    layout_three = dict(title = 'Average Salary for Formal Education Status',
                xaxis = dict(title = 'Formal Education',
                  autotick=False, showticklabels=False),
                yaxis = dict(title = 'Salary'),
                )
    '''   
    df4 = cleandata() 
    
    graph_four = []
    df4 = df4.groupby(['Professional'], as_index=False)['Salary'].mean()
    df4.sort_values('Salary', ascending=False, inplace=True)
    profs = df4.Professional.unique().tolist()
    
    for p in profs:
      x_val = df4[df4['Professional'] == p].Professional.tolist()
      y_val =  df4[df4['Professional'] == p].Salary.tolist()
      graph_four.append(
          go.Bar(
          x = x_val,
          y = y_val,
          name = p,
          #mode = 'lines'
          )
      )

    layout_four = dict(title = 'Average Salary for Profession',
                xaxis = dict(title = 'Profession',
                  autotick=False),
                yaxis = dict(title = 'Salary'),
                )
    '''   
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    #figures.append(dict(data=graph_four, layout=layout_four))

    return figures

