import angr

func_addr = 0x40056D

p = angr.Project("./maze")
cl = p.factory.callable(func_addr)
cl(2, 52, 39)
flag = cl.result_state.posix.stdout.concretize()
print(flag[0].decode())

# FLAG --> batpwn{PRetty_MUch_A_mAzeIng}
