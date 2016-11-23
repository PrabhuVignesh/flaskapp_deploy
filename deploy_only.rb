require 'rubygems'
require 'git'
spawn "echo 'sdsd'"
sleep 2
Dir.chdir('/home/vicky/Documents/flaskapp/flaskapp_deploy')
working_dir ="/home/vicky/Documents/flaskapp/flaskapp_deploy"
 g = Git.open('/home/vicky/Documents/flaskapp/flaskapp_deploy', :log => Logger.new(STDOUT))
 
 p "'git add . ' is running"
 g.add(:all=>true)  
  str = 'git commit -m "Committing code for Time.now"'

p "'#{str}' is running"
g.commit("Committing code for #{Time.now}")
p "Pushing to git hub"
g.push(g.remote('origin'))