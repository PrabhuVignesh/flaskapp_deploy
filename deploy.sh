cd /home/vicky/Documents/flaskapp/flaskapp_deploy && git add . && git commit -m "Changes from dev deployment" && git push origin master
ssh ubuntu@35.164.12.89 'bash -s' < local_script.sh
