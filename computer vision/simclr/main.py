import tensorflow as tf
from tensorflow.keras import layers
import tensorflow_datasets as tfds
import numpy as np

# Load the dataset
(train_ds,test_ds),ds_info = tfds.load('cifar10',split=["train","test"],as_supervised=True,with_info=True)

# Initial params
IMG_SIZE = 32
BATCH_SIZE = 256
projection_dim = 128
temperatures = 0.5
EPOCHS = 20

# DataAugmentation
DataAugmentation = tf.keras.Sequential(
    [
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.2),
        layers.RandomContrast(0.2),
        layers.RandomCrop(IMG_SIZE,IMG_SIZE)
    ]
)

# Preprocess the img
def preprocess(image,label):
    image = tf.cast(image,tf.float32)/255.0
    return image,label

#prepare the dataset
train_ds = train_ds.map(preprocess).shuffle(10000).batch(BATCH_SIZE).prefetch(tf.data.AUTOTUNE)

# Encoder
baseEncoder = tf.keras.applications.ResNet50(
    include_top = False,
    weights = None,
    input_shape = (IMG_SIZE,IMG_SIZE),
    pooling = 'avg'
)

# ProjectionHead
def build_projection_head(encoder,projection_dims:int):

    inputs  = layers.Input(shape = (IMG_SIZE,IMG_SIZE,3))
    features = encoder(inputs)
    x = layers.Dense(512,activation='relu')(features)
    outputs = layers.Dense(projection_dims)(x)
    model = tf.keras.Model(inputs,outputs)
    return model

encoder_model = build_projection_head(baseEncoder,projection_dim)

# Contrastive Loss
def contrastive_loss(features,temperature:float):
    features = tf.math.l2_normalize(features,axis=1)
    similarities = tf.matmul(features,features,transpose_b=True) /temperature
    labels = tf.range(tf.shape(features)[0])
    loss = tf.keras.losses.sparse_categorical_crossentropy(labels,similarities,from_logits=True)
    return tf.reduce_mean(loss)

optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)


# train
@tf.function
def train_step(image):
    with tf.GradientTape as tape:

        augmented1 = DataAugmentation(image)
        augmented2 = DataAugmentation(image)

        projection1 = encoder_model(augmented1,training=True)
        projection2 = encoder_model(augmented2, training=True)

        projections = tf.concat([projection1,projection2],axis=0)


        losses = contrastive_loss(projections,temperatures)

        gradients = tape.gradient(losses,encoder_model.trainable_variables)
        optimizer.apply_gradients(zip(gradients,encoder_model.trainable_variables))

        return losses


# training loop

for epoch in range(1,EPOCHS+1):
    total_loss = 0
    num_batches = 0
    for images,_ in train_ds:
        loss = train_step(images)
        total_loss += loss
        num_batches +=1
    print(f"Epoch {epoch}, Loss:{total_loss/num_batches:.4f}")
print("Training Finished")


