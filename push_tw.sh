cp science-in-the-digital-era.html ../science-in-the-digital-era-gh-pages/index.html
pushd ../science-in-the-digital-era-gh-pages/
git add index.html
git commit -m "Publish"
git reset --soft HEAD~2
git commit -m "Publish"
git push origin -f gh-pages
popd
