import requests
import json
 
url = "http://10.29.168.132:4440/api/50/webhook/70fR82oCqmlIJEZDL6w2Q0HIHzYKg1BL#SAP_Access_Removal_Handler"
 
payload = json.dumps({
  "result": {
    "rd_exec_id": 24803,
    "rd_job_status": "DONE",
    "ticket_state": "Closed Complete",
    "ticket_work_notes": "This is just for testing"
  }
})
headers = {
  'Authorization': '5a9GHIQM00Rk7M4jc22NphKQesKFp3BH',
  'Content-Type': 'application/json'
}
 
response = requests.request("POST", url, headers=headers, data=payload)
 
print(response.text)