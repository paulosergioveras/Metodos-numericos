def get_bits(input_bits):
    bits = input_bits.replace(' ', '')

    signal_bit = bits[0]
    exp_bits = bits[1:12]
    frac_bits = bits[12:]
    
    return signal_bit, exp_bits, frac_bits

def represent_ieee_float(input_bits):
    signal_bit, exp_bits, frac_bits = get_bits(input_bits)

    e = int(exp_bits, 2)

    return (f'(-1)^{signal_bit} * (1.{frac_bits})_2 × 2^{e}-1023')

def binary_to_float(input_bits):
    signal_bit, exp_bits, frac_bits = get_bits(input_bits)

    s = int(signal_bit)
    e = int(exp_bits, 2) - 1023

    f = 1.0
    for i, bit in enumerate(frac_bits):
        if bit == '1':
            f += 2 ** (-(i + 1))
    
    result = ((-1) ** s) * f * (2 ** e)
    return result

def process_question(label, input_bits):
    print(f'\n{label}) {input_bits}')

    signal_bit, exp_bits, frac_bits = get_bits(input_bits)

    print(f'Bit de sinal: {signal_bit}')
    print(f'Bits de expoente: {exp_bits}')
    print(f'Bits de fração: {frac_bits}')

    represent_float = represent_ieee_float(input_bits)
    print(f'\nRepresentação na forma (−1)^s (1.f)_2 × 2^e−1023:\n{represent_float}')

    float_result = binary_to_float(input_bits)
    print(f'\nRepresentação decimal: {float_result}')
    print('-' * 60)


def main():
    process_question('a', '0 10000001010 1001001100000000000000000000000000000000000000000000')
    process_question('b', '1 10000001010 1001001100000000000000000000000000000000000000000000')
    process_question('c', '0 01111111111 0101001100000000000000000000000000000000000000000000')
    process_question('d', '0 01111111111 0101001100000000000000000000000000000000000000000001')


if __name__ == '__main__':
    main()
