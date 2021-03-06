"""
Using This Code Example
=========================
The code examples are provided by Yasoob Khalid to help you 
reference Practical Python Projects book. Code samples follow
PEP-0008, with exceptions made for the purposes of improving book
formatting. Example code is provided "as is".
Permissions
============
In general, you may use the code we've provided with this book in your
programs . You do not need to contact us for permission unless you're
reproducing a significant portion of the code and using it in educational
distributions. Examples:
* Writing an education program or book that uses several chunks of code from
    this course requires permission. 
* Selling or distributing a digital package from material taken from this
    book does require permission.
* Answering a question by citing this book and quoting example code does not
    require permission.
Attributions usually include the title, author, publisher and an ISBN. For
example, "Practical Python Projects, by Yasoob Khalid. Copyright 2020 Yasoob."
If you feel your use of code examples falls outside fair use of the permission
given here, please contact me at hi@yasoob.me.
"""

class MainWidget(QWidget):
    
    def __init__(self, parent):
        super(MainWidget, self).__init__(parent)
        self.threads = []
        self.initUI()
    
    # ...
    
    def setup_connections(self):
        self.browse_btn.clicked.connect(self.pick_location)
        self.download_btn.clicked.connect(self.start_download)
        
    def start_download(self):
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position,0, QTableWidgetItem(self.url_input.text()))
        self.tableWidget.setItem(row_position,1, QTableWidgetItem("0%"))
        downloader = DownloadThread(self.location_input.text(), self.url_input.text(),\ 
        row_position)
        downloader.data_downloaded.connect(self.on_data_ready)
        self.threads.append(downloader)
        downloader.start()
    def on_data_ready(self, data):
        self.tableWidget.setItem(data[2],0, QTableWidgetItem(data[0]))
        self.tableWidget.setItem(data[2],1, QTableWidgetItem(data[1]))
