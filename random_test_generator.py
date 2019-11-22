import random

registers = ['$zero','$ra','$sp','$gp','$tp','$t0','$t1','$t2','$s0','$s1','$a0','$a1','$a2','$a3','$a4','$a5',
'$a6','$a7','$s2','$s3','$s4','$s5','$s6','$s7','$s8','$s9','$s10','$s11','$t3','$t4','$t5','$t6']

coverpoint = ['add', 'sub', 'mul', 'div', 'xor']

def rt_generator():

    choice = random.randint(0,4)
    return 'lw ' + registers[5] + ',' + '0x0C($zero)' + '\n',\
    'lw' + registers[6] + ',' + '0x10($zero)' + '\n',\
    coverpoint[choice] + registers[7] + ',' + registers[5] + ',' + registers[6]


if __name__ == '__main__':
    text = 'main:\n'
    val = rt_generator();
    text += val[1] # generate one ori assembly code
    #for i in range(100): # generate 100 ori assembly code
        #text += generate_ori()

    # output to file
    f = open('generator_example.asm', 'w')
    f.write(text)
    f.close()    
