# Anthony Leouie Palmera
# PHMAN29

def list_all_prime(number):
    primes = []

    for x in range(2, number + 1):

        is_prime = True

        for y in range(2, int(x ** 0.5) + 1):
            if x % y == 0: 
                is_prime = False
                break

        if is_prime:
            primes.append(x)

    return primes

list_of_primes = list_all_prime(int(input("Enter a number: "))) 

with open(r"files\result_challenge.txt", "w") as file:
    for prime in list_of_primes:
        file.write(str(prime) + "\n")