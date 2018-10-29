<h1> Linear Regression </h1>
<h5> Linear Regression is the simplest type of Supervised learning.</h5><p>The goal of Regression is to explore the relation between the input Feature with that of the target Value and give us a continuous Valued output for the given unknown data.
<div align='center'>
<h6 align='center'>Linear Regression Model</h6> 
<img align="center" src='https://cdn-images-1.medium.com/max/1200/0*FjKhbw6Va8O8bCkF.png'>
</div>
<br>
<ul>
<li><span style='color:#f03c15'>Red</span> line indicates regression line</li>
<li><span style='color:blue'>Blue</span> points our actual data - observation points</li>
<li><span style='color:black'>Black lines called <b>residuals - difference between the observation points and fitted line</b></li>
</ul>
  <br><br>
  <p>All we're trying to do when we calculate our regression line is draw a line that's as close every observation points as possible</p>
  <p>For classic linear regression , or "Least Squared Method", you only measure the closeness in "up and down" direction</p>
  <p>Our mission with linear regression is to <b>minimize the vertical distance</b> between ald data points and our regression line.So for finding best fitted line we should minimize the distance between all the points and their distance to our line </p>
  <p>There are a lot of different ways to minimize this ,(<b>mean squared error,mean absolute error,root mean square error</b>) I implemented all these 3 ways in <b>linear_regression_boston.py</b> 
 
 <h3> Overview </h3>

  ---
  <ol>
  <li>I explored the boston data set and then renamed its column names</li>
  <li>I explored the boston data set using .DESCR, my goal was to predict the housing prices using the given features.</li>
  <li>I used Scikit learn library in order  to fit linear regression to the entire data set and calculated the mean squared error.</li>
  <li>I made a <b>train-test split</b> and calculated the <b>mean squared error</b> for my training data and test data in order to minimize error</li>
  <li>Visaulize the results</li>
  </ol>
  
  <h3> Visaulizaiton </h3>
 
  ***
  
<div align='center'>
<img align="center" src='https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/lr_boston.png'>
</div>
  
  
 
 