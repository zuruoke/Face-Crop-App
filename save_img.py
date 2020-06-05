import cv2
from google.colab.patches import cv2_imshow


model_file = "/content/crop_weight.h5"
model = models.load_model(model_file, backbone_name='resnet50')
model = models.convert_model(model)

formatted_data = {
    'image_name': [],
    'x_min': [],
    'y_min': [],
    'x_max': [],
    'y_max': [],
}

def create_df(folder, converted_data, Path):
    for filename in os.listdir(folder):
    
        filepath = Path + filename
        im = cv2.imread(os.path.join(folder,filename))
        if im is not None:
            im = im[:,:,:3]
            imp = preprocess_image(im)
            imp, scale = resize_image(im)
            boxes, scores, labels = model.predict_on_batch(np.expand_dims(imp, axis=0))
            boxes /= scale
            for box, score, label in zip(boxes[0], scores[0], labels[0]):
                if score < 0.5:
                    break
                box = box.astype(np.int32)
                
                converted_data['image_name'].append(filepath)
                converted_data["x_min"].append(box[1])
                converted_data["y_min"].append(box[3])
                converted_data["x_max"].append(box[0])
                converted_data["y_max"].append(box[2])

PATH = '/content/drive/My Drive/Colab Notebooks/'

images = os.path.join(PATH, 'REAL_IMAGES')

create_df(images+"/",formatted_data,'/content/drive/My Drive/Colab Notebooks/REAL_IMAGES/')

df_ = pd.DataFrame(formatted_data)
df_





new_dir = "Images_folder"
os.mkdir(new_dir)
idl = 0
def save_cropped_image(_df):
    global idl
    for i,r in _df.iterrows():
        n =  r["image_name"]
        x1 = r["x_min"]
        x2 = r["y_min"]
        y1 = r["x_max"]
        y2 = r["y_max"]
        im = np.array(Image.open(n))
        new = im[x1:x2, y1:y2]
        f = n.split("/")[-1]
        cv2.imwrite("Images_folder/{}_{}".format(idl,f), new)
        idl +=1

path_2 = '/content/drive/My Drive/Cropped/'

idl = 0
def save_cropped_image(_df):
    global idl
    for i,r in _df.iterrows():
        n =  r["image_name"]
        x1 = r["x_min"]
        x2 = r["y_min"]
        y1 = r["x_max"]
        y2 = r["y_max"]
        im = np.array(Image.open(n))
        new = im[x1:x2, y1:y2]
        f = n.split("/")[-1]
        cv2.imwrite("{}{}_{}".format(path_2,idl,f), new)
        idl +=1

save_cropped_image(df_)

os.listdir("/content/drive/My Drive/Cropped/")

adq = cv2.imread("/content/drive/My Drive/Cropped/447_donald-trump-kim-jong-un.jpg")
adq = cv2.cvtColor(adq, cv2.COLOR_BGR2RGB)

cv2_imshow(adq)
cv2.waitKey(0)
cv2.destroyAllWindows()