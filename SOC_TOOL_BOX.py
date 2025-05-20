import tkinter as tk
from tkinter import *
import subprocess
import sys

window = Tk()
window.title("SOC Toolbox")
window_width = 500
window_height = 300
window.geometry(f"{window_width}x{window_height}")
# Horizontally center, vertically near the top
window.update_idletasks()
screen_width = window.winfo_screenwidth()
x = (screen_width // 2) - (window_width // 2)
y = 150  # Distance from the top of the screen (adjust as needed)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")
# Set the background color of the window to light blue
window.config(bg="#ef5a68")
# Replace this with the full path to Chrome if needed
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"


# Function to launch the selected website(s) in new browser windows
def open_in_new_window(urls, is_new_window=False):
    # If is_new_window is True, open the first URL in a new window, subsequent URLs in tabs
    if is_new_window:
        subprocess.Popen([chrome_path, '--new-window'] + urls)  # Open all URLs in a new window
    else:
        # Open all URLs for the same website in a single new window with tabs
        subprocess.Popen([chrome_path, '--new-window'] + urls)  # Open the first URL in a new window


def SOC_ToolBox():
    selected_website = website_var.get()
    if selected_website == "SLBOS Cycle J and Cycle A":
        # Set of URLs for SLBOS Cycle J and Cycle A, all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20J&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20J&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CIM&productFamily=Customer&hostGroup=Cycle%20J%20-%20Charter&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=AcpGateway&productFamily=Gateways&hostGroup=Cycle%20J&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20A&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20A&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CIM&productFamily=Customer&hostGroup=Cycle%20A%20-%20Global&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=AcpGateway&productFamily=Gateways&hostGroup=Cycle%20A&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20A&transaction=SendCardPayment&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20A&transaction=CreateRecurringEFTPayment&timeBucket=00:05:00",
            "https://zabbix.csgiprod.com/zabbix/zabbix.php?action=dashboard.view&dashboardid=31",
            "https://accprdislpu0001.csgiprod.com/SLBSInject/JetDashboardCVP.aspx",
            "https://accprdislpu0001.csgiprod.com/SLBSInject/DashboardCVP.aspx",
            "https://confluence.csgicorp.com/pages/viewpage.action?spaceKey=SLBOS&title=SLBOS+Team+Calendar"
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)
    elif selected_website == "SLBOS Others":
        # Set of URLs for SLBOS Others, all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway&productFamily=SLBOS%20CSG&hostGroup=Comcast&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Comcast&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CIM&productFamily=Customer&hostGroup=Cycle%20B%20-%20Comcast&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=AcpGateway&productFamily=Gateways&hostGroup=Comcast&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway&productFamily=SLBOS%20CSG&hostGroup=Dish&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Dish&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CIM&productFamily=Customer&hostGroup=Cycle%20D%20-%20Dish&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=AcpGateway&productFamily=Gateways&hostGroup=Dish&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=FleetGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=ForteRealtimeGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=AuthGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CcsCyberRealtimeGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=TermServGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SchedulingGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CapGateway&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=Ccs-Customer&productFamily=CCS&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=Ccs-ExtendedField&productFamily=CCS&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CcsServer&productFamily=CCS&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=Memo&productFamily=CCS&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00",
            "https://confluence.csgicorp.com/pages/viewpage.action?spaceKey=SLBOS&title=SLBOS+Team+Calendar"
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)



    elif selected_website == "Voice and CCS":
        # Set of URLs for Voice and CCS, all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=VoiceSDS&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=chrtrvp%7Ctwcvp&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=VoiceSrv&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CHRTRVP%7CTWCVP&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=PDBServices&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CHT%7CPTW&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=PDBServices_SLB&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CHT%7CPTW&timeBucket=00:05:00",
            "https://cvp.csgicorp.com/view/SOG-PDBServices/",
            "https://zabbix.csgiprod.com/zabbix/zabbix.php?action=dashboard.view&dashboardid=15",
            "https://zabbix.csgiprod.com/zabbix/zabbix.php?action=dashboard.view&dashboardid=68",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=VoiceSDS&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CMCVP&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=VoiceSrv&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CMCVP&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=PDBServices&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CST&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=PDBServices_SLB&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CST&timeBucket=00:05:00",
            "https://cvp.csgicorp.com/view/CVP-3270/",
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)
    elif selected_website == "ACSR and ACPx":
        # Set of URLs for ACSR, ACPx all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CharterOrderService&productFamily=ORM&hostGroup=%5BAll%20Host%20Groups%5D&transaction=CharterOrderSubmitOperation.SubmitOrder&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=Configuration&productFamily=ACPx&hostGroup=Charter&transaction=ISecurityRuntimeCreateFederatedSession&timeBucket=00:05:00",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=OfferManagement&productFamily=ACPx&hostGroup=Charter&transaction=IProductOfferServiceRetrieveQualifyingProductOfferList&timeBucket=00:05:00",
            "https://stathub.csgedirect.com:5601/goto/79ccd728d8e290229b35fa79f71dd2d3",
            "https://stathub.csgedirect.com:5601/goto/88647920aa6baf42594f16752d3b996b",
            "https://stathub.csgedirect.com:5601/goto/aad316d043bb4b16996b91b66922bdb3",
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)
    elif selected_website == "FSM":
        # Set of URLs for Facebook, all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=WFXAPI&productFamily=Workforce&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=TECHNET&productFamily=Workforce&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=JRA&productFamily=Workforce&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=Scheduling&productFamily=Gateways&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:05:00&pagingDisabled=false",
            "https://2210cef755c34e0db1f17e7fe1ab3b0c.us-east-1.aws.found.io:9243/app/r/s/vvqm1",
            "https://2210cef755c34e0db1f17e7fe1ab3b0c.us-east-1.aws.found.io:9243/app/r/s/NVtlb",
            "https://accprdislws0001.csgiprod.com:8124/iwc/main.iwc?action=1&sortBy=DB&sortOrder=ASC&pm=P&filter=wfxcmc",
            "https://accprdislws0001.csgiprod.com:8124/iwc/main.iwc?action=1&sortBy=DB&sortOrder=ASC&pm=P&filter=chr",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/altice-prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/chrt-prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/com-prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/moms-prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/nasbu-prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/teco-prod/",
            "https://cvp-prod.csgicorp.com/view/FSM-CVP-Prod/job/FSM_CVP_PROD_UI_VALIDATION_SEQUENTIAL_CLIENT_SPECIFIC/",
            "https://wfxapsls20.co.csgsystems.com:3000/dashboard",
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)
    elif selected_website == "System Health Check":
        # Set of URLs for System Health Check all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/home?product=CharterOrderService&productFamily=ORM&hostGroup=%5BAll%20Host%20Groups%5D",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=CharterOrderService&productFamily=ORM&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=CharterOrderService&productFamily=ORM&hostGroup=%5BAll%20Host%20Groups%5D&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/home?product=OfferManagement&productFamily=ACPx&hostGroup=Charter",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=OfferManagement&productFamily=ACPx&hostGroup=Charter&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=OfferManagement&productFamily=ACPx&hostGroup=Charter&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/home?product=SlbosBosGateway%7CSlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20J",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=SlbosBosGateway%7CSlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20J&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=SlbosBosGateway%7CSlbosEniGateway&productFamily=SLBOS%20CSG&hostGroup=Cycle%20J&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/home?product=EniPoller&productFamily=Enterprise%20Interfaces&hostGroup=EniPoller%20-%20Charter",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/home?product=EniPoller&productFamily=Enterprise%20Interfaces&hostGroup=CapPoller%20-%20Charter&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=EniPoller&productFamily=Enterprise%20Interfaces&hostGroup=EniPoller%20-%20Charter&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=EniPoller&productFamily=Enterprise%20Interfaces&hostGroup=CapPoller%20-%20Charter&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=EniPoller&productFamily=Enterprise%20Interfaces&hostGroup=EniPoller%20-%20Charter&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=EniPoller&productFamily=Enterprise%20Interfaces&hostGroup=CapPoller%20-%20Charter&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/home?product=AcpGateway&productFamily=Gateways&hostGroup=Cycle%20J",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=AcpGateway&productFamily=Gateways&hostGroup=Cycle%20J&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=AcpGateway&productFamily=Gateways&hostGroup=Cycle%20J&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=ACSR&productFamily=ACP&hostGroup=ACSR&client=Charter&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=ACSR&productFamily=ACP&hostGroup=ACSR&client=Charter&axisType=fixed&timeBucket=auto",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/throughput?product=PDBServices_SLB&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CHT%7CPTW%7CCHH&timeBucket=00:15:00&pagingDisabled=false",
            "https://stathub.csgedirect.com/StatHubUI_prod/#/activity/range?product=PDBServices_SLB&productFamily=Provisioning&hostGroup=%5BAll%20Host%20Groups%5D&client=CHT%7CCHH%7CPTW&axisType=fixed&timeBucket=auto",
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)
    elif selected_website == "CCS Code Location":
        # Set of URLs for ACSR, ACPx all open in the same window (in tabs)
        urls = [
            "https://stathub.csgedirect.com/StatHubUI_prod/#/log/codeLocation?product=CCSErrors%7CCCS-QUE&productFamily=CCS&hostGroup=%5BAll%20Host%20Groups%5D&timeBucket=auto&pagingDisabled=false",
        ]
        open_in_new_window(urls, is_new_window=False)  # Open in the same window (tabs)
    else:
        # Handle case for invalid selection or no selection made
        print("Please select a valid website from the dropdown.")


# Options for website selection
options = [
    "Please select from the drop down",
    "SLBOS Others",
    "SLBOS Cycle J and Cycle A",
    "ACSR and ACPx",
    "Voice and CCS",
    "FSM",
    "System Health Check",
    "CCS Code Location"
]
website_var = StringVar()
website_var.set(options[0])
# Dropdown menu for selecting a website
drop = OptionMenu(window, website_var, *options)
drop.config(bg="aliceblue", width=50, height=2)
drop.pack(pady=20)
# Button to launch the selected website(s) in a new browser window
# linkbutton = Button(window, text="Launch", command=SOC_ToolBox, bg="aliceblue")
linkbutton = Button(window, text="Launch", command=SOC_ToolBox, bg="aliceblue", width=15, height=2)
linkbutton.pack()
# Run the main window
window.mainloop()
