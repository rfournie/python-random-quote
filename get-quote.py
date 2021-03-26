  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)

git add get-quote.py
git commit -m "Random quote bot is working"
git push
