
# %%
from dataclasses import dataclass

from types import MethodType, FunctionType, LambdaType
from typing import Callable, Any, Tuple, Optional, List


def _rewrite_me():
    raise NotImplementedError()


@dataclass
class Delay:
    f: Callable = _rewrite_me
    args: Tuple[Any] = ((), )

    def execute(self):
        return self.f(*self.args)


@dataclass
class Order:
    afters: Optional[Tuple[str]] = None
    befores: Optional[Tuple[str]] = None
    orders: List[str] = []

    def __getattr__(self, name):
        print(f'getatter: {name}')


class Limit:

    @staticmethod
    def after(*methods):
        def deco(f):
            def _(nonself, *args, **kwargs):
                print(nonself)
                return f(nonself, *args, **kwargs)
            return _
        return deco

    @staticmethod
    def before(*methods):
        def deco(f):
            def _(nonself, *args, **kwargs):
                print(nonself)
                return f(nonself, *args, **kwargs)
            return _
        return deco

    @staticmethod
    def __call__(cls):
        """
        メソッドが呼ばれたときに直前によばれたメソッドがafterで指定したものでなければエラーを挙げる
        またbeforeで使えるようにこの
        """
        dic = {
            k: v
            for k, v in cls.__dict__.items()
            if isinstance(v, (MethodType, FunctionType, LambdaType)) and k[0] != '_'
        }
        print(dic)
        print(cls.__dict__)
        print(cls.__class__)
        return cls


limit = Limit()
# %%


@limit
@dataclass
class Trans(Order):
    delay: Delay = Delay()

    @limit.after('args')
    def lam6da(self, f: Callable):
        pass

    @limit.before('lam6da')
    def args(self, *args):
        self._args = args


a = 1
b = 2
trans = Trans()
trans.delay
trans.args(a, b)
trans._args


# %%

class Base:
    a = 1


class Foo:
    def __del__(self):
        print('死んだああああ')

    def __getattr__(self, attrname):
        print("result : ")
        return getattr(self, attrname)

    def test(self, s):
        print(s)


f = Foo()
f.test('ssssss')
f.aa()

a = 1
print(a)
