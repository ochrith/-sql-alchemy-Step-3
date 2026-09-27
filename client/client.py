import requests
from Status import  Status



def upload(filename):
    response = requests.post(
        "http://127.0.0.1:5000/upload",
        files={"file": open(filename, "rb")}
    )
    return response.json().get("uid")

def status(uid):
    response = requests.get(
        f"http://127.0.0.1:5000/status/{uid}"
    )

    response.raise_for_status()

    data = response.json()

    return Status(
        status=data["status"],
        filename=data["filename"],
        timestamp=data["timestamp"],
        explanation=data["explanation"]
    )
id=upload("photosynthese_explanation.pptx",209727361)
print(status(id))
