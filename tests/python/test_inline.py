import tvm

def test_inline():
    m = tvm.Var('m')
    A = tvm.placeholder((m,), name='A')
    T = tvm.compute((m,), lambda i,: A(i) + 10, name='T')
    X = T(100)
    stmt = tvm.make.Evaluate(T(10) + 11 * T(100))
    stmt = tvm.ir_pass.Inline(
        T, T.source_op.iter_var, T.source_op.body, stmt)
    print(stmt)
    assert(tvm.ir_pass.VerifySSA(stmt))

if __name__ == "__main__":
    test_inline()