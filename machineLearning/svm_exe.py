from cvxopt.solvers import qp
from cvxopt.base import matrix
import numpy as np
import pylab, random, math


classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + \
            [(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]
classB = [(random.normalvariate(0.0, 0.5), random. normalvariate(-0.5, 0.5), -1.0) for i in range(10)]
data = classA + classB
random. shuffle(data)


def polynomial_kernel(x, y, power=3):
    return (1 + np.dot(x, y)) ** power


def call_qp(P, q, G, h):
    r = qp(P, q, G, h)
    alpha = list(r['x'])
    return alpha


def train():

    G = matrix(-np.identity(20))  # -1, 20x20
    h = matrix(np.zeros(20))
    q = matrix(-np.ones((20, 1)))
    P = matrix([[x[2]*y[2]*polynomial_kernel(x[:2], y[:2]) for x in data] for y in data])

    alpha_list = call_qp(P, q, G, h)
    return zip(alpha_list, data)


def get_non_zeros(alpha_list, thresh_hold=0.00001):
    alphas = filter(lambda (alpha, point): alpha > thresh_hold, alpha_list)

    with open("output_alpha.txt", 'w') as f:
        f.write("\n".join(map(lambda (alpha, point): "%s, (%s, %s, %s)" % (alpha, point[0], point[1], point[2]), alphas)))

    return alphas


def notes():
    a = np.ones((2, 3), dtype=int)
    a = np.array([20, 30, 40, 50])


def plot_data(classA, classB):
    pylab.hold(True)
    pylab.plot([p[0] for p in classA],
               [p[1] for p in classA],
               'bo')
    pylab.plot([p[0] for p in classB],
               [p[1] for p in classB],
               'ro')
    pylab.show()


# plot_data(classA, classB)


def plot_boundary():
    xrange = np.arange(-4, 4, 0.05)
    yrange = np.arange(-4, 4, 0.05)

    grid = matrix([[indicator(x, y) for y in yrange] for x in xrange])

    pylab.contour(xrange, yrange, grid,
                  (-1.0, 0.0, 1.0),
                  colors=('red', 'black', 'blue'),
                  linewidths=(1, 3, 1))


def indicator(test_point, model):
    value = sum(alpha * point[2] * polynomial_kernel(test_point, point[:2]) for alpha, point in model)
    return 1 if value > 0 else -1


def test(model):
    classA = [(random.normalvariate(-1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)] + \
             [(random.normalvariate(1.5, 1), random.normalvariate(0.5, 1), 1.0) for i in range(5)]
    classB = [(random.normalvariate(0.0, 0.5), random.normalvariate(-0.5, 0.5), -1.0) for i in range(10)]
    data = classA + classB
    random.shuffle(data)

    results = [indicator(test_point[:2], model) for test_point in data]
    for pre, target in zip(results, data):
        if int(pre) == int(target[2]):
            print True
        else:
            print False

    print results
    print map(lambda each: each[2], data)
    return results


def main():
    alpha_list = train()
    model = get_non_zeros(alpha_list)
    # test_point = (2.5473284419, 1.37778966571)

    # predict = indicator(test_point, model)
    # print predict, predict == 1.0
    test(model)


if __name__ == "__main__":
    main()
