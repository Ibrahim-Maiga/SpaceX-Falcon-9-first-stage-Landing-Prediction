# Install python packages required to run the application
pip3 install pandas dash

# Download the SpaceX Launch dataset as spacex_launch_dash.csv
wget "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv"

# Observe the port number shown in the terminal and Launch Application 
python3 spacex_dash_app.py
