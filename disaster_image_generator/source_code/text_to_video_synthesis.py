# -*- coding: utf-8 -*-
"""text-to-video-synthesis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uW1ZqswkQ9Z9bp5Nbo5z59cAn7I0hE6R
"""

!nvidia-smi

!pip install modelscope==1.4.2
!pip install open_clip_torch
!pip install pytorch-lightning

from modelscope.pipelines import pipeline
from modelscope.outputs import OutputKeys

p = pipeline('text-to-video-synthesis', 'damo/text-to-video-synthesis')
test_text = {
        'text': 'A panda eating bamboo on a rock.',
    }
output_video_path = p(test_text,)[OutputKeys.OUTPUT_VIDEO]
print('output_video_path:', output_video_path)

# Download result
from google.colab import files
files.download(output_video_path)

"""The above code will display the save path of the output mp4 video, and the current encoding format can be played normally with [VLC player](https://www.videolan.org/vlc/). Some other media players may not view it normally."""