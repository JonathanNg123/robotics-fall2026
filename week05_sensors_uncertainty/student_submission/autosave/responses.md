# Week 5: Sensors, Noise, and Uncertainty

- course_id: 24454203
- email: Jonathan.ng03@login.cuny.edu
- name: Jonathan Ng

## concepts.observation

When I increased the noise, the readings became more spread out and became father from 2.0 meters. This shows that the spread of the data was increased, but the measurements were still mostly centered around the line. When I increased the bias, the readings just shifted upward and now centered around 2.2 meters instead of 2.0 meters. This showed that noise causes more spread, while bias causes the sensor to move higher or lower.

## final.course_reflection

This lab helped me understand how important sensor accuracy and decision-making are in robotics. I always knew they were both important, but now I truly understand how much they affect a robot. This is helpful as my group project for this class will need to rely on sensors and decision making a lot and now that I know how important these things are, I will need to properly test the robot's abilities before being confident in submitting anything. In addition, the part that stood out to me the most was comparing the warehouse robot and the assistive robot. It was shocking how different both robots approach problems. Even though both robots use sensors to detect obstacles, they operate in different environments and have different safety concerns.

## final.synthesis

Doing this lab, I learned many things like how sensor measurements and filtering affect the decisions robots make. In Mission 1 for example, I learned that sensor readings are not always accurate because of varaibles such as noise, outliers, or missing information. This shows that robots should not always trust a single measurement and why many readings can help improve accuracy. In Mission 2, after using different filtering methods and window sizes, we see that a window of 3 gave an RMSE of 0.166, while increasing the window to 11 increased RMSE to 0.1851. I also tested a median filter with a window of 3, which gave an RMSE of 0.1637. This shows that using more readings does not always improve accuracy. This also shows that filtering has its own tradeoffs between reducing noise and responding quickly. In Mission 3, warehouse and assistive robots both had a 0% false-safe rate and zero dangerous-command events. After changing the warehouse robot to require two readings however, increased detection delay from 0.15 to 0.20 seconds. This shows that robot settings should depend on the environment and the people around them.

## mission_1.bias

-0.01097

## mission_1.bias_vs_variance

My prediction was mostly similar to the actual statistics because the mean I had calculated was close to 2.00 m, but was slightly off due to some extreme readings. Bias measures how far the average is from the true distance, while variance measures how spread out the readings are. 

## mission_1.dropouts

3

## mission_1.mean

1.989

## mission_1.median

2.0

## mission_1.more_samples

More samples would help, but would not remove the main problems completely. The samples could help make a better stable average, but they would not prevent the sensor from occasionally producing extreme measurements. From my evidence, there were four outliers which will always happen. 

## mission_1.outliers

4

## mission_1.prediction

I predict that for a biased sensor, we will have a mean that is mostly always above or below the true distance which will result in a bigger bias, but low variance.  A noisy sensor will have readings that are more spread out which results in a higher variance, but would mostly be closer to the true distance with little bias.

## mission_1.prediction_draft

I predict that for a biased sensor, we will have a mean that is mostly always above or below the true distance which will result in a bigger bias, but low variance.  A noisy sensor will have readings that are more spread out which results in a higher variance, but would mostly be closer to the true distance with little bias.

## mission_1.profile

quantized

## mission_1.robot_consequence

If a robot is moving and approaches a pedestrian, if  the actual distance is 2.00 m but an outlier reports 2.90 m, the robot might incorrectly believe it has more room to move forward. This is clearly a problem as safetly is in play now. The robot should check these unusual measurements before making important movement decisions.

## mission_1.variance

0.010218

## mission_2.comparison

After comparing the moving average windows of 3, 7, and 11, the RMSE values were 0.1660, 0.1750, and 0.1851 m. Their response delays were 1.30, 1.30, and 1.10 seconds. What we found out was that increasing the window did not necessarily always improve the overall error. After also comparing the moving average and median filters with window 3 and weight of 0.25, I found out that the median had a lower RMSE of 0.1637 m compared to 0.1660 m and a faster response delay of 1.10 seconds compared to 1.30 seconds.

## mission_2.fusion_choice

After comparing the fusion weights of 0.25, 0.50, and 0.75 with a median filter of 3, their RMSE values were 0.1637, 0.1420, and 0.1454 m, while their response delays were 1.10, 1.05, and 0.80 seconds. I personally selected attemot 6 of 0.75 because it was clear it was the fastest response. Using a median filter helps reduce the effects of outliers on Sensor A while giving it more weight improves the responsiveness.

## mission_2.manual_average

4.1667 

## mission_2.manual_fusion

2.25 

## mission_2.manual_median

2.3 

## mission_2.prediction_draft

Increasing the weight on Sensor A from 0.50 to 0.75 should make the fused estimate rely more on Sensor A. rather than Sensor B now. I predict that the noise and outliers from Sensor A could increase the overall error.

## mission_2.responsiveness

Smoothing helps reduce random changes in sensor reading while also delaying the robot's response to changes. In my experiments, the moving averages of window of 3 had a response delay of 1.30 seconds. Compared to the median filter of window of 3 with weight of 0.75, the delay was 0.8 seconds. A longer response delay could cause the robot to see that there is a person nearby too late. This shows why responsiveness is important for safety.

## mission_2.selected

5

## mission_3.Assistive.prediction_draft

After changing the caution margin from 0.20 to 0.10, I predict it may reduce unnecessary stops because the robot will have a smaller area where it needs to be cautious. The problem with this is the safety concerns as it is much less safe when a pedestrian suddenly approaches because the robot may react much later than usual. I expect the robot to move more freely, but there may be a tradeoff between safety and convenience.

## mission_3.Warehouse.prediction_draft



## mission_3.context_comparison

For the two final policies, both original baseline settings for both robots were better because they had faster detection times. The warehouse policy robot uses a stopping threshold of 0.75 m and a caution margin of 0.10 m, while the assistive robot uses a stopping threshold of 0.95 m and a caution margin of 0.20 m. The main difference is that the assistive robot needs a larger safety distance because it is near people with many different speeds. Both policies use a median filter with a window of 3, but the warehouse robot had a maximum detection delay of 0.15 seconds while the assistive robot had 0.05 seconds. Both had a 0% false-safe rate and zero dangerous-command events. After seeing all these different evidences, it is clear that these robots should be using the settings that match the people and environments around them.

## mission_3.error_costs

In the warehouse policy, false-safe errors would put many workers at risk of less safety. Unnecessary-stop would slow down work as it would take a lot of time to complete an instruction due to the constant stopping. Both warehouse policies had a 0% false-safe rate and a 3.06% unnecessary-stop rate. The detection delay increased from 0.15 to 0.20 seconds after requiring two readings before stopping. In the the assistive policy, false-safe errors would put pedestrians at risk, while unnecessary stops could make it harder for people to use the robot. Both assistive policies had a 0% false-safe rate and a 2.03% unnecessary-stop rate. However, detection delay increased from 0.05 to 0.20 seconds after reducing the caution margin.

## mission_3.limitations

The seven tests show that both robots can respond to different situations. In my tests, both baseline and revised policies passed with a 0% false-safe rate and zero dangerous-command events. However, passing seven simulated scenarios does not prove that the robots will always be safe in real life. Real environments can have unpredictable obstacles that the simulation may not fully be able to handle. A stakeholder to consult would be people who use technology to understand safety concerns as that is the main issue that is being tested with these two robots. I would also conduct real-world tests with unexpected obstacles to further test how these robots react before deployment.
