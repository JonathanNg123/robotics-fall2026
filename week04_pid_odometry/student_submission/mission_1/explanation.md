# mission_1 Submission

- Name: (not provided)
- Section: (not provided)

## Explanations

### prediction

With too little Kp, the arms should move too slowly and weak reaching the target. Too little Kd would overshoot the arms over the target and oscillate back and forth.

### tuning_analysis

I predicted that too little Kp would make the arm be too weak and have trouble reaching the target while too little Kd would cause more overshoot and wild adjustments. I adjusted the shoulder and elbow PID controllers using the tuned/stiff settings. Adding gravity comp also allowed the arm to support its weight.