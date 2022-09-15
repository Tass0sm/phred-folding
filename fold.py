from functools import cache

test_seq = "gggtctctctggttagaccagatctgagcctgggagctctctggctaactagggaaccca"

###############################################################################
#                                    Utils                                    #
###############################################################################

def is_g_c_pair(seq, i, j):
    return (seq[i] == 'g' and seq[j] == 'c') or (seq[i] == 'c' and seq[j] == 'g')

def is_a_u_pair(seq, i, j):
    return (seq[i] == 'a' and seq[j] == 'u') or (seq[i] == 'u' and seq[j] == 'a')

class FH:
    def __init__(self, i, j):
        self.i = i
        self.j = j

        assert self.i < self.j

class FL:
    def __init__(self, i, i_prime, j_prime, j):
        self.i = i
        self.i_prime = i_prime
        self.j = j
        self.j_prime = j_prime

        assert self.i < self.i_prime < self.j < self.j_prime

###############################################################################
#                                     main                                    #
###############################################################################

# ooo(o(oooo))ooo
def E_FL(fl):
    if fh.j - fh.i < 4:
        return 9999
    else:
        return 0

    print("hello")

# (......)
def E_FH(fh):
    if fh.j - fh.i < 4:
        return 9999
    else:
        return 0

# E1 = E(FH(i,j)),
def V_hairpin(seq, i, j):
    print("hello")

# E2 = min {E(FL(i,j,i',j')) + V(i',j')},
#    i<i'<j'<j
def V_stacking_bulge_interior(seq, i, j):
    lower_limit = i + 1
    upper_limit = j

    for i_prime in range(lower_limit, upper_limit):
        for j_prime in range(i_prime + 1, upper_limit):
            e = E() + V(i_prime, j_prime)
            print(f"{i_prime}, {j_prime}")

# E3 = min {W(i+l,i') + W(i'+l,j-l)}.
#    i+l<i'<j-2
def V_bifurcation(seq, i, j):
    lower_limit = i + 2
    upper_limit = j - 2

    for i_prime in range(lower_limit, upper_limit):
        print(f"{i_prime}")

# j comes later in the sequence.

# the minimum free energy (kcal/mol) of any possible loop structure
@cache
def V(seq, i, j):
    if j - i == 4:
        if is_g_c_pair(seq, i, j):
            return 8.4
        elif is_a_u_pair(seq, i, j):
            return 8.0
        else:
            return 0.0
    elif j - i > 4:
        E1 = V_hairpin(seq, i, j)
        E2 = V_stacking_bulge_interior(seq, i, j)
        E3 = V_bifurcation(seq, i, j)

        return min([E1, E2, E3])
    else:
        print("Too short")
        return None

# case 1
# W(i+l,j), W(i,j-1)
def W_i_or_j_in_structure(seq, i, j):
    return min(W(seq, i + 1, j), W(seq, i, j - 1))

# case 2
# V(i,j)
def W_i_j_base_pair(seq, i, j):
    return V(seq, i, j)

# case 3
# E4 = min { W(i,i') + W(i'+l,j) }
#    i< i' <j-1
def W_i_j_pair_others(seq, i, j):
    lower_limit = i + 1
    upper_limit = j - 1

    i_primes = range(lower_limit, upper_limit)
    minimum_energies = map(lambda i_p: W(seq, i, i_p) + W(seq, i_p + 1, j), i_primes)
    return min(minimum_energies)

# the minimum free energy (kcal/mol) of any possible structure
@cache
def W(seq, i, j):
    if j - i == 4:
        return 0
    elif j - i > 4:
        E1 = W_i_or_j_in_structure(seq, i, j)
        E2 = W_i_j_base_pair(seq, i, j)
        E3 = W_i_j_pair_others(seq, i, j)

        return min([E1, E2, E3])
    else:
        print("Too short")
        return None

def E(seq):
    i = 0
    minimum_energy = 0

    for j in range(4, len(seq)):
        minimum_energy = W(seq, i, j)

    return minimum_energy
