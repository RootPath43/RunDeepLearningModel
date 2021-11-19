# RunDeepLearningModel
The logic of this:Let's supposed your computer doesn't have enough proccessing power to train a  deep learning model.That's where this thing works.You just upload your dataset and choose deep learning model to train. Every train button click put you into redis q and your data and model pullout from sql. 
So it trains itself.
Backend side of a deep learning server. It uses redis, redis queue, flask(API), postgresql
