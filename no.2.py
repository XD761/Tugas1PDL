## No. 2

import numpy as np
import time

def matrix(n, m, R, dtype):
    A = np.random.rand(n, m).astype(dtype)
    B = np.random.rand(m, 1).astype(dtype)
    C = np.random.rand(n, 1).astype(dtype)

    waktu_mulai = time.time()

    for _ in range(R):
        Y = A @ B + C
        waktu_akhir = time.time()

        waktu = waktu_akhir - waktu_mulai
        
        print(f"Parameter : (n={n}, m={m}, R={R}) => waktu : {waktu: .4f} detik")

if __name__ == "__main__":
    ## tipe data float32
    print("Tipe data float32")
    matrix(100, 1000, 10, np.float32)
    matrix(200, 2000, 10, np.float32)
    matrix(400, 4000, 10, np.float32)
    matrix(400, 4000, 10, np.float32)
    matrix(1600, 16000, 2, np.float32)
    print("\n\n")

    ## tipe data float16
    print("Tipe data float16")
    matrix(100, 1000, 10, np.float16)
    matrix(200, 2000, 10, np.float16)
    matrix(400, 4000, 10, np.float16)
    matrix(400, 4000, 10, np.float16)
    matrix(1600, 16000, 2, np.float16)
    print("\n\n")

    ## tipe data float64
    print("Tipe data float64")
    matrix(100, 1000, 10, np.float64)
    matrix(200, 2000, 10, np.float64)
    matrix(400, 4000, 10, np.float64)
    matrix(400, 4000, 10, np.float64)
    matrix(1600, 16000, 2, np.float64)
    print("\n\n")