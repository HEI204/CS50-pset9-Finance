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

Apart from the function required and the built in function provided in this exercise, I also added some function to the website: 
- Allow user to change their password but cannot same as current password
- Allow user to check their profit for the stock that they have bought
- Allow users to buy more shares or sell shares of stocks they already own via click the button on the index page, without having to type stocks’ symbols manually.
- Allow users to add more cash into their account via the add cash page

## Tools:
- Flask for backend development
- HTML for website strcuture 
- Bootstrap for design
- <a href="https://iexcloud.io/">IEX API</a> to get the stocks valus in real time
- sqlite3 for storing users information (username and hashed password) and the transaction record (bought or sold)

## Website:

Test account: user012 ; password: 123456 <br><br>

Every user after registered will have $10000 by default
- Login page:
![image](https://user-images.githubusercontent.com/78290169/147714592-d4823736-11ad-450a-b210-29a6185d1825.png)

- Register page:
![image](https://user-images.githubusercontent.com/78290169/147714600-5cdaa2a6-07b3-43c6-9145-ccc22bdda35f.png)

- Index page (after login your own accout):
it will show about your stock info with the price when you bought and total price for total number of share when you bought. Also,
it will show about the latest profit for your stock 
![image](https://user-images.githubusercontent.com/78290169/147842674-aff20c29-7089-41b0-a239-319b587252c9.png)

- Quote page (Input the stock symbol for checking the stock info):
![image](https://user-images.githubusercontent.com/78290169/147733972-835636ec-cb12-4b1d-861f-6d9959ba5918.png)

- Buy page (Input the stock symbol and number of shares to buy):
![image](https://user-images.githubusercontent.com/78290169/147733981-27e16096-e237-463a-a805-2350ab5907ba.png)

- Sell page (Select the stock that you have bought in the drop-down list and input the number of shares to sell):
![image](https://user-images.githubusercontent.com/78290169/147733999-048bbee0-b02e-48c1-82ba-4408c2e51351.png)

- History page (Show all your action on the page such as sell, buy):
![image](https://user-images.githubusercontent.com/78290169/147842677-19c801c2-7d85-4a20-b267-92ba18bcabd5.png)

- Add Cash:
![image](https://user-images.githubusercontent.com/78290169/147734058-51e9cb87-fed3-41b0-abc5-e4d372bf94b2.png)

- Change password (Allow user to change their password but cannot input the new password same as current password):
![image](https://user-images.githubusercontent.com/78290169/147734093-b6fd2d4c-78c4-47d4-a684-f6b7775afee2.png)

## Reference:
- Bootstrap https://getbootstrap.com/docs/5.1/getting-started/introduction/
- W3School
- Stack Overflow
