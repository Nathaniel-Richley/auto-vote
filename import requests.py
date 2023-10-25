import requests
import threading

FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSdgSLozEfmb5gKE8d_hyxBVRiXpvuFFUXdTVlPOVuRLfDxySg/formResponse"
MULTI_CHOICE_ENTRY_ID = "entry.953604185"

def submit_vote(choice_id):
    data = {
        MULTI_CHOICE_ENTRY_ID: choice_id
    }
    while True:
        response = requests.post(FORM_URL,data=data)

        if response.status_code == 200:
            print(f'Success you voted for choice: {choice_id}')
        else:
            print(f'Failed vote for {choice_id}')
        

CHOICE_ID_FOR_YOUR_NAME = value="Richley, Nathaniel"
t1 = threading.Thread(target=submit_vote, args=(CHOICE_ID_FOR_YOUR_NAME,))
t2 = threading.Thread(target=submit_vote, args=(CHOICE_ID_FOR_YOUR_NAME,))
t3 = threading.Thread(target=submit_vote, args=(CHOICE_ID_FOR_YOUR_NAME,))
t4 = threading.Thread(target=submit_vote, args=(CHOICE_ID_FOR_YOUR_NAME,))
t5 = threading.Thread(target=submit_vote, args=(CHOICE_ID_FOR_YOUR_NAME,))
t6 = threading.Thread(target=submit_vote, args=(CHOICE_ID_FOR_YOUR_NAME,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()


