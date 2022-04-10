# Python-Blur-Metric
This is python code for Blur Metric from A No-Reference Perceptual Blur Metric conference paper

Marziliano, Pina & Dufaux, Frederic & Winkler, Stefan & Ebrahimi, Touradj. (2002). A No-Reference Perceptual Blur Metric. International Conference on Image Processing, Rochester, NY. 53. III-57 . 10.1109/ICIP.2002.1038902. 

created by
- Dr (c). Sandy Suryo Prayogo, S.T., M.T.
- Affa Alfiandy

# How?
This function only need your image path, or you can change inside the function if you want to customize.

### Short explanation about how this algorithm works
- This code will open your image with CV2 library
- Then image will convert to gray with RGB2GRAY Matlab format ITU-R
- Blur the image with GaussianBlur then edge detection with sobel filter
- Check pixel by pixel in column for horizontal blur analysis and row for vertical blur analysis
- Get total blur by adding horizontal blur with vertical blur then divided by 2

Or you can read the paper for more explanation

# Example
## Blur Image
<br/>
<img src="https://images.unsplash.com/photo-1523821741446-edb2b68bb7a0?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8Ymx1cnxlbnwwfHwwfHw%3D&w=1000&q=80" width="500">
<br/>
Result
<br/>
<img src="Screenshot (964).png" width="500">

## 4K Image
<br/>
<img src="https://www.pixelstalk.net/wp-content/uploads/2016/07/4k-Images-Free-Download.jpg" width="500">
<br/>
Result
<br/>
<img src="Screenshot (965).png" width="500">

