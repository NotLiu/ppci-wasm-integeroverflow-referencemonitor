from ppci import wasm
code = '(module (func $truth (result i32) (i32.const 42) (return)))'
m1 = wasm.Module(code)
m2 = wasm.Module(m1.to_bytes())

m1.show()