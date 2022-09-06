Clothes image generation using GAN(Generative Adversarial Network), to be more specific, DCGAN (Deep Convolutional Generative Adversarial Network).

## Result
it's more like clothes from trash can 🤣

<img src="logs/intermediate_training_images/epoch45_iter80.png">

<br>

## Real Colthes Images
<img src="logs/real_images.png">

### Image Acquisition

Total **~3000** real clothes images are from various clothing brands' online shop or e-commerces such as ZARA, Lativ, REVOLVE, Beams ... and so on.

All images were scraped using Chrome extension `Image downloader` for batch downlaoding images from webpages. Then select and collect manually.

It's worth noticing that we only use image with **white background** and **without model**.

<img width="250" alt="Screen Shot 2022-09-05 at 11 56 43 PM" src="https://user-images.githubusercontent.com/75982405/188485544-07ea1c20-df28-4f68-ac68-ef63faaf7716.png">

### Image pre-processing
There exist some problem in the collected image

1. object (cloth) is not at the center of image
    
    <img width="150" alt="Screen Shot 2022-09-06 at 11 34 11 AM" src="https://user-images.githubusercontent.com/75982405/188541571-1b6111f6-d7d6-44d6-b05b-5bcc31a50195.png">


2. size of white padding between object and border is different amoung different source website.

    <img width="150" alt="Screen Shot 2022-09-06 at 11 14 54 AM" src="https://user-images.githubusercontent.com/75982405/188539552-01a63db2-bfe2-411f-a9de-e45c56fa59ac.png">
    <img width="150" alt="Screen Shot 2022-09-06 at 11 16 04 AM" src="https://user-images.githubusercontent.com/75982405/188539651-80a136a4-d6e8-4e91-a046-d58b834c45a0.png">
    
To deal with this problem, we use a pre-process step to make sure object is at the center and the size of white padding is the same:

1. turn image into grey scale and remove white background (250 - 255)
2. find object's contour
3. crop image with the border of contour
4. extend the border to make sure every side is 1.2 * (max border side) -> this can make image square
( step 1-3 is from [reference 3] )

|before|after|
|------|-----|
|<img width="150" alt="Screen Shot 2022-09-06 at 11 34 11 AM" src="https://user-images.githubusercontent.com/75982405/188541571-1b6111f6-d7d6-44d6-b05b-5bcc31a50195.png">|<img width="150" alt="Screen Shot 2022-09-06 at 11 35 26 AM" src="https://user-images.githubusercontent.com/75982405/188541710-68746dc3-4043-47b5-8251-d5281a2f86be.png">|
|<img width="150" alt="Screen Shot 2022-09-06 at 11 14 54 AM" src="https://user-images.githubusercontent.com/75982405/188539552-01a63db2-bfe2-411f-a9de-e45c56fa59ac.png">|<img width="150" alt="Screen Shot 2022-09-06 at 11 28 18 AM" src="https://user-images.githubusercontent.com/75982405/188541027-06c33b66-a2ee-44ba-9efc-11d4a0c3469c.png">
|<img width="150" alt="Screen Shot 2022-09-06 at 11 16 04 AM" src="https://user-images.githubusercontent.com/75982405/188539651-80a136a4-d6e8-4e91-a046-d58b834c45a0.png">|<img width="150" alt="Screen Shot 2022-09-06 at 11 29 58 AM" src="https://user-images.githubusercontent.com/75982405/188541163-d2e37a85-6537-412a-b903-4168aa8c9c00.png">|

### Image processing before entering GAN
target image size will be square `64*64`

<br>

## Model Architecture

### Generator

### Discriminator

<br>

## Reference
1. [Pytorch DCGAN tutorial](https://pytorch.org/tutorials/beginner/dcgan_faces_tutorial.html)
2. [【機器學習2021】生成式對抗網路 (Generative Adversarial Network, GAN) (二) – 理論介紹與WGAN](https://www.youtube.com/watch?v=jNY1WBb8l4U&list=PLJV_el3uVTsMhtt7_Y6sgTHGHp1Vb2P2J&index=15)
3. [Stack Overflow - How to crop or remove white background from an image](https://stackoverflow.com/questions/48395434/how-to-crop-or-remove-white-background-from-an-image)
