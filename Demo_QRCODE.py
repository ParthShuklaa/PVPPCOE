import qrcode
import pyqrcode

Name = "parth Shukla "
Mobile_No = "9599587014"
Linked_ID ="www.linkedin.com/in/parth-shukla-09205239 "
github = "https://github.com/ParthShuklaa"
Website_link ="http://shuklaparth.com/"

MYQRCODE = pyqrcode.create(Name+Mobile_No+Linked_ID+github+Website_link)
MYQRCODE.svg("QRcode.svg")
