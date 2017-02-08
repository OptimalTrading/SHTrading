import _mactowin
import win32com.client

# explore = win32com.client.Dispatch("InternetExplorer.Application")
# explore.Visible = True
# word = win32com.client.Dispatch("Word.Application")
# word.Visible = True

#step1
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1, 1).Value = "hello world"
wb.SaveAs('E:\\save\\test.xlsx')
excel.Quit()

#step2
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('E:\\save\\test.xlsx')
ws = wb.ActiveSheet
ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10
ws.Range("A2:C2").Interior.ColorIndex = 27


###!!!!!!!!!!!!! 이거 왜 안되냐!!!!!!!!