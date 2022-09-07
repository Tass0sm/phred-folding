test_seq = gggtctctctggttagaccagatctgagcctgggagctctctggctaactagggaaccca

###############################################################################
#                                    Utils                                    #
###############################################################################

def is_g_c_pair(seq, i, j):
    return (seq[i] == 'g' and seq[j] == 'c') or (seq[i] == 'c' and seq[j] == 'g')

def is_a_u_pair(seq, i, j):
    return (seq[i] == 'a' and seq[j] == 'u') or (seq[i] == 'u' and seq[j] == 'a')

def FH(seq, i, j):


###############################################################################
#                                     main                                    #
###############################################################################

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
def V(seq, i, j):
    if j - i = 4:
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

        V(i, j) = min([E1, E2, E3])
    else:
        print("Too short")
        return None

# the minimum free energy (kcal/mol) of any possible structure
def W(seq, i, j):
    if j - i = 4:
        return 0
    elif j - i > 4:
        print("TODO")
    else:
        print("Too short")
        return None
