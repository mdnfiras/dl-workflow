import pandas
import tensorflow
import keras

print("Running...")

!if [[ ! -d report ]]; then mkdir report ; fi
!echo GG > report/metrics.txt
!wget https://thumbs.dreamstime.com/b/card-minimal-cartoonish-style-vector-templates-nice-job-lettering-speech-bubble-89326194.jpg -P report