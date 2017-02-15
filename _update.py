import _secret as sec
from pywinauto import application, timings
import time
import os

app = application.Application()
app.start("C:/Kiwoom/KiwoomFlash2/khministarter.exe")
dlg = timings.WaitUntilPasses(20, 0.5, lambda: app.window_(title="번개 Login"))
pass_ctrl = dlg.Edit2
pass_ctrl.SetFocus()
pass_ctrl.TypeKeys(sec.pswd)
cert_ctrl = dlg.Edit3
cert_ctrl.SetFocus()
cert_ctrl.TypeKeys(sec.cpswd)
btn_ctrl = dlg.Button0
btn_ctrl.Click()

#문제의 코드
# time.sleep(50)
# os.system("taskkill /im khmini.exe")
