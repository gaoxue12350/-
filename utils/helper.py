#!/usr/bin/env python
#-*-coding:utf-8-*-
import  os
import  xml.dom.minidom
class DataHelper(object):
	def base_dir(self,path1,path2):
		return os.path.join(os.path.dirname(os.path.dirname(__file__)), path1, path2)

	def getXmldata(self,value):
		dom = xml.dom.minidom.parse(self.base_dir('data','system.xml'))
		db = dom.documentElement
		name = db.getElementsByTagName(value)
		nameValue = name[0]
		return nameValue.firstChild.data

	def getXmlUser(self,parent, child):
		dom = xml.dom.minidom.parse(self.base_dir('data','system.xml'))
		db = dom.documentElement
		itemlist = db.getElementsByTagName(parent)
		item = itemlist[0]
		return item.getAttribute(child)




