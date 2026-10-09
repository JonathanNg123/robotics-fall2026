# Mission 2

## comparison

After comparing the moving average windows of 3, 7, and 11, the RMSE values were 0.1660, 0.1750, and 0.1851 m. Their response delays were 1.30, 1.30, and 1.10 seconds. What we found out was that increasing the window did not necessarily always improve the overall error. After also comparing the moving average and median filters with window 3 and weight of 0.25, I found out that the median had a lower RMSE of 0.1637 m compared to 0.1660 m and a faster response delay of 1.10 seconds compared to 1.30 seconds.

## fusion_choice

After comparing the fusion weights of 0.25, 0.50, and 0.75 with a median filter of 3, their RMSE values were 0.1637, 0.1420, and 0.1454 m, while their response delays were 1.10, 1.05, and 0.80 seconds. I personally selected attemot 6 of 0.75 because it was clear it was the fastest response. Using a median filter helps reduce the effects of outliers on Sensor A while giving it more weight improves the responsiveness.

## manual_average

4.1667 

## manual_fusion

2.25 

## manual_median

2.3 

## prediction_draft

Increasing the weight on Sensor A from 0.50 to 0.75 should make the fused estimate rely more on Sensor A. rather than Sensor B now. I predict that the noise and outliers from Sensor A could increase the overall error.

## responsiveness

Smoothing helps reduce random changes in sensor reading while also delaying the robot's response to changes. In my experiments, the moving averages of window of 3 had a response delay of 1.30 seconds. Compared to the median filter of window of 3 with weight of 0.75, the delay was 0.8 seconds. A longer response delay could cause the robot to see that there is a person nearby too late. This shows why responsiveness is important for safety.

## selected

5
