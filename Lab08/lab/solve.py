import angr
import sys
import binascii

main_addr = 0x4011a9
find_addr = 0x401371
avoid_addr = 0x40134d

# def is_successful(state):
#     stdout_output = state.posix.dumps(sys.stdout.fileno())
#     return 'AC!\n'.encode() in stdout_output


# def should_abort(state):
#     stdout_output = state.posix.dumps(sys.stdout.fileno())
#     return 'WA!\n'.encode() in stdout_output

class my_scanf(angr.SimProcedure):
    def run(self, fmt, n):
        simfd = self.state.posix.get_fd(sys.stdin.fileno())
        data, ret_size = simfd.read_data(0x04)
        self.state.memory.store(n, data)
        return ret_size

proj = angr.Project('./src/prog', load_options={'auto_load_libs': False})
proj.hook_symbol('printf', angr.SIM_PROCEDURES['stubs']['ReturnUnconstrained'](), replace=True)
proj.hook_symbol('__isoc99_scanf', my_scanf(), replace=True)

state = proj.factory.blank_state(addr=main_addr)

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=find_addr, avoid=avoid_addr)

if simgr.found:
    input = simgr.found[0].posix.dumps(sys.stdin.fileno())
    bytes_list = [input[i:i+4] for i in range(0, len(input), 0x04)]
    with open('solve_input', 'w') as f:
        for bytes in bytes_list:
            dec = int.from_bytes(bytes, byteorder='little', signed=True)
            f.write(f'{dec}\n')
else:
    print('Failed')
