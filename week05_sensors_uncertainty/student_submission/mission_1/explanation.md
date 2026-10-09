# Mission 1

## bias

-0.01097

## bias_vs_variance

My prediction was mostly similar to the actual statistics because the mean I had calculated was close to 2.00 m, but was slightly off due to some extreme readings. Bias measures how far the average is from the true distance, while variance measures how spread out the readings are. 

## dropouts

3

## mean

1.989

## median

2.0

## more_samples

More samples would help, but would not remove the main problems completely. The samples could help make a better stable average, but they would not prevent the sensor from occasionally producing extreme measurements. From my evidence, there were four outliers which will always happen. 

## outliers

4

## prediction

I predict that for a biased sensor, we will have a mean that is mostly always above or below the true distance which will result in a bigger bias, but low variance.  A noisy sensor will have readings that are more spread out which results in a higher variance, but would mostly be closer to the true distance with little bias.

## prediction_draft

I predict that for a biased sensor, we will have a mean that is mostly always above or below the true distance which will result in a bigger bias, but low variance.  A noisy sensor will have readings that are more spread out which results in a higher variance, but would mostly be closer to the true distance with little bias.

## profile

quantized

## robot_consequence

If a robot is moving and approaches a pedestrian, if  the actual distance is 2.00 m but an outlier reports 2.90 m, the robot might incorrectly believe it has more room to move forward. This is clearly a problem as safetly is in play now. The robot should check these unusual measurements before making important movement decisions.

## variance

0.010218
