class Function:
    def __call__(self, value):
        raise NotImplementedError


class CompositeFunction(Function):
    def __init__(self, *functions):
        # TODO: fill this code
        # NOTE: `functions` is a tuple of arguments
        self.functions = functions

    def __call__(self, value):
        # TODO: fill this code
        # HINT: `reversed(TUPLE)` returns a tuple in reversed order
        res = value
        for f in reversed(self.functions):
            res = f(res)
        return res


class F(Function):
    def __call__(self, value):
        return value + 1


class G(Function):
    def __call__(self, value):
        return value ** 2


class H(Function):
    def __call__(self, value):
        return value - 3


if __name__ == "__main__":
    f = F()
    g = G()
    h = H()

    func = CompositeFunction(h, g, f)

    print(func(2))  # 6
