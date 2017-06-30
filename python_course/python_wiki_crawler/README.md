# [ ] Degrees of Science

A webscraping project utilizing BeautifulSoup and Wikipedia. 

The idea for this project came from reading [this old Huffington Post article](http://www.huffingtonpost.com/2011/11/14/wikipedia-philosophy_n_1093460.html). The article states that if a user clicks the first link on a Wikipedia article, those clicks will eventually 'lead' to the Philosophy article 94.5% of the time.

I decided to try and see if that was still true. It's not. In fact, it seems like (in my limited time testing) most articles lead to the Science article now. How often does that happen? Let's turn this bad boy into a Django project, add some charts (BECAUSE CHARTS!), and track the results over time. 

## Dependancies
This project currently utilizes:
* Python 3.6
* requests ```pip install requests```
* BeautifulSoup 4 ```pip install ```
* Django 
