## Offline trainning model:
Used 500 news with labeled topic to train the model, format:
```
[class_topic], [new_title], [news_description], [news_source]
```

### Vocabularay embedding
```
embedding : Tensorflow cannot handle string, so we need to convert str to vectors(array)
Tensorflow have Vocabulary Processor to do this

1. convert each word in sentence to vector
I like apple
I like banana
I eat apple
[1 2 3]
[1 2 4]
[1 5 3]

2. convert each char in word to vector
I like apple
[1 2 3 0 0]
to
[0, 1, 0, 0, 0] I
[0, 0, 1, 0, 0] Like 
[0, 0, 0, 1, 0] Apple
[1, 0, 0, 0, 0] padding
[1, 0, 0, 0, 0] padding
```

### CNN Convolutional neural networks
```
Convolutional
[0.27164... -0.0600.....]
....
Pooling (sample采样)
1 1 2 4
5 6 7 8                 6 8
3 2 1 0   -> max pool   3 4 
1 2 3 4

then map to the topic of classes
```