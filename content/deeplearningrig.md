Title: The Perfect Deep Learning Build
Date: 2017-11-22 13:10
Category: Misc 

## GPU 

The main component of your deep learning rig is the GPU. GPU's enable highly parallelized matrix operations, which are very important for deep learning operations. It would be ideal to have roughly 20GB of GPU memory for larger models that you are trying to run.

The TITAN GeForce is near top of the line for deep learning applications and research. You should have no problem running neural networks at blazing frames per second with these, totaling ~24 GB of GDDR5X RAM. It comes with an incredible 3584 cores per gpu, enabling fast parallelization of linear algebra operations.  

[2 x NVIDIA GeForce TITAN X](https://www.amazon.com/gp/product/B00UXTN5P0?ie=UTF8&tag=deepython-20&camp=1789&linkCode=xm2&creativeASIN=B00UXTN5P0)

On the slightly less expensive side, there is the GTX 1080 Ti. This is based on the new Pascal and has shown to have increased performance and benchmarks for deep learning experiments, often times matching or surpassing the Titan X. However, the catch is that the 1080 Ti only has 11GB of memory compared to the TITAN X's 12GB per GPU. However, I think this is the more cost effective option at the moment, expecially with cryptocurrencies driving up GPU prices.   

[2 x NVIDIA GeForce GTX 1080 Ti](https://www.amazon.com/gp/product/B06Y11DFZ3/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B06Y11DFZ3&linkCode=as2&tag=deepython-20&linkId=26f6f380c0bb7f0e38b68f474080684d)

---
## CPU 

For CPU's you want something that can load and augment data fast, especially if your dataset can't fit in RAM. You don't want your workflows to be hindered and slowed down by the CPU. 

As for CPU, you will want something like an Intel i7 processor. The [Intel i7 4.00 GHz Quad Core Skylake](https://www.amazon.com/gp/product/B012M8LXQW/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B012M8LXQW&linkCode=as2&tag=deepython-20&linkId=9d19f0640aa68ec740ed2435a26e7633) should do a great job at keeping your system fast at preprocessing and augmenting your data on the fly.  

One important thing to remember here is that you want to ensure that you have enough PCIe lanes. As failing to have enough of these in your CPU can be a bottleneck for multi-GPU builds. 

Another good option is the slightly slower [Intel i5 3.50 GHz Skylake](https://www.amazon.com/gp/product/B012M8M7TY/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B012M8M7TY&linkCode=as2&tag=deepython-20&linkId=247dc2b25f648234cd9d2e713560e262)

If you really want to go all out, the [AMD Ryzen Threadripper 1950X](https://www.amazon.com/gp/product/B074CBH3R4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B074CBH3R4&linkCode=as2&tag=deepython-20&linkId=cbedf7505aa01973de832e8dd214f275) is about the best that money can buy currently.


---
## Memory

Here you want sufficient space to keep your small/medium sized datasets in memory, which can help speed things up quite a bit. I've heard good things about this 32GB kit from Ballistix. 

[Ballistics Elite 32Gb DDR4 Kit](https://www.amazon.com/gp/product/B00RCGJPUQ?ie=UTF8&tag=deepython-20&camp=1789&linkCode=xm2&creativeASIN=B00RCGJPUQ)

Here you might even want to opt for two of these, especially if you are doing computer vision related tasks. You can improve training and inference speed by increasing your batch size. To do so takes more RAM typically. 

---
## Storage

Any modern high performance computing environment needs solid state memory. Seriously. If you sum up all the time required to launch IDE's, notebooks, copy and write data, you can save hours of your time by using an SSD. 
I recommend a Samsung Internal SSD.

[Here is the 1TB version](https://www.amazon.com/gp/product/B00LF10KTE/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00LF10KTE&linkCode=as2&tag=deepython-20&linkId=a2653413e75dc4725194d362880c8049)

[Here is a 2TB version](https://www.amazon.com/gp/product/B010QD6RX4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B010QD6RX4&linkCode=as2&tag=deepython-20&linkId=f5ad8802faaaa465193e30fd37c448a7)

---
## General Programming

I do a lot of programming and video editing in my free time. I prefer an operating system that has a linux/unix style command line interface, with high performance while looking good. The [Dell XPS 13 8th Gen](https://www.amazon.com/gp/product/B0762JB7M8/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0762JB7M8&linkCode=as2&tag=deepython-20&linkId=57f22d708469a70964294aeae190da56) fulfills all these needs. It has an infinity edge display with almost no bezels, a solid state hard
drive, 8GB or 16GB of RAM, and the new 8th generation intel CPU. I plan on installing Ubuntu or Debian on the laptop, as it comes with Windows 10 installed. I may have to pounce on this laptop during the holiday season. 

I will be continually adding things here as time goes on and I discover new parts. 

Until next time,
#### Clayton Blythe | *Deep Python*
