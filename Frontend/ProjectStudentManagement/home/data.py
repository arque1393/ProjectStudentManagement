from PySide6.QtNetwork import QHttpMultiPart, QHttpPart
from PySide6.QtCore import QFile, QUrl

multiPart = QHttpMultiPart(QHttpMultiPart.FormDataType)
textPart = QHttpPart()
textPart.setHeader(QNetworkRequest.ContentDispositionHeader,
                   QVariant("form-data; name=\"text\""))
textPart.setBody("my text")
imagePart = QHttpPart()
imagePart.setHeader(QNetworkRequest.ContentTypeHeader, QVariant("image/jpeg"))
imagePart.setHeader(QNetworkRequest.ContentDispositionHeader,
                    QVariant("form-data; name=\"image\""))
file = QFile("image.jpg")
file.open(QIODevice.ReadOnly)
imagePart.setBodyDevice(file)
# we cannot delete the file now, so delete it with the multiPart
file.setParent(multiPart)
multiPart.append(textPart)
multiPart.append(imagePart)
url = QUrl("http://my.server.tld")
request = QNetworkRequest(url)
manager = QNetworkAccessManager()
reply = manager.post(request, multiPart)
multiPart.setParent(reply)  # delete the multiPart with the reply
# here connect signals etc.
