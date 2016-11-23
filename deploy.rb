
require 'rubygems'
require 'json'
require 'highline/import'	
require 'net/ssh'
require 'optparse'
require 'net/scp'
require 'io/console'

class BasicOperation
	def self.yesno(prompt = 'Continue?', default = true)
	  a = ''
	  s = default ? '[Y/n]' : '[y/N]'
	  d = default ? 'y' : 'n'
	  until %w[y n].include? a
	    a = ask("#{prompt} #{s} ") { |q| q.limit = 1; q.case = :downcase }
	    a = d if a.length == 0
	  end
	  a == 'y'
	end
# -----------------------copying satori.sh through scp connection ------------------
	def self.connect_remote(cert_path,local_path,server,username,app_path,commit_string,core_deploy)
		p "------------ committing and pushing from local----------------"
		p `cd #{local_path} && git add . && git commit -m "#{commit_string}" && git push origin master`
		Net::SSH.start( server, username, :keys => cert_path ) do |ssh|

			p "---------------connect-----------"
			if core_deploy
				results = ssh.exec("cd #{app_path} && git pull origin master")
				p "Migration ______#{app_path}"
				results = ssh.exec("sudo service apache2 reload")
				results = ssh.exec("sudo service apache2 restart")
			else
				results = ssh.exec("cd #{app_path} && git pull origin master")
				results = ssh.exec("sudo service apache2 reload")
				results = ssh.exec("sudo service apache2 restart")
			end		   	
		   	
		end
		p "--------------- connection out --------------"
	end
end

local_path = "/home/vicky/Documents/workspace/flaskapp/flaskapp_deploy"
cert_path = "/home/vicky/Documents/instance_certs/minion.pem"
server = "35.164.12.89"
username = "ubuntu"
app_path = "/home/ubuntu/flaskapp"

if BasicOperation.yesno("Environment change?", true)
	core_deploy = true
else
	core_deploy = false
end
p "Enter the commit message"
commit_string = gets.chomp
BasicOperation.connect_remote(cert_path,local_path,server,username,app_path,commit_string,core_deploy)