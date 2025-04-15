'''
Natanael Kris Setyabudi
622023018
'''
## No. 1

def create_spiral(karakter, jarak_karakter, jumlah_karakter, arah):
    # Hitung ukuran grid
    size = jumlah_karakter * (jarak_karakter + 1)
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Titik awal di tengah grid
    x, y = size // 2, size // 2
    grid[x][y] = karakter

    # Aturan gerakan
    if arah == "CCW":  # Berlawanan arah jarum jam
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # Atas, Kiri, Bawah, Kanan
    else:  # CW (searah jarum jam)
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Kanan, Bawah, Kiri, Atas

    step = 1
    char_count = 1

    while char_count < jumlah_karakter:
        for dx, dy in moves:
            for _ in range(step):
                if char_count >= jumlah_karakter:
                    break
                x += dx * (jarak_karakter + 1)
                y += dy * (jarak_karakter + 1)
                if 0 <= x < size and 0 <= y < size:
                    grid[x][y] = karakter
                    char_count += 1
            if dx != 0 or dy != 0:  # Tambah langkah setiap dua arah
                step += 1

    return grid


def print_spiral(grid):
    for row in grid:
        print(''.join(row))


if __name__ == "__main__":
    karakter = input("Masukkan karakter: ").upper()
    jarak_karakter = int(input("Masukkan jarak antar karakter: "))
    jumlah_karakter = int(input("Masukkan jumlah karakter: "))
    arah = input("Masukkan arah spiral (CW/CCW): ").upper()

    spiral_grid = create_spiral(karakter, jarak_karakter, jumlah_karakter, arah)
    print_spiral(spiral_grid)