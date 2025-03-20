import streamlit as st
import requests
import json

state_names=["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]

state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "Virgin Islands, U.S.": "VI",
}

st.title("Weather Alert Viewer")
st.write("___")
state = st.selectbox("Select a State", state_names, placeholder="Choose a state")


alerts = requests.get("https://api.weather.gov/alerts/active?area=" + state_abbrev[state])
alert_json = alerts.json()

st.header("Weather Alerts in " + state)


a_count = 0
while a_count < len(alert_json["features"]):
    
    event = alert_json["features"][a_count]["properties"]["event"] 
    description = alert_json["features"][a_count]["properties"]["description"]
    headline = alert_json["features"][a_count]["properties"]["headline"]

    if "Freeze" in event:
        wicon = ":material/severe_cold:"
    elif "Flood" in event or "Hydrologic" in event:
        wicon = ":material/flood:"
    elif "Wind" in event:
        wicon = ":material/air:"
    elif "Winter" in event or "Frost" in event:
        wicon = ":material/ac_unit:"
    elif "Red Flag" in event or "Fire" in event:
        wicon = ":material/mode_heat:"
    elif "Current" in event:
        wicon = ":material/pool:"
    elif "Special" in event:
        wicon = ":material/warning:"
    elif "Fog" in event:
        wicon = ":material/mist:"
    elif "Cyclone" in event:
        wicon = ":material/cyclone:"
    elif "Storm" in event:
        wicon = ":material/storm:" 
    else:
        wicon = ":material/error:"
    with st.expander(event, expanded=True, icon=wicon):
        st.subheader(headline)
        st.write(description)
        a_count+=1
st.write("Powered by the [National Weather Service](https://www.weather.gov/)") 

