import numpy as np
import pandas as pd


def indepedence(c):
    if abs(c) <= 0.5:
        return 0
    else:
        return c

def rename_columns(colname):
    return "var" + str(colname)


def multivariate_linear_model(n, m):
    """ simulate a multivariate linear dataset

    Args:
        n (int): number of predictors in the dataset (columns)
        m (int): number of observations in the dataset (rows)

    Returns:
        [type]: [description]
    """

    c = np.random.normal(size=n)
    c = list(map(indepedence, c))
    X = np.random.uniform(size=(m,n))
    b = np.random.normal(size=m)
    y = X.dot(c)+b
    print("underlying process:", c)
    return X, y


def main():
    n = int(input("insert number of predictors: "))
    m = int(input("insert number of observatios: "))
    filename = input("insert filename: ")
    print(n, m)
    X, y = multivariate_linear_model(n, m)
    dat = pd.DataFrame(X)
    dat[n] = y
    dat.columns = list(map(rename_columns, dat.columns))
    dat.to_csv(filename, index=False)

if __name__ == "__main__":
    main()