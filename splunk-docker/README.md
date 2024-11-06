# Splunk server and test scripy using docker

- This repo contains a docker compose file to setup a splunk server and a script sends events to the Splunk HTTP Event Collector (HEC) endpoint.<br />
<br />
For docker-compose.yml file:<br />
1- Replace YourSecurePassword with a strong admin password.<br />
2- Set your_hec_token to the HEC token you’ll use for authentication.<br />
3- You may want to adjust volume paths or add additional configurations if needed.<br />
<br />
For python Script to Send Test Events (send_event.py):<br />
Instructions to Run:<br />
1- Replace splunk_hec_url with the URL to your Splunk HEC if not on localhost.<br />
2- Replace splunk_token with the token you set in the Docker Compose file.<br />
3- Run the script with: python3 send_event.py<br />
4- You should receive confirmation that the data was sent, and you can search for it in Splunk with: index=main "This is a test event from a service"<br />
<br />
Access Splunk UI:<br />
Open http://localhost:8000 in your browser.<br />
Log in with admin and the password you set (YourSecurePassword).<br />
Ensure the HTTP Event Collector (HEC) is enabled and configured.<br />
<br />
- If you’re running into issues with SSL, set verify=False in the Python script to skip SSL verification (especially if using localhost).
You may need to adjust the time range in Splunk to view recent data.