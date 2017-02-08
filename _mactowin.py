import os, sys
#move to window os
if os.name=="posix":
	os.system(\
		'source /Users/seohasong/.bash_profile\n\
		rm -rf __pycache__\n\
		mactowin'\
		.replace("\t",""))	
	print("이 운영체제는 맥OS임!\n\
		그래서 이문서는 실행되지 않고 윈도우 운영체제로 전송되었음!\n\
		본격적인 실행은 윈도우에서 하면됨~"\
		.replace("\t",""))
	sys.exit()