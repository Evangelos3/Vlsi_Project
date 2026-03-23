import itertools
import time

def karnaugh_map_2vars(minterms, dont_cares):
    km = [[0 for _ in range(4)] for _ in range(4)]

    for minterm in minterms:
        km[minterm][minterm] = 1
    for dont_care in dont_cares:
        km[dont_care][dont_care] = -1

    groups = []
    for i in range(4):
        for j in range(4):
            if km[i][j] == 1:
                group = [(i, j)]
                km[i][j] = 0
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 4 and 0 <= ny < 4 and km[nx][ny] == 1:
                            group.append((nx, ny))
                            km[nx][ny] = 0
                            queue.append((nx, ny))
                groups.append(group)

    essential_pis = []
    for group in groups:
        is_essential = True
        for other_group in groups:
            if group!= other_group and set(group).issubset(set(other_group)):
                is_essential = False
                break
        if is_essential:
            essential_pis.append(group)

    minimized_expression = ""
    for pi in essential_pis:
        term = ""
        for i in range(2):
            if pi[0][i // 2] == pi[1][i // 2]:
                term += "x" + str(i + 1)
            else:
                term += "x" + str(i + 1) + "'"
        minimized_expression += term + " + "

    return minimized_expression[:-3]

def karnaugh_map_3vars(minterms, dont_cares):
    km = [[0 for _ in range(8)] for _ in range(8)]

    for minterm in minterms:
        km[minterm][minterm] = 1
    for dont_care in dont_cares:
        km[dont_care][dont_care] = -1

    groups = []
    for i in range(8):
        for j in range(8):
            if km[i][j] == 1:
                group = [(i, j)]
                km[i][j] = 0
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 8 and 0 <= ny < 8 and km[nx][ny] == 1:
                            group.append((nx, ny))
                            km[nx][ny] = 0
                            queue.append((nx, ny))
                groups.append(group)

    essential_pis = []
    for group in groups:
        is_essential = True
        for other_group in groups:
            if group != other_group and set(group).issubset(set(other_group)):
                is_essential = False
                break
        if is_essential:
            essential_pis.append(group)

    minimized_expression = ""
    for pi in essential_pis:
        term = ""
        for i in range(3):
            if len(pi) > 1:
                if pi[0][i // 2] == pi[1][i // 2]:
                    term += "x" + str(i + 1)
                else:
                    term += "x" + str(i + 1) + "'"
            else:
                binary_pi = format(pi[0][0], 'b').zfill(3)
                if binary_pi[i] == '1':
                    term += "x" + str(i + 1)
                else:
                    term += "x" + str(i + 1) + "'"
        minimized_expression += term + " + "

    return minimized_expression[:-3]

def karnaugh_map_4vars(minterms, dont_cares):
    start_time = time.time()

    km = [[0 for _ in range(16)] for _ in range(16)]

    for minterm in minterms:
        km[minterm >> 4][minterm & 0xF] = 1
    for dont_care in dont_cares:
        km[dont_care >> 4][dont_care & 0xF] = -1

    groups = []
    for i in range(16):
        for j in range(16):
            if km[i][j] == 1:
                group = [(i, j)]
                km[i][j] = 0
                queue = [(i, j)]
                while queue:
                    x, y = queue.pop(0)
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < 16 and 0 <= ny < 16 and km[nx][ny] == 1:
                            group.append((nx, ny))
                            km[nx][ny] = 0
                            queue.append((nx, ny))
                groups.append(group)

    essential_pis = []
    for group in groups:
        is_essential = True
        for other_group in groups:
            if group!= other_group and set(group).issubset(set(other_group)):
                is_essential = False
                break
        if is_essential:
            essential_pis.append(group)

    minimized_expression = ""
    for pi in essential_pis:
        term = ""
        for i in range(4):
            if len(pi) > 1:
                if pi[0][0] >> i & 1 == pi[1][0] >> i & 1:
                    term += "x" + str(i + 1)
                else:
                    term += "x" + str(i + 1) + "'"
            else:
                binary_pi = format(pi[0][0], 'b').zfill(4)
                if binary_pi[i] == '1':
                    term += "x" + str(i + 1)
                else:
                    term += "x" + str(i + 1) + "'"
        minimized_expression += term + " + "

    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")

    return minimized_expression[:-3]

def quine_mccluskey(minterms, dont_cares, num_vars):
    prime_implicants = {}

    essential_pis = []

    minimized_expression = []

    terms = minterms + dont_cares

    binary_terms = [format(term, 'b').zfill(num_vars) for term in terms]

    groups = {}

    for num_literals in range(num_vars, -1, -1):
        for i in range(len(binary_terms)):
            for j in range(i + 1, len(binary_terms)):
                if sum(c1!= c2 for c1, c2 in zip(binary_terms[i], binary_terms[j])) == 1:
                    new_term = ''.join(c1 if c1 == c2 else '-' for c1, c2 in zip(binary_terms[i], binary_terms[j]))

                    if new_term not in groups:
                        groups[new_term] = [binary_terms[i], binary_terms[j]]
                    else:
                        groups[new_term].append(binary_terms[i])
                        groups[new_term].append(binary_terms[j])

    for group in groups.values():
        if len(group) == 1:
            prime_implicants[group[0]] = True

    for pi in prime_implicants:
        is_essential = True
        for other_pi in prime_implicants:
            if pi!= other_pi and set(pi) <= set(other_pi):
                is_essential = False
                break
        if is_essential:
            essential_pis.append(pi)

    for pi in essential_pis:
        term = ''
        for i in range(num_vars):
            if pi[i] == '1':
                term += 'x' + str(i + 1)
            elif pi[i] == '0':
                term += 'x' + str(i + 1) + "'"
        minimized_expression.append(term)

    return ' '.join(minimized_expression)

def minimize_expression(minterms, dont_cares, num_vars):
    if num_vars == 2:
        return karnaugh_map_2vars(minterms, dont_cares)
    elif num_vars == 3:
        return karnaugh_map_3vars(minterms, dont_cares)
    elif num_vars == 4:
        km_expression = karnaugh_map_4vars(minterms, dont_cares)
        qm_expression = quine_mccluskey(minterms, dont_cares, num_vars)
        return "Karnaugh Map: " + km_expression + "\nQuine-McCluskey: " + qm_expression
    else:
        return quine_mccluskey(minterms, dont_cares, num_vars)

# Get user input
num_vars = int(input("Enter the number of variables: "))
minterms = list(map(int, input("Enter the minterms (space-separated): ").split()))
dont_cares = list(map(int, input("Enter the don't cares (space-separated): ").split()))

# Start timer
start_time = time.time()

# Minimize the expression
minimized_expression = minimize_expression(minterms, dont_cares, num_vars)

# Stop timer
end_time = time.time()

# Print the result
print("Minimized expression:", minimized_expression)
print("Run time:", end_time - start_time, "seconds")
