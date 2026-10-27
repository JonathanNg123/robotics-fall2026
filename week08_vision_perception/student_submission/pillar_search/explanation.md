# pillar_search

## diagnosis
In my saved blue-only attempt (20261027T055019-77eef8f8), the controller detected and centered the blue pillar. The camera showed the blue pillar while the color mask just showed a white area. The controller used the centroid marker to compare the pillar's position with the center of the image. No setting was changed.

## evidence
In my four-color attempt (20261027T055424-e5479a3b), the robot centered all four pillars in the order red, green, turquoise, and blue. The camera images and color masks showed me how the controller saw the colored regions and used the centroids to adjust its turning direction. However, centering a colored region doesn't mean that that is the correct object. Another object with a similar color could produce the same detection. Additional sensors or information would be needed to estimate distance better.
