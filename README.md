create a new repository on the command line\n

echo "# ml1" >> README.md \n
git init \n
git add README.md \n
git commit -m "first commit"\n
git branch -M main\n
git remote add origin https://github.com/Elmsvi-Git/ml1.git\n
git push -u origin main\n

…or push an existing repository from the command line\n
git remote add origin https://github.com/Elmsvi-Git/ml1.git\n
git branch -M main\n
git push -u origin main\n
