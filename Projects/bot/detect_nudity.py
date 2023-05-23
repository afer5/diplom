from nudenet import NudeClassifier


def detect_nude_photo(photo):
    c = NudeClassifier()
    data = c.classify(photo)
    if data[photo]['safe'] < 0.9:
        return 1  # nude
    else:
        return 0  # not nude


def detect_nude_video(video):
    c = NudeClassifier()
    data = c.classify_video(video)
    unsafe_sum = 0.0
    for key, value in data['preds'].items():
        unsafe_sum += value['unsafe']
    unsafe_count = sum(1 for value in data['preds'].values() if value['unsafe'])
    if unsafe_sum / unsafe_count < 0.21:
        return (0)  # safe
    else:
        return (1)  # unsafe

#%%
