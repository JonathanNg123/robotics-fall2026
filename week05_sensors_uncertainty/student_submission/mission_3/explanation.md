# Mission 3

## Assistive.prediction_draft

After changing the caution margin from 0.20 to 0.10, I predict it may reduce unnecessary stops because the robot will have a smaller area where it needs to be cautious. The problem with this is the safety concerns as it is much less safe when a pedestrian suddenly approaches because the robot may react much later than usual. I expect the robot to move more freely, but there may be a tradeoff between safety and convenience.

## Warehouse.prediction_draft



## context_comparison

For the two final policies, both original baseline settings for both robots were better because they had faster detection times. The warehouse policy robot uses a stopping threshold of 0.75 m and a caution margin of 0.10 m, while the assistive robot uses a stopping threshold of 0.95 m and a caution margin of 0.20 m. The main difference is that the assistive robot needs a larger safety distance because it is near people with many different speeds. Both policies use a median filter with a window of 3, but the warehouse robot had a maximum detection delay of 0.15 seconds while the assistive robot had 0.05 seconds. Both had a 0% false-safe rate and zero dangerous-command events. After seeing all these different evidences, it is clear that these robots should be using the settings that match the people and environments around them.

## error_costs

In the warehouse policy, false-safe errors would put many workers at risk of less safety. Unnecessary-stop would slow down work as it would take a lot of time to complete an instruction due to the constant stopping. Both warehouse policies had a 0% false-safe rate and a 3.06% unnecessary-stop rate. The detection delay increased from 0.15 to 0.20 seconds after requiring two readings before stopping. In the the assistive policy, false-safe errors would put pedestrians at risk, while unnecessary stops could make it harder for people to use the robot. Both assistive policies had a 0% false-safe rate and a 2.03% unnecessary-stop rate. However, detection delay increased from 0.05 to 0.20 seconds after reducing the caution margin.

## limitations

The seven tests show that both robots can respond to different situations. In my tests, both baseline and revised policies passed with a 0% false-safe rate and zero dangerous-command events. However, passing seven simulated scenarios does not prove that the robots will always be safe in real life. Real environments can have unpredictable obstacles that the simulation may not fully be able to handle. A stakeholder to consult would be people who use technology to understand safety concerns as that is the main issue that is being tested with these two robots. I would also conduct real-world tests with unexpected obstacles to further test how these robots react before deployment.
