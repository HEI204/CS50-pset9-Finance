# CS50 Finance (Week9: Problem Set)

## Introduction
This is the one of the exercise from CS50x - Introduction for Computer Science: <a href="https://cs50.harvard.edu/x/2021/psets/9/finance/">Exercise detail</a>

The target of this exercise:
<ul> 
  <li>Implement a website that allow user to "buy" and "sell" stock and the following functions:</li>
  <li>Complete the implementation of <b>register</b> in such a way that it allows a user to register for an account via a form.</li>
  <li>Complete the implementation of <b>quote</b> in such a way that it allows a user to look up a stock’s current price.</li>
  <li>Complete the implementation of <b>buy</b> in such a way that it enables a user to buy stocks.</li>
  <li>Complete the implementation of <b>index</b> in such a way that it displays an HTML table summarizing, for the user currently logged in, which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price). Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).
  </li>
  <li>Complete the implementation of <b>sell</b> in such a way that it enables a user to sell shares of a stock (that he or she owns).</li>
  <li>Complete the implementation of <b>history</b> in such a way that it displays an HTML table summarizing all of a user’s transactions ever, listing row by row each and every buy and every sell.
  </li>
</ul>

Apart from the function required, I also added some function to the website such as allow user to change their password and allow users to buy more shares or sell shares of stocks they already own via index itself, without having to type stocks’ symbols manually.

## Tools
- Flask for backend development
- HTML for website strcuture 
- Bootstrap for design
- <a href="https://iexcloud.io/">IEX API</a> to get the stocks valus in real time
- sqlite3 for storing users information (username and hashed password) and the transaction record (bought or sold)

## Reference:
- Bootstrap https://getbootstrap.com/docs/5.1/getting-started/introduction/
- W3School
- Stack Overflow
