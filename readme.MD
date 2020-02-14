https://minimal-dash.herokuapp.com
1. virtualenv venv

2. source venv/bin/activate

3. pip install -r requirements.txt

4. jupyter notebook
    - navigate to the ipynb file to interact with that to see the progression

5. python deploy-example.py
    - to run the local development version

6. Deploy to heroku. Set up heroku cli OS specific

    - https://devcenter.heroku.com/articles/heroku-cli

7. heroku create my-dash-app

8. git init

9. git add .

10. git commit -m 'Initial app'

11. git push heroku master # deploy code to heroku

12. heroku ps:scale web=1