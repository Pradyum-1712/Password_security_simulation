import hashlib
import time
import string
import itertools
passwords = {
    'simple': 'abc',
    'moderate': 'aB3',
    'complex': 'aB3!',
    'very_complex': 'aB3!xY7@'
}
def simulate_password_cracking(password):
    charset = string.ascii_letters + string.digits + string.punctuation
    attempts = 0
    max_attempts = len(charset) ** len(password)
    start_time = time.time()

    for attempt in itertools.product(charset, repeat=len(password)):
        attempts += 1
        attempt_password = ''.join(attempt)
        if attempt_password == password:
            end_time = time.time()
            time_taken = end_time - start_time
            print(f"Password '{password}' cracked in {attempts} attempts, taking {time_taken:.2f} seconds.")
            return time_taken
        if attempts % 100000 == 0:
            print(f"Attempts so far: {attempts}")

    print(f"Password '{password}' not cracked after {attempts} attempts.")
    return None
results = {}

for level, pwd in passwords.items():
    print(f"Simulating for {level} password...")
    time_taken = simulate_password_cracking(pwd)
    results[level] = time_taken
import matplotlib.pyplot as plt

levels = list(results.keys())
times = [results[level] for level in levels]

plt.bar(levels, times)
plt.xlabel('Password Complexity')
plt.ylabel('Time to Crack (seconds)')
plt.title('Password Security Simulation Results')
plt.show()
