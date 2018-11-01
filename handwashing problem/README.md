<h1 align='center'>
1. Meet Dr. Ignaz Semmelweis
</h1>
<div align="center">
 <img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/ignaz_semmelweis.jpg" align='center'/>
</div>

This is Dr. Ignaz Semmelweis, a Hungarian physician born in 1818 and active at the Vienna General Hospital. If Dr. Semmelweis looks troubled it's probably because he's thinking about childbed fever: A deadly disease affecting women that just have given birth. He is thinking about it because in the early 1840s at the Vienna General Hospital as many as 10% of the women giving birth die from it. He is thinking about it because he knows the cause of childbed fever: It's the contaminated hands of the doctors delivering the babies. And they won't listen to him and wash their hands!

In this project, we're going to reanalyze the [data](https://github.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/blob/master/datasets/yearly_deaths_by_clinic.csv) that made Semmelweis discover the importance of handwashing. Let's start by looking at the data that made Semmelweis realize that something was wrong with the procedures at Vienna General Hospital.

<div align="center">
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/data.png" align='center'/>
</div>

<h1 align='center'>
2. Proportion of deaths on both clinics
</h1>
The table above shows the number of women giving birth at the two clinics at the Vienna General Hospital for the years 1841 to 1846. You'll notice that giving birth was very dangerous; an alarming number of women died as the result of childbirth, most of them from childbed fever.

We see this more clearly if we look at the proportion of deaths out of the number of women giving birth. The <b>graph</b> below illustrate information about yearly proportion of deaths at both clinic 1 and clinic 2.
<div align='center'>
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/yearly_plot_by_clinic_new.png" align='center'/>
</div>
<h1 align='center'> 3. The effect of handwashing </h1>
With the data loaded we can now look at the proportion of deaths over time. In the plot below we haven't marked where obligatory handwashing started, but it reduced the proportion of deaths to such a degree that you should be able to spot it!
<div align='center'>
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/monthly_plot_clinic1.png" align='center'/>
</div>
<h1 align='center'> 4. The effect of handwashing highlighted </h1>
Starting from the summer of 1847 the proportion of deaths is drastically reduced and, yes, this was when Semmelweis made handwashing obligatory.

The effect of handwashing is made even more clear if we highlight this in the graph.
<div align='center'>
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/bef_af_washing.png" align='center'/>
</div>

<h1 align='center'> 5. More handwashing, fewer deaths? </h1>
Again, the graph shows that handwashing had a huge effect. How much did it reduce the monthly proportion of deaths on average?
We calculate that by finding difference in <b>mean</b> monthly proportion of deaths due to handwashing. In our case that is `mean_diff` with a value <b>-0.08395660751183336</b>.

<h1 align='center'> 6. A Bootstrap analysis of Semmelweis handwashing data </h1>
It reduced the proportion of deaths by around 8 percentage points! From 10% on average to just 2% (which is still a high number by modern standards).

To get a feeling for the uncertainty around how much handwashing reduces mortalities we could look at a confidence interval (here calculated using the bootstrap method).
A bootstrap analysis is a quick way of getting at the uncertainty of an estimate, in your case the estimate is the `mean_diff` that we calculated before (-0.08395660751183336). A bootstrap analysis works by simulating redoing the data collection by drawing randomly from the data and allowing a value to be drawn many times. Using a pandas column `my_col` (also called a Series) this can be done like this:

`boot_col = my_col.sample(frac=1, replace=True)`
The estimate is then calculated using `boot_col` instead of `my_col`. This process is repeated a large number of times (in our case 3000) and the distribution of the bootstrapped estimates represents the uncertainty around the original estimate. If `boot_mean` is a list of bootstrap estimates you can calculate a <b>95%</b> confidence interval using pandas:

`pd.Series(boot_mean).quantile([0.025, 0.975])`
<h1 align='center'> 7. The fate of Dr. Semmelweis </h1>
So handwashing reduced the proportion of deaths by between <b>6.7</b> and <b>10</b> _(You can see it by running code)_ percentage points, according to a <b>95%</b> confidence interval. All in all, it would seem that Semmelweis had solid evidence that handwashing was a simple but highly effective procedure that could save many lives.

The tragedy is that, despite the evidence, Semmelweis' theory — that childbed fever was caused by some _substance_ (what we today know as bacteria) from autopsy room corpses — was ridiculed by contemporary scientists. The medical community largely rejected his discovery and in 1849 he was forced to leave the Vienna General Hospital for good.

One reason for this was that statistics and statistical arguments were uncommon in medical science in the 1800s. Semmelweis only published his data as long tables of raw data, but he didn't show any graphs nor confidence intervals. If he would have had access to the analysis we've just put together he might have been more successful in getting the Viennese doctors to wash their hands.

# The data Semmelweis collected points to that:
`doctors_should_wash_their_hands = True`

<h5 align='left'>NOTE:
 You can find comments that have written in the _handwashing.py_ python file before every single part of the code which could help you to understand the whole project. <b>Enjoy!</b> </h1>
