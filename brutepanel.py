# coding: utf-8
#!/usr/bin/env python

#:::::::::::::::::::::::#
#      BrutePanel       #
#:::::::::::::::::::::::#

# A modern admin-panel finder (bruteforcer + search + dorker + port scanner)
# https://github.com/code-sploit/brutepanel

import httplib
import socket
import requests
import google
import time
import os
import re
import bs4
from time import sleep
from bs4 import BeautifulSoup
from google import search

#############################
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'
W  = '\033[1;0m'  # white (normal)
R  = '\033[1;31m' # red
G  = '\033[1;32m' # green
O  = '\033[1;33m' # orange
B  = '\033[1;34m' # blue
P  = '\033[1;35m' # purple
C  = '\033[1;36m' # cyan
GR = '\033[1;37m' # gray
T  = '\033[1;93m' # tan
M = '\033[1;35;32m' # magenta
################################

def adminpanel():
	
	  #here you can edit all the paths as per your choice
	
	  quick = ['admin/','administrator/','admin/login.html','admin/index.html','wp-login.php','admin/admin-login.php','admin_login.php', 'adm.php','login.html','administrator.html','login.html','admin.html','cp.html','adminpanel.php','admin_login.php','cpanel','user_login','admin-area/login.php']

	  regular = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','_admin/','usuarios/',
'usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','webadmin/login.php','webadmin/index.php','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html', 'adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php','cpanel']  

	  thorough = [ 'admin/slider.php','admin/add-slider.php','admin/add_gallery_image.php','admin/welcome.php','admin/configration.php','admin/dashbord.php','manage_admin.php','admin/form.php','admin/my_account.php','admin/specializations.php',
'admin/initialadmin.php','admin/pages/home_admin.php','admin/home.php','/admin/save.php','admin/enter.php','admin/userpage.php','admin/banners_report.php','admin/login-home.php','admin/category.php','admin/dashboard/index.php','admin/add_banner.php',
'admin/add_testimonials.php','admin/userpage.php','admin_main.html','admin/addblog.php','admin/products.php','admin/admin_management.php','admin/add.php','admin/add-room.php','admin/main_page.php','admin/adminview.php','admin/welcomepage.php','admin/index-digital.php',
'admin/overview.php','admin_home.php','admin/admin_users.php','/admin/upload.php','admin/index_ref.php','admin/checklogin.php','admin/member_home.php','admin/banner.php','admin/manageImages.php','admin/login_success.php','admin/leads.php',
'admin/uhome.html','admin/AdminDashboard.php','admin/cpanel.php','admin/manage_team.php','admin/voucher.php','admin/ManageAdmin.php','admin/dashboard.php','admin/account.php','admin/change_gallery.php','admin/list_gallery.php','admin/viewblog.php','admin/main.php',
'admin/AdminHome.php','admin/dash.php','admin/gallery.php','admin/product.php','admin/loginsuccess.php','admin/gallery.php','admin/headline.php','admin/page_management.php','admin/index.php','admin/event.php','admin/admin-home.php','admin/myaccount.php','admin/admin_index.php',
'admin/viewmembers.php','admin/default.php','admin/CPhome.php','admin/control_pages/admin_home.php','admin/adminarea.php','cpanel']

	  php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','webadmin/login.php','webadmin/index.php','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php','cpanel',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

	  jsp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.jsp','admin/index.jsp','admin/login.jsp','admin/admin.jsp','admin/account.jsp',
'admin_area/admin.jsp','admin_area/login.jsp','webadmin/login.jsp','webadmin/index.jsp','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.jsp','bb-admin/index.jsp','bb-admin/login.jsp','bb-admin/admin.jsp','admin/home.jsp','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.jsp','admin.jsp','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.jsp','cp.jsp','administrator/index.jsp','administrator/login.jsp','nsw/admin/login.jsp','webadmin/login.jsp','admin/admin_login.jsp','admin_login.jsp',
'administrator/account.jsp','administrator.jsp','admin_area/admin.html','pages/admin/admin-login.jsp','admin/admin-login.jsp','admin-login.jsp',
'bb-admin/index.html','bb-admin/login.html','acceso.jsp','bb-admin/admin.html','admin/home.html','login.jsp','modelsearch/login.jsp','moderator.jsp','moderator/login.jsp',
'moderator/admin.jsp','account.jsp','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.jsp','admincontrol.jsp',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.jsp','adminarea/index.html','adminarea/admin.html','.admin_login.jsp','ADMIN.jsp',
'webadmin.jsp','webadmin/index.jsp','webadmin/admin.jsp','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.jsp','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.jsp','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.jsp','wp-login.jsp','adminLogin.jsp','admin/adminLogin.jsp','home.jsp','admin.jsp','adminarea/index.jsp',
'adminarea/admin.jsp','adminarea/login.jsp','panel-administracion/index.jsp','panel-administracion/admin.jsp','modelsearch/index.jsp',
'modelsearch/admin.jsp','admincontrol/login.jsp','adm/admloginuser.jsp','admloginuser.jsp','admin2.jsp','admin2/login.jsp','admin2/index.jsp','usuarios/login.jsp',
'adm/index.jsp','adm.jsp','affiliate.jsp','adm_auth.jsp','memberadmin.jsp','administratorlogin.jsp','cpanel']

	  asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','webadmin/login.asp','webadmin/index.asp','webadmin/login.html','cpanel']

	  cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','webadmin/login.cfm','webadmin/index.cfm','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm','cpanel']

	  js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','webadmin/login.js','webadmin/index.js','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js','cpanel']

	  cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
'admin_area/admin.cgi','admin_area/login.cgi','webadmin/login.cgi','webadmin/index.cgi','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi','cpanel']

	  brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
'admin_area/admin.brf','admin_area/login.brf','webadmin/login.brf','webadmin/index.brf','webadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf','cpanel']    

	  brutefound200 = []
	  brutefound302 = []
	  bruteother = []
	  respother = []
	  searchfound = []
	  dorkfound = []
	  portfound = []

	  def brute():

	    global web
	    print ''
	    time.sleep(1)
	    print ''+R+'\n\n              B R U T E F O R C E R\n'
	    global var1, var2
	    print ''+O+'\n  Choose the type of bruteforce you want to perform :-'
	    time.sleep(0.3)
	    print ''+GR+' +=====================================================+\n'
	    print ""+C+"  [1] \033[1;94mSpecific (more chances of detection)"
	    print ""+G+" -- This type of bruteforce requires knowledge of the"
	    print ""+G+"        lang. in which the website is written in."
	    time.sleep(0.3)
	    print ""+C+"  [2] \033[1;94mRandom (less chances)"
	    print ""+G+" -- This bruteforce is for websites which you have zero"
	    print ""+G+"                  knowledge of.\n"
	    print ''+GR+' +=====================================================+\n'
	    time.sleep(0.2)
	    co = raw_input(''+GR+' ▣ \033[1;4mTID\033[0m'+GR+' :> ' + color.END)
	    if co == '2':
		    print ''
		    print ''+R+ '  Choose the type of bruteforce you want to perform :-'
		    time.sleep(0.2)
		    print ''+GR+' +========================================+\n'
		    print ""+C+"      [1] \033[94mA Quick Bruteforce"
		    time.sleep(0.05)
		    print ""+C+"      [2] \033[94mA Regular Bruteforce "
		    time.sleep(0.05)
		    print ""+C+"      [3] \033[94mA Thorough Bruteforce \n"
		    time.sleep(0.05)
		    print ''+GR+' +========================================+\n' 
		    time.sleep(0.2)
		    code = raw_input(''+GR+' ▣ \033[1;4mTID\033[0m'+GR+' :> ' + color.END)
		    time.sleep(0.2)
		    if code =='1':
			print ""+O+"\n [¬] Scan Type Selected: "+GR+"Quick Shuffle"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n")
			time.sleep(1)
		        for admin in quick:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [*] The bruteforce completed, press "+GR+"'Enter'"+C+" to continue")
			if s == "":
			    pass			

		    elif code =='2':
			print ""+O+" [¬] Scan Type Selected: "+GR+"Regular"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in regular:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+"  [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+"  [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='3':
			print ""+O+" [¬] Scan Type Selected: "+GR+"Thorough Scan"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in thorough:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

	    elif co == '1':
		    print ''
		    print ''+R+ 'Choose the type of website you want bruteforce to perform :-\n'
		    print ''+GR+'+================================+\n'
		    print ""+C+"     [1] \033[94mPHP Website"
		    print ""+C+"     [2] \033[94mASP Website"
		    print ""+C+"     [3] \033[94mCFM Website"
		    print ""+C+"     [4] \033[94mJS Website"
		    print ""+C+"     [5] \033[94mCGI Website"
		    print ""+C+"     [6] \033[94mJSP Website"
		    print ""+C+"     [7] \033[94mBRF Website\n"
		    print ''+GR+'+================================+' 
		    code = raw_input(""+O+"\n  Enter the number corresponding to the type :> ")
		    if code =='1':
			print ""+O+" [¬] Web Type Selected: "+GR+"PHP"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in php:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='2':
			print ""+O+" [¬] Web Type Selected: "+GR+"ASP"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in asp:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+"       [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='3':
			print ""+O+" [¬] Web Type Selected: "+GR+"CFM"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in cfm:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='4':
			print ""+O+" [¬] Web Type Selected: "+GR+"JS"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in js:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
				connection.close()
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='5':
			print ""+O+" [¬] Web Type Selected: "+GR+"CGI"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in cgi:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
				connection.close()
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='6':
			print ""+O+" [¬] Web Type Selected: "+GR+"JSP"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in jsp:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass

		    elif code =='7':
			print ""+O+" [¬] Web Type Selected: "+GR+"BRF"
			time.sleep(0.8)
		        print(""+B+"\n [+] Scanning initiated -> "+GR+"" +web+""+B+ "...\n\n")
			time.sleep(1)
		        for admin in brf:
		            admin = admin.replace("\n","")
		            admin = "/" + admin
		            host = web + admin
		            print (""+C+" [*] Checking -> "+ P +""+ host )
		            connection = httplib.HTTPConnection(web)
		            connection.request("GET",admin)
		            response = connection.getresponse()
		            if response.status == 200:
		                var1 = var1 + 1
		                print "%s %s" % (""+C+"\n\n [+] " + host, ""+G+"Admin page found!\n")
				brutefound200.append(host)
				break
		            elif response.status == 404:
		                var2 = var2 + 1
				var2 = var2
		            elif response.status == 302:
		                print "%s %s" % (""+G+"\n [!] " + host, "Possible admin page (302 - Redirect)\n")
				brutefound302.append(host)
		            else:
		                print "%s %s %s" % (""+G+" [!] "+host, ""+O+" Interesting response: ", response.status)
				bruteother.append(host)
				respother.append(response.status)
		            connection.close()
		        print(""+GR+"\n [!] Completed \n")
			time.sleep(0.5)
		        print(""+O+" [!] Admin page path found -> %s" % (host))
			time.sleep(0.5)
		        print(""+O+" [!] Total Pages Scanned -> %s" % (var2))
			time.sleep(0.5)
		        s=raw_input("\n"+C+" [!] The bruteforce completed, press 'Enter' to continue")
			if s == "":
			    pass
			    print ''

	  def search():
		
		from google import search
		global web
		time.sleep(0.4)
		print ''+R+'\n\n          G O O G L E   S E A R C H\n'
		time.sleep(0.8)

		try:
		        wordlist = ['admin login site of ','admin site of ','login page of ','cpanel login page of '] 
            	        for lol in wordlist:
				lol = lol + str(web)
				print ''+C+" [!] Trying query : '" +B+ str(lol) + "'"
		    		for url in search(lol, tld='com', lang='es', stop=25):
				    if str(web) in str(url):
					print(""+O+color.BOLD+" [!] Site Found :> "+W+"" + url)
					searchfound.append(url)

		except:
			print ' [!] Some error occured!'

	  def dorker():

		global web
		print ''+R+'\n\n           G O O G L E   D O R K E R \n'
		connection = httplib.HTTPSConnection("www.google.com")
		connection.request("GET", "/search?q=inurl:admin+site:"+str(web))
		connection.addheaders=[('User-agent', 'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)')]
		response = connection.getresponse()

		if response.status == 302:
	
			html_response = response.read()
			urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', html_response)
			host_name = re.findall('(?:[a-zA-Z0-9](?:[a-zA-Z0-9\-]{,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}',urls[0])
			connection = httplib.HTTPSConnection(host_name[0])
			connection.request("GET", "/search?q=inurl:admin+site:"+str(web))
			connection.addheaders=[('User-agent', 'Opera/9.80 (Macintosh; U; de-de) Presto/2.8.131 Version/11.10')]
			response = connection.getresponse()
	
		if response.status == 200:
	
			soup = BeautifulSoup(response.read(), "lxml")
			divList = soup.findAll('cite')
			for ids in divList:

				print (C+" [!] Site Found :> "+O+ids.text)
				dorkfound.append(ids.text)

	  def portscan():

		global web
		print ''+R+'\n\n            P O R T   S C A N N E R \n'
		commonports = [2082,2083,2095,2096] # some websites use these ports for keeping the admin login panel
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		for port in commonports:
	
			try:
				lol = str(web)+':'+str(port)
				print GR+' [!] Trying connections against '+lol
				s.connect((ip, int(port)))
				s.shutdown(5)
				time.sleep(0.6)
				print(G+" [!] Port "+str(port)+" : Open")
				print C+' [!] Possible admin page at --> '+O+lol
				portfound.append(lol)
				time.sleep(0.5)
				break
        	        except: 
                		print R+' [-] No open port at --> '+O+str(web)+':'+str(port)
				time.sleep(0.5)

	  def main():

	     try:
		os.system('clear')
	  	print ''
		print ''
		print ""+C+"    ________              _____           ________                   ______"
		time.sleep(0.1)
		print ""+C+"    ___  __ )__________  ___  /_____      ___  __ \_____ _______________  /"
		time.sleep(0.1)
		print ""+B+"    __  __  |_  ___/  / / /  __/  _ \     __  /_/ /  __ `/_  __ \  _ \_  / "
		time.sleep(0.1)
		print ""+B+"    _  /_/ /_  /   / /_/ // /_ /  __/     _  ____// /_/ /_  / / /  __/  /  "
		time.sleep(0.1)
		print ""+C+"    /_____/ /_/    \__,_/ \__/ \___/      /_/     \__,_/ /_/ /_/\___//_/   \n"
		time.sleep(0.1)
		print ''+GR+'                                  [ v 1.0.1 ]\n'
		print ''+B+'             Coded with '+R+'<3'+B+' by '+P+'@_tID'+B+' (Team '+P+'CodeSploit'+B+')\n'
		global var1
		global var2
		global web
		var1=0
		var2=0
	  	try:

			web = raw_input(''+O+' [¬] Enter target website :> '+G+'')
			time.sleep(0.4)
			print (""+R+" [!] Target set :> "+O+"%s" % (web))
	  		time.sleep(0.1)
	        	web = web.replace("http://","")
	        	print (""+C+"\n [*] Checking availability -> " + web)
			time.sleep(1)
	        	conn = httplib.HTTPConnection(web)
	        	conn.connect()
	        	print (""+G+" [!] Server detected online.")
	  	except (httplib.HTTPResponse, socket.error) as Exit:
	        	raw_input(""+R+" [!] Error occured, Server is Offline or Invalid URL")
			sys.exit(0)
	  
		time.sleep(0.4)
		print ''+B+'\n [*] Preparing modules...'
		time.sleep(0.6)
		print ''+GR+' [*] Preparing action lists...'
		time.sleep(1)  
		print ''+O+' [*] Loading module [1] BRUTEFORCER...'
		brute()
		time.sleep(0.4)
		print ''+B+'\n [*] Preparing next module...'
		time.sleep(0.6)
		print ''+GR+' [*] Preparing action lists...'
		time.sleep(1)  
		print ''+O+' [*] Loading module [2] GOOGLE SEARCH...'
		search()
		time.sleep(0.4)
		print ''+B+'\n [*] Preparing next module...'
		time.sleep(0.6)
		print ''+GR+' [*] Preparing action lists...'
		time.sleep(1)  
		print ''+O+' [*] Loading module [3] GOOGLE DORKER...'
		dorker()
		time.sleep(0.4)
		print ''+B+'\n [*] Preparing next module...'
		time.sleep(0.6)
		print ''+GR+' [*] Preparing action lists...'
		time.sleep(1)  
		print ''+O+' [*] Loading module [4] PORT SCANNER...'
		portscan()
		print C+'\n [!] Admin Panel Hunt Completed!'

		print B+'\n    +---------------+'
		print B+'    |  '+R+'R E P O R T  '+B+'|'
		print B+'    +---------------+\n'
		print P+'    Bruteforce'
		print P+'    =========='

		if brutefound200:
		    print C+'    |'
		    for m in brutefound200:
			print C+'    +-- '+GR+m+P+' [Response 200]'
		else:
		    print R+' [-] No real admin path found'

		if brutefound302:
		    print C+'    |'
		    for m in brutefound302:
			print C+'    +-- '+GR+m+O+' [Response 302]'

		if bruteother:
		    print C+'    |'
		    for m in xrange(len(bruteother)):
			print C+'    +-- '+GR+ str(bruteother[m]) +B+' [Response '+ str(respother[m]) +']'
		print ''

		print P+'    Google Search'
		print P+'    ============='
		if searchfound:
		    print C+'    |'
		    for m in searchfound:
			print C+'    +-- '+GR+m
		else:
		    print R+' [-] No results from Google Search'

		print ''

		print P+'    Google Dork'
		print P+'    ==========='
		if searchfound:
		    print C+'    |'
		    for m in dorkfound:
			print C+'    +-- '+GR+m
		else:
		    print R+' [-] No results from Google Dorks'	

		print ''	    

		print P+'    Port Scan'
		print P+'    ========='
		if searchfound:
		    print C+'    |'
		    for m in portfound:
			print C+'    +-- '+GR+m
		else:
		    print R+' [-] No results from Port Scan'

		print ''

		print GR+' [*] Shutting Down...'
		time.sleep(0.4)
		print G+' [!] Goodluck mate! See ya!\n'
	     except KeyboardInterrupt:
		print ''+R+' [!] User requested SHUTDOWN!'
		print ''+O+' [!] Exiting...\n'
		sys.exit(0)
	  main()
		
adminpanel()
