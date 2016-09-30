Review of Yuan Shi's Citibike Analysis - by Geoff Perrin

a. <verify that their Null and alternative hypotheses are formulated correctly>
 
Yuan's null hypothesis looks correct, and the alternative hypothesis is 
nearly correct - my one suggestion is with the inequality. I would say that
Amount(m) < Amount(a), rather than Amount(m) <= Amount(a), as you do not want
overlapping null and alternative hypotheses. I would also want to restrict both hypotheses
to test only weekday trips, as weekend rush hour doesnt necessarily exist in NYC

b.<verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)>

My first suggestion would be to remove weekend rides, as the hypothesis seems to want to be testing commuter hours, rather than all morning / afternoon rides. To test my hypothesis, I would structure the data so that the data is aggregated by the total number of rides per calendar day, rather than the total number of rides per hour, as this would give us a larger n and a more robust test. In this case, if you aggregate by hour, you really only have an n of 4 for morning and afternoon.

c. Choose an appropriate test to test H0

I would use a t-test to test H0, where the data is structured as outlined above, with the data aggregated by the total number of rides per calendar day, split into morning ride count and afternoon ride count for each calendar day. This would give us an n of 30 for morning and afternoon. Since we dont know the population standard deviation, and our sample size is still relatively small, I would favor the t-test over the z-test. I would then compute the mean morning counts and afternoon counts and see if the morning mean is significantly greater than the afternoon mean. If it is, then the null hypothesis can be rejected. 
