echo start
python3 -m pip freeze > requirements.txt
echo 1
git pull origin master
echo 2
git add .
echo 3
git commit -m "新提交"
echo 4
git push origin master
echo end
