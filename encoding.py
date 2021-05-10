import category_encoder as ce


ce.TargetEncoder()# Target encoding. Encode each cateogry of categorical variable with  target mean


ce.CountEncoder()# Encodes based on the size of the category [12, 8, 4]
#normalise = true -> [0.5, 0.3, 0.2]

encoder = ce.BackwardDifferenceEncoder(cols=[...])
encoder = ce.BaseNEncoder(cols=[...])
encoder = ce.BinaryEncoder(cols=[...])
encoder = ce.CatBoostEncoder(cols=[...])
encoder = ce.CountEncoder(cols=[...])
encoder = ce.GLMMEncoder(cols=[...])
encoder = ce.HashingEncoder(cols=[...])
encoder = ce.HelmertEncoder(cols=[...])
encoder = ce.JamesSteinEncoder(cols=[...])
encoder = ce.LeaveOneOutEncoder(cols=[...])
encoder = ce.MEstimateEncoder(cols=[...])
encoder = ce.OneHotEncoder(cols=[...]) ### For multiplicative
encoder = ce.OrdinalEncoder(cols=[...]) ### For Trees
encoder = ce.SumEncoder(cols=[...])
encoder = ce.PolynomialEncoder(cols=[...])
encoder = ce.TargetEncoder(cols=[...])# Target encoding. Encode each cateogry of categorical variable with  target mean
#smoothing= 1 helps to avoid dataleaks
encoder = ce.WOEEncoder(cols=[...])
