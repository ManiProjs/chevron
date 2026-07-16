from chevron import Confirm

if Confirm("Delete everything?").ask():
    print("Deleted!")
else:
    print("Cancelled.")
