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
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/yearly_plot_by_clinic.png" align='center'/>
</div>
<h1 align='center'> 3. The effect of handwashing </h1>
With the data loaded we can now look at the proportion of deaths over time. In the plot below we haven't marked where obligatory handwashing started, but it reduced the proportion of deaths to such a degree that you should be able to spot it!
<div align='center'>
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/monthly_plot_clinic1.png" align='center'/>
</div>
<h1 align='center'> The effect of handwashing highlighted </h1>
Starting from the summer of 1847 the proportion of deaths is drastically reduced and, yes, this was when Semmelweis made handwashing obligatory.

The effect of handwashing is made even more clear if we highlight this in the graph.
<div align='center'>
<img src="https://raw.githubusercontent.com/AzerbaijanOpenSourceCommunity/neural-networks-and-machine-learning/master/images/bef_af_washing.png" align='center'/>
</div>