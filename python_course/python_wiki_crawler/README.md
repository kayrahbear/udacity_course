# [ ] Degrees of Science

A webscraping project utilizing BeautifulSoup and Wikipedia. 

The idea for this project came from reading [this old Huffington Post article](http://www.huffingtonpost.com/2011/11/14/wikipedia-philosophy_n_1093460.html). The article states that if a user clicks the first link on a Wikipedia article, those clicks will eventually 'lead' to the Philosophy article 94.5% of the time.

I decided to try and see if that was still true. It's not. In fact, it seems like (in my limited time testing) most articles lead to the Science article now. How often does that happen? Let's turn this bad boy into a Django project, add some charts (BECAUSE CHARTS!), and track the results over time. 

---

## Dependencies
This project currently utilizes:
* Python 3.6
* requests 
* BeautifulSoup 4 
* Django 

## Running
Everyone:
 * ```git clone <this repository url>```
 * ```cd python_course/python_wiki_crawler```
 ---
 With Anaconda: 
 * Inspect the ```environment.yml``` file. Change line 16 so that it is pointing to your local Anaconda3 env folder.
 * ```conda env create -f environment.yml```
    * this will create a virtual environment named p_w_c and install all dependencies into that env.
 * Activate environment:
    * Windows: ```activate p_w_c```
    * OSX/ Linux: ```source activate p_w_c```
 
 Without Anaconda:
 * Install Python 3.6 & pip if you haven't already
 * Install requests ```pip install requests```
 * Install BeautifulSoup 4 ```pip install beautifulsoup4```
 ---
 Everyone:
 * ```python wiki_crawling.py```
    * Showcases current functionality. Chooses a random wikipedia article and tries to travel to the Science article by choosing the first link it finds. You can follow the progress in the terminal.  
 
 
 
