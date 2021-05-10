from sklearn.cluster            import KMeans
from sklearn.neighbors          import KNeighborsClassifier
from sklearn.naive_bayes        import GaussianNB, MultinomialNB
from sklearn.model_selection    import cross_val_score, ShuffleSplit, GridSearchCV, train_test_split, StratifiedKFold, cross_val_predict
from sklearn                    import pipeline
from sklearn.tree               import DecisionTreeClassifier
from sklearn.experimental       import enable_hist_gradient_boosting # for HistGradientBoostingClassifier
from sklearn.ensemble           import RandomForestClassifier, ExtraTreesClassifier, AdaBoostClassifier, GradientBoostingClassifier, HistGradientBoostingClassifier
from xgboost                    import XGBClassifier
from lightgbm                   import LGBMClassifier
from catboost                   import CatBoostClassifier


mult_classifiers = {
        "LM Linear Regression": LinearRegression(), # not useful for classification on titanic
        "LM Logistic Regression": LogisticRegression(),
        "LM Ridge": RidgeClassifier(),
        "LM Lasso": Lasso(), Not useful for titanic dataset
        "NN Multi layer Perceptron": MLPClassifier(random_state=909),
        "SVM Linear": svm.SVC(kernel='linear'),
        "SVM RBF": svm.SVC(kernel='rbf'),
        "KNN": KNeighborsClassifier(),
        "BM Guassian Naive Bayes": GaussianNB(),
        "BM Multinominal Naive Bayes":MultinomialNB(),

}

tree_classifiers = {
        "Decision Tree": DecisionTreeClassifier(),
        "Extra Trees":ExtraTreesClassifier(),
        "Random Forest":RandomForestClassifier(),
        "AdaBoost":AdaBoostClassifier(),
        "Skl GBM":GradientBoostingClassifier(),
        "Skl HistGBM":HistGradientBoostingClassifier(),
        "XGBoost":XGBClassifier(use_label_encoder=False),
        "LightGBM":LGBMClassifier(),
        "CatBoost":CatBoostClassifier()
        }
