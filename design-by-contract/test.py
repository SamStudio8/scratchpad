from contracts import contract, ContractNotRespected, new_contract

@contract(a='int,>0', returns='int,<0')
def fa(a):
    return -1 * a

@contract(b='int,>0|<0', returns='int,0')
def fb(b):
    return 0

try:
    fa(-1)
except ContractNotRespected:
    print("Contract violation!")
try:
    fa(1.0)
except ContractNotRespected:
    print("Contract violation!")

fa(8)

try:
    fb(0)
except ContractNotRespected:
    print("Contract violation!")


class MyClass:
    pass

honk = MyClass()

@contract(c=MyClass)
def fc(c):
    return c

fc(MyClass())
try:
    fc(0)
except ContractNotRespected:
    print("Contract violation!")


@contract(x='(int|float),>=0')
def fd(x):
    return x

fd(1.0)
fd(1)

@contract(x='list[>0](int|float,>0)')
def fe(x):
    return x

try:
    fe([])
except ContractNotRespected:
    print("Contract violation!")

try:
    fe([-1])
except ContractNotRespected:
    print("Contract violation!")


@contract(x='dict(str:(int,>0))')
def ff(x):
    return x

try:
    ff({
        "honk": 0
    })
except ContractNotRespected:
    print("Contract violation!")

@contract(x='dict[>0](str:( list[>0](int,>0) ))')
def fg(x):
    return x

try:
    fg({
    })
except ContractNotRespected:
    print("Contract violation! fg0")

try:
    fg({
        "honk": []
    })
except ContractNotRespected:
    print("Contract violation! fg1")

try:
    fg({
        "honk": [1.0]
    })
except ContractNotRespected:
    print("Contract violation! fg2")

fg({
    "honk": [1]
})


@new_contract
def is_even(x):
    if x % 2 != 0:
        raise ValueError("%d is not even" % x)

@contract(x='int,is_even,>0')
def fh(x):
    return x

try:
    fh(3)
except ContractNotRespected as e:
    print(e)


