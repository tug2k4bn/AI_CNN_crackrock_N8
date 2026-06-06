import tensorflow as tf
import numpy as np




class LeNetRockModel:
    def __init__(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(filters=6, kernel_size=(5, 5), activation='relu', input_shape=(150, 150, 3)),
            tf.keras.layers.AvgPool2D(pool_size=(2, 2), strides=2),
            tf.keras.layers.Conv2D(filters=16, kernel_size=(5, 5), activation='relu'),
            tf.keras.layers.AvgPool2D(pool_size=(2, 2), strides=2),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(units=120, activation='relu'),
            tf.keras.layers.Dense(units=84, activation='relu'),
            tf.keras.layers.Dense(units=1, activation='sigmoid')
        ])
        print(self.model.summary())
        weights_path = r"app\model\weights\lenet_concrete_crack.weights.h5"
        try:
            self.model.load_weights( weights_path )
            print(f"[INFO] Load weights thành công từ: {weights_path}")
        except Exception as e: 
            print(f"[ERROR] Không thể load weights từ '{weights_path}'. Chi tiết lỗi:")
            print(e)
            
        
    def predict(self, img: np.ndarray): #TODO: Unknown logic
        # weight = keras.lenet_rock_model.load_model ()
        """
        Dự đoán nhãn cho ảnh đầu vào.
        img: numpy array shape (1, IMG_SIZE_LENET_ROCK, IMG_SIZE_LENET_ROCK, 3)
        """
        
        
        preds = self.model.predict(img)
        print (preds)
        # Nếu là binary classification, trả về 0 hoặc 1
        return (preds > 0.5).astype(int) 



lenet_rock_model = LeNetRockModel()
