#-*-coding:utf-8-*-
import  unittest
import  os
import sys
import  time
import  HTMLTestRunner
reload(sys)
sys.setdefaultencoding('utf-8')

def suite():
    dir_case=unittest.defaultTestLoader.discover(
        start_dir=os.path.join(os.path.dirname(__file__),'testcase'),
        pattern='test_*.py',
        top_level_dir=None
        )
    return dir_case

def getNow():
    '''获取当前时间'''
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def filePath():
    '''获取测试报告的目录'''
    return os.path.join(os.path.dirname(__file__),'report',getNow()+'testReport.html')

def readFile():
    '''二进制写入'''
    fp=file(filePath(),'wb')
    return fp

def run():
    runner=HTMLTestRunner.HTMLTestRunner(
		stream=readFile(),
		title=u'自动化测试报告',
		description=u'自动化测试报告详细的信息'
	)
    runner.run(suite())

if __name__=='__main__':
    run()