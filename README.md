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

Apart from the function required, I also added some function to the website: 
- Allow user to change their password but cannot same as current password
- Allow users to buy more shares or sell shares of stocks they already own via click the button on the index page, without having to type stocks’ symbols manually.
- Allow users to add more cash into their account via the add cash page

## Tools:
- Flask for backend development
- HTML for website strcuture 
- Bootstrap for design
- <a href="https://iexcloud.io/">IEX API</a> to get the stocks valus in real time
- sqlite3 for storing users information (username and hashed password) and the transaction record (bought or sold)

## Website:

Every user after registered will have $10000 by default
- Login page:
![image](https://user-images.githubusercontent.com/78290169/147714592-d4823736-11ad-450a-b210-29a6185d1825.png)

- Register page:
![image](https://user-images.githubusercontent.com/78290169/147714600-5cdaa2a6-07b3-43c6-9145-ccc22bdda35f.png)

- Index page (after login your own accout):
![image](https://user-images.githubusercontent.com/78290169/147714625-d0c55db0-b2a4-4580-82e3-c3831f005a0a.png)

- Quote page (Input the stock symbol for checking the stock info):
![image](https://user-images.githubusercontent.com/78290169/147714647-13237e35-7086-4283-9a39-87f5b95dce59.png)

- Buy page (Input the stock symbol and number of shares to buy):
![image](https://user-images.githubusercontent.com/78290169/147714669-2b86ce99-2355-4c30-9cfa-b90d39425783.png)

- Sell page (Select the stock that you have bought in the drop-down list and input the number of shares to sell):
![image](https://user-images.githubusercontent.com/78290169/147714696-bf31961f-c088-4ac1-a176-602e4b115441.png)

- History page (Show all your action on the page such as sell, buy):
![image](https://user-images.githubusercontent.com/78290169/147714709-0a236bf0-20af-446b-b98d-1deabffe9016.png)

- Change password (Allow user to change their password but cannot input the new password same as current password):
![image](https://user-images.githubusercontent.com/78290169/147714736-75e2526e-4512-4ce1-b848-cadadef408c0.png)

## Reference:
- Bootstrap https://getbootstrap.com/docs/5.1/getting-started/introduction/
- W3School
- Stack Overflow
