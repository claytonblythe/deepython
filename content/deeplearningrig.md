Title: The Perfect Deep Learning Build
Date: 2017-11-22 13:10
Category: Misc 

## GPU 

The main component of your deep learning rig is the GPU. GPU's enable highly parallelized matrix operations, which are very important for deep learning operations. It would be ideal to have roughly 20GB of GPU memory for larger models that you are trying to run.

The TITAN GeForce is near top of the line for deep learning applications and research. You should have no problem running neural networks at blazing frames per second with these, totaling ~24 GB of GDDR5X RAM. It comes with an incredible 3584 cores per gpu, enabling fast parallelization of linear algebra operations.  

[2 x NVIDIA GeForce TITAN X](https://www.amazon.com/gp/product/B00UXTN5P0?ie=UTF8&tag=deepython-20&camp=1789&linkCode=xm2&creativeASIN=B00UXTN5P0)

On the slightly less expensive side, there is the GTX 1080. This is based on the new Pascal and has shown to have increased performance and benchmarks for deep learning experiments. However, the catch is that the 1080 only has 8GB of RAM compared to the TITAN X's 12GB per GPU.  

[2 x NVIDIA GeForce GTX 1080 Ti](https://www.amazon.com/gp/product/B06Y11DFZ3/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B06Y11DFZ3&linkCode=as2&tag=deepython-20&linkId=26f6f380c0bb7f0e38b68f474080684d)

---
## CPU 

For CPU's you want something that can load and augment data fast, especially if your dataset can't fit in RAM. You don't want your workflows to be hindered and slowed down by the CPU. 

As for CPU, you will want something like an Intel i7 processor. The [Intel i7 4.00 GHz Quad Core Skylake](https://www.amazon.com/gp/product/B012M8LXQW/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B012M8LXQW&linkCode=as2&tag=deepython-20&linkId=9d19f0640aa68ec740ed2435a26e7633) should do a great job at keeping your system fast at preprocessing and augmenting your data on the fly.  

One important thing to remember here is that you want to ensure that you have enough PCIe lanes. As failing to have enough of these in your CPU can be a bottleneck for multi-GPU builds. 

Another good option is the slightly slower [Intel i5 3.50 GHz Skylake](https://www.amazon.com/gp/product/B012M8M7TY/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B012M8M7TY&linkCode=as2&tag=deepython-20&linkId=247dc2b25f648234cd9d2e713560e262)

---
## Memory

Here you want sufficient space to keep your small/medium sized datasets in memory, which can help speed things up quite a bit. I've heard good things about this 32GB kit from Ballistix. 

[Ballistics Elite 32Gb DDR4 Kit](https://www.amazon.com/gp/product/B00RCGJPUQ?ie=UTF8&tag=deepython-20&camp=1789&linkCode=xm2&creativeASIN=B00RCGJPUQ)

---
## Storage

Any modern high performance computing environment needs solid state memory. Seriously. If you sum up all the time required to launch IDE's, notebooks, copy and write data, you can save hours of your time by using an SSD. 
I recommend a Samsung Internal SSD.

[Here is the 1TB version](https://www.amazon.com/gp/product/B00LF10KTE/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00LF10KTE&linkCode=as2&tag=deepython-20&linkId=a2653413e75dc4725194d362880c8049)

[Here is a 2TB version](https://www.amazon.com/gp/product/B010QD6RX4/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B010QD6RX4&linkCode=as2&tag=deepython-20&linkId=f5ad8802faaaa465193e30fd37c448a7)

I will be updating this more yet, but the GPU, CPU, and SSD are core parts of the build you want.

Until next time,
#### Clayton Blythe | *Deep Python*
