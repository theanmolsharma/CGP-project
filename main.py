from map import process
from stft import convertMappingToSTFT
from sklearn.model_selection import train_test_split

def main():
    # Load data and labels
    # Process data
    cancerous = 13
    noncancerous = 12
    x = []
    y = []
    for i in range(1, cancerous + 1):
        path = 'dataset/cancerous/' + str(i)
        arr = process(path)
        x.append(convertMappingToSTFT(arr))
        y.append(1)
    for i in range(1, noncancerous + 1):
        path = 'dataset/noncancerous/' + str(i)
        arr = process(path)
        x.append(convertMappingToSTFT(arr))
        y.append(0)

    # split data into training and testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
    from sklearn.preprocessing import StandardScaler
    st_x = StandardScaler()
    x_train = st_x.fit_transform(x_train)
    x_test = st_x.transform(x_test)

    # train model
    from sklearn.neighbors import KNeighborsClassifier
    classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2)
    classifier.fit(x_train, y_train)

    # predict test set results
    y_pred = classifier.predict(x_test)
    from sklearn.metrics import confusion_matrix

    # evaluate model
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    from sklearn.metrics import accuracy_score
    print(accuracy_score(y_test, y_pred) * 100)


if __name__ == '__main__':
    main()