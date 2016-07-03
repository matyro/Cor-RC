from Website.site_base import BaseHandler

import tornado.web
import tornado

import time
import os

class EditHandler(BaseHandler):
    @tornado.web.authenticated 
    def get(self):
        if self.current_user is None:
            self.redirect('login.html?next=edit')
            return
			
        print('Files:')
        htmlTreeView = ''
         
        for dirname, dirnames, filenames in os.walk('./'):
            if '.git' in dirnames:                
                dirnames.remove('.git')
            if 'flot' in dirnames:                
                dirnames.remove('flot')
            if '__pycache__' in dirnames:
                dirnames.remove('__pycache__')
            
            ##print('New loop ' + str(dirname) + ' | ' + str(dirnames) + ' >' + str(os.path.basename(dirname)))
           
            if len(filenames) > 0:
                htmlTreeView = htmlTreeView + '<li><span><i class="glyphicon glyphicon-folder-open"></i> ' +  str(os.path.basename(dirname)) + '</span>\n'
                htmlTreeView = htmlTreeView + '<ul>\n'
                for filename in filenames:
                    htmlTreeView = htmlTreeView + '<li style="display:none;"><span><i class="glyphicon glyphicon-leaf"></i>  ' + '<a href=\"/edit?action=load&file=' + os.path.join(dirname, filename) + '\">' + str(filename) + '</a>' + '</span>\n'
                    ##print(os.path.join(dirname, filename))           
            
                htmlTreeView = htmlTreeView + '</ul>'
        
        readFile = ''
        readPath = ''
        for itr in self.get_arguments('action', strip=True):
            
            if itr == 'reload':
                print('Test permission for reload:')
                if self.current_user.permission >= 9000:
                    print('System shutdown!')
                    self.redirect('/edit')
                    time.sleep(1)
                    tornado.ioloop.IOLoop.current().stop()
                else:
                    print('User %s: illegal shutdown!' % self.current_user.username)
                    self.render('edit.html', msg='You dont have the permission to do that!', fileTree=htmlTreeView, fileContent=readFile, filePath=readPath)
            
            if itr == 'load':
                print('Load: ' + str(self.get_argument('file')))
                try:
                    f = open(self.get_argument('file'), 'r+')
                    readFile = f.read()
                    f.close()
                    readPath = self.get_argument('file')
                except FileNotFoundError:
                    print('File not found!')
                    self.render('edit.html', msg='File %s not found!' % self.get_argument('file'), fileTree=htmlTreeView, fileContent=readFile, filePath=readPath)
                    return
           
                    
        self.render('edit.html', msg=None, fileTree=htmlTreeView, fileContent=readFile, filePath=readPath)
         
        
    def post(self):       
        self.set_header("Content-Type", "text/plain")
        
        print(str(self.request.arguments))
        filePath = self.get_argument('filePath',  u'')
        fileContent = self.get_argument('fileContent', u'')
        
        if len(filePath) > 0:
            try:
                f = open(filePath, 'w')
                f.write( fileContent )
                f.close();
            except:
                print('Exception')
                raise
                    
        self.redirect('/edit?action=load&file=' + self.get_argument('filePath'))