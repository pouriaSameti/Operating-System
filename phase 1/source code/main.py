from register import *
from operating_system import OS

if __name__ == '__main__':

    os = OS()
    ir = IR()
    temp = Temp()
    acc = Accumulator()
    pc = PC()

    OS.run(os, pc, ir, acc, temp)



    """t1 = Temp()
    print(t1.is_empty()) 
    t1.set(1)
    print(t1.is_empty())
    t1.reset()
    print(t1.is_empty())

    t1.set(10)
    print(t1.is_empty())
    t1.reset()
    print(t1.is_empty())
    --------------------------------------------------"""
    """t1 = Temp()
    t1.set(1)

    a1 = Accumulator()
    print(a1.is_empty())
    a1.set(100)
    print(a1.is_empty())
    print(a1.get())
    a1.set_to_temp(t1)
    print(a1.get())

    a1.reset()
    # print(a1.get())
    print(a1.is_empty())
    ---------------------------------------------------"""

    """p1 = PC()
    print(p1.get())

    p1.increment()
    p1.increment()
    print(p1.get())
    print(p1.get_ra())

    p1.jump(10)
    print(p1.get())
    print(p1.get_ra())

    p1.jump_back()
    print(p1.get())
    print(p1.get_ra())
    ---------------------------------------------------------"""

    """ir = IR("divide", 20)
    ir1 = IR("load", 20)
    print(ir1.get_instruction())
    print(ir1.get_immediate())"""