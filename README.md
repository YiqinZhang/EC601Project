# EC601Project1 - Building 3D scenes from 2D images

## 1. Introduction

Creating realistic 3D scenes from 2D images is a fundamental problem in image-based modeling and computer vision. 3D reconstruction, the creation of three-dimensional models from a set of images, is the reverse process of obtaining 2D images from 3D scenes. 2D images do not give us enough information to reconstruct a 3D scene because image points are the actual objects' projections on a 2D plan without depth. 
3D reconstruction technology is becoming increasingly prevalent in games, movies, mapping, positioning, navigation, autonomous driving, VR / AR, and industrial manufacturing. Therefore, real-time 3D reconstruction is an inevitable trend to achieve better interaction and perception. 
Computer vision is moving towards integrating 3D reconstruction and recognition. Therefore, building 3D scenes from 2D images is an essential problem in computer vision and other imaging applications.

## 2. Related Work

### 2.1 Traditional approach

**(1) Monocular vision geometry**

Monocular vision only uses a single camera as a collection device, which has the advantages of low cost and easy deployment. It relies on the parallax of continuous images obtained over a while to reconstruct a three-dimensional environment. Nevertheless, there is a problem using the monocular vision method to estimate the depth from the image and achieve 3D reconstruction. A single image may correspond to countless natural physical world scenes (morbidity).
At present, this algorithm is widely applicable in mobile devices such as mobile phones, and algorithms include SFM, REMODE, and SVO.
SFM, recovering structure of 3D from the camera motion, is one of the means to solve the 3D modeling in the field of computer graphics and computer vision.

Andrew Davison [2] presented a general method for real-time, vision-only single-camera simultaneous localization and mapping (SLAM) - an algorithm that applies to the localization of any camera moving through a scene - and studied its application to the localization of a wearable robot with active vision. He utilizes a single-view camera as well as geometric information to present the method of Visual SLAM.

Ashutosh Saxena el. [3]  Present a Markov Random Field (MRF) method to infer a set of "plane parameters" that capture both the 3D location and 3D orientation of the patch.

In CVPR 2019 best paper, Shumian Xin's team present a novel theory of Fermat paths of light between a known visible scene and an unknown object not in the line of sight of a transient camera. Based on this theory, they present an algorithm called Fermat Flow to estimate the non-line-of-sight object's shape. Their method allows accurate shape recovery of complex objects, ranging from diffuse to specular, hidden around the corner and hidden behind a diffuser. 

**(2) Binocular / multi-eye vision geometry**

Binocular vision mainly uses the two corrected images obtained by the left and right cameras to find the matching points of the left and right pictures and then recover the three-dimensional information of the environment according to the geometric principle. However, the difficulty of this method is the matching of the left and right camera pictures, and the inaccurate matching will affect the final algorithm imaging effect. Multi-eye vision uses three or more cameras to improve the matching accuracy. However, the disadvantages are also apparent. It takes much time, and the real-time performance is not good.
Both methods can theoretically recover the depth information more accurately, but the shooting conditions often do not guarantee accuracy. The common ones are SGM and SGBM algorithms. Among the automatic driving data set KITTI, almost half of the top 50 algorithms are improvements to SGM.

ShapeNet: In [13], Wu presented a model, 3D ShapeNets, learns the distribution of complex 3D shapes
across different object categories and arbitrary poses from raw CAD data, automatically discovering hierarchical compositional part representations. It naturally supports joint object recognition and shapes completion from 2.5D depth maps, enabling active object recognition through view planning. To train their 3D deep learning model, they construct ModelNet - a large-scale 3D CAD model dataset. Extensive experiments show that our 3D deep representation enables significant performance improvement over the state-of-arts in various tasks. It is a famous work to push people to research 3D reconstruction methods using deep net architecture. 

**(3) Based on consumer-grade RGB-D cameras**

There has been much research on 3D reconstruction based directly on consumer-grade RGB-D cameras in the recent decade. For example, Microsoft's Kinect V1 and V2 products have achieved good results. The earliest, Kinect Fusion[7], proposed by Newcombe et al. Of the Imperial College of Technology in 2011, realized the real-time rigid body reconstruction based on cheap consumer cameras for the first time, without the RGB map but only the depth map. Thus, it significantly promoted the commercialization of real-time dense 3D reconstruction. Since then, there have been algorithms such as Dynamic Fusion and Bundle Fusion.

### 2.2 Deep learning

### (1)Integrate deep learning methods to improve the traditional 3D reconstruction algorithm 

Since CNN has a considerable advantage in image feature matching, there is much research in this area.
DeepVO is based on deep recursive convolutional neural network (RCNN) to infer posture directly from a series of original RGB images (video), without using any module in the traditional visual odometer, improving the visual odometer in 3D reconstruction ring.
BA-Net uses the Bundle Adjustment (BA) optimization algorithm in the SfM algorithm as a neural network layer to train a better basis function generation network, thereby simplifying the back-end optimization process in reconstruction.
Code SLAM extracts several essential functions through the neural network to represent the depth of the scene. These basis functions can simplify the optimization problem of traditional geometric methods.
CNN-SLAM13 fuses the dense depth map predicted by CNN and the result of monocular SLAM. When the monocular SLAM is close to the failed image position, such as a low-texture area, its fusion scheme gives more weight to the depth scheme, which improves the reconstruction effect.

### (2) Deep learning algorithms for 3D reconstruction

There are four main types of data formats in 3D reconstruction: Depth map, voxel, point cloud, mesh.

**(A) Depth Map**

A depth map is 2D pictures or image channels that contain the distance from the viewpoint to the surfaces of objects, expressed in grayscale: the closer, the darker.

David Eigen's team[4] presented a method that addresses this task by employing two deep network stacks: one that makes a coarse global prediction based on the entire image and another that refines this prediction locally. They also apply a scale-invariant error to help measure depth relations rather than scale. By leveraging the raw datasets as significant sources of training data, Their method achieves state-of-the-art results on both NYU Depth and KITTI. Furthermore, it matches clear depth boundaries without the need for super pixelation.

**(B) Voxel**

Voxels, as the simplest form, perform the easiest 3D reconstruction by expanding 2D convolution to 3D.
Depth Map Prediction from a Single Image using a Multi-Scale Deep Network, 2014 This method is a pioneering work of 3D reconstruction using deep learning. The voxel form uses a single image to use a neural network to restore the depth map method directly. The network is divided into global rough and local fine estimation and uses a scale-invariant loss function for regression.
3D-R2N2: A unified approach for single and multi-view 3d object reconstruction, 2016 
Christopher et al. introduced the 3D-R2N2 model based on voxel form. They used the network structure of Encoder-3DLSTM-Decoder to establish the mapping of 2D graphics to 3D voxel models, completing the single-view / multi-view three-dimensional reconstruction based on voxels. The multi-view figures will be input as a sequence into the LSTM, and multiple results will be output.
However, there is a problem with this voxel-based method. Increasing accuracy need to increase the resolution, and the increase in resolution will significantly increase the calculation time (3D convolution, cubic power calculation).
Algorithms based on voxel are computationally intensive, and resolution and accuracy are difficult to balance.

**(C) Point cloud**

Each dot contains three-dimensional coordinates and even color, reflection intensity information. The point cloud is easier to operate during geometric transformation and deformation because its connectivity is not updated. 
A Point Set Generation Network for 3D Object Reconstruction From a Single Image, 2017.
It solves the loss problem when training point cloud networks. However, because different point clouds may represent the same geometry to the same degree of approximation, employing appropriate loss function to measure is always a problem of 3D reconstruction method based on the point cloud.
Point-Based Multi-View Stereo Network, 2019. This method improves the accuracy of point cloud reconstruction by processing the point cloud of the scene and fusing 3D depth and 2D texture information.
However, one disadvantage of point cloud algorithms is the lack of connectivity between the points in the point cloud. Therefore the surface of the object is not smooth after reconstruction.

**(D)Mesh**

The mesh representation method has the characteristics of lightweight and rich shape details. The important thing is that there is a connection relationship between adjacent points. Therefore, the researchers do 3D reconstruction based on the grid. We know that vertices, edges, and faces describe the mesh, corresponding to the graph convolutional neural network's M = (V, E, F).

Pixel2Mesh. They use triangle mesh to do 3D reconstruction of a single RGB image. First, for any input image, initialize an ellipsoid as the initial three-dimensional shape. Then, the network is divided into two parts. One uses a fully convolutional neural network to extract the input image's features; the other uses a convolutional graph network to represent the 3D grid structure. Next, continuously deform the 3D mesh, and finally output the shape of the object.

The model uses four loss functions to constrain the shape and achieves good results. The contribution is that the end-to-end neural network is used to directly generate the three-dimensional information of the object represented by the grid from a single color map.



## References
[1]David Kim, Otmar Hilliges, Pushmeet Kohli. KinectFusion: Real-time 3D Reconstruction and Interaction Using a Moving Depth Camera[C]. ISMAR, 2011.

[2]A. J. Davison, W. W. Mayol, and D. W. Murray. Real-time localization and mapping with wearable active vision. In The Second IEEE and ACM International Symposium on Mixed and Augmented Reality, 2003. Proceedings., pages 18–27. IEEE, 2003.

[3] A. Saxena, M. Sun, and A. Y. Ng. Make3d: Learning 3d scene structure from a single still image. IEEE transactions on pattern analysis and machine intelligence, 31(5):824–840, 2008.

[4] D. Eigen, C. Puhrsch, and R. Fergus. Depth map prediction from a single image using a multi-scale deep network. In Advances in neural information processing systems, pages 2366–2374, 2014.
