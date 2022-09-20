# learn more about dashboarding tools from: https:// pyviz.org/dashboarding/
# learn more about making dashboards with plotly: https://plotly.com/python/getting-started/

def intro2plotly():
    import piplite
    await piplite.install(['nbformat', 'plotly'])
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go

    # Read the airline data into pandas dataframe
    from js import fetch
    import io

    URL = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv'
    resp = await fetch(URL)
    text = io.BytesIO((await resp.arrayBuffer()).to_py())

    airline_data = pd.read_csv(text,
                               encoding="ISO-8859-1",
                               dtype={'Div1Airport': str, 'Div1TailNum': str,
                                      'Div2Airport': str, 'Div2TailNum': str})

    # Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
    data = airline_data.sample(n=500, random_state=42)

    # show how departure time changes with respect to airport distance with a scatter plot
    # First we create a figure using go.Figure and adding trace to it through go.scatter
    fig = go.Figure(data=go.Scatter(x=data['Distance'], y=data['DepTime'], mode='markers', marker=dict(color='red')))

    # Updating layout through `update_layout`. Here we are adding title to the plot and providing title to x and y axis.
    fig.update_layout(title='Distance vs Departure Time', xaxis_title='Distance', yaxis_title='DepTime')

    # Display the figure
    fig.show()

    # line plot of avg monthly arrival time change over the year
    # Group the data by Month and compute average over arrival delay time.
    line_data = data.groupby('Month')['ArrDelay'].mean().reset_index()

    # Create line plot here
    fig2 = go.Figure(
    data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'], mode='lines', marker=dict(color='green')))
    fig2.update_layout(title='Avg Delay per Month', xaxis_title='Month', yaxis_title='Avg Delay')
    fig2.show()

    # Bar chart
    # Group the data by destination state and reporting airline. Compute total number of flights in each combination
    bar_data = data.groupby(['DestState'])['Flights'].sum().reset_index()

    # Use plotly express bar chart function px.bar. Provide input data, x and y axis variable, and title of the chart.
    # This will give total number of flights to the destination state.
    fig = px.bar(bar_data, x="DestState", y="Flights",
                 title='Total number of flights to the destination state split by reporting airline')
    fig.show()

    # Bubble Chart
    # Group the data by reporting airline and get number of flights
    bub_data = data.groupby('Reporting_Airline')['Flights'].sum().reset_index()

    # Create bubble chart here
    fig = px.scatter(bub_data, x="Reporting_Airline", y="Flights", size="Flights",
                     hover_name="Reporting_Airline", title='Reporting Airline vs Number of Flights', size_max=60)
    fig.show()