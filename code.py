from sklearn import tree

''' this will predict gender based on 3 parameters: height, weight and shoe size
your input should go directly to the prediction (line 8)''' 

x = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [190, 89,45], [200, 105, 50], [155, 45,36]]
y = ['male', 'female', 'female', 'male','male','female']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)
lst = ['none'] *3
lst[0]= int(input('Enter your height:'))
lst[1]= int(input('Enter your weight:'))
lst[2]= int(input('Enter your shoesize:'))
prediction = clf.predict([lst])
print (prediction)
