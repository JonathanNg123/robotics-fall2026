# mission_1

## diagnosis
The two images I compared was `normal_1` and `dim_1. In `normal_1`, the detector was able to see that the cup was there, but the green bounding box also included some of the desk. The threshold mask also shows some unwanted areas from the laptop and other objects. In `dim_1`, the lighting appeared to be darker, but the detector still included some parts of the mug and surrounding background. The settings that I used were the ones recommended which  allowed other objects with similar colors to pass the filter. This also shows that these settings used were detecting the presence of a mug, but not necessarily being able to locate it accurately.

## limitations
One parameter I changed during practice was thhe brightness. Lowering the minimum brightness made it so darker pixels passed through the color filter. Just like the images that were compared, this helped detect the mug in darker lighting, but it could also included more area around that we did not need. A limitation could be that objects can have similar colors to the mug. This means that changing brightness is not enough as the detector might not give an accurate image due to similar colors.
