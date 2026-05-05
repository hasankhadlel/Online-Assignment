# ============================================================
# Online Assignment
# Dynamic Distribution for Uneven NRP
# NRP: 121
# ============================================================

import heapq

# ------------------------------------------------------------
# 1. Data task
# ------------------------------------------------------------
# Setiap angka menunjukkan durasi pengerjaan satu task.
# Data task dibuat berdasarkan NRP 121 dan beberapa tambahan task
# agar proses distribusi dapat terlihat lebih jelas.
tasks = [1, 2, 1, 4, 6, 3, 5, 2, 7, 4]

# Jumlah worker/prosesor yang akan mengerjakan task
num_workers = 3

# ------------------------------------------------------------
# 2. Inisialisasi worker
# ------------------------------------------------------------
# Format data worker:
# (total_waktu_kerja, nomor_worker, daftar_task_yang_dikerjakan)
workers = [(0, i + 1, []) for i in range(num_workers)]

# Priority queue digunakan agar worker dengan beban kerja paling kecil
# selalu dipilih terlebih dahulu.
heapq.heapify(workers)

print("====================================================")
print("Dynamic Distribution for Uneven NRP")
print("NRP: 121")
print("====================================================")
print("Task durations:", tasks)
print("Number of workers:", num_workers)
print("")

# ------------------------------------------------------------
# 3. Proses dynamic distribution
# ------------------------------------------------------------
print("Task Execution Process:")
print("----------------------------------------------------")

for task_number, task_duration in enumerate(tasks, start=1):
    # Mengambil worker dengan total waktu kerja paling kecil
    current_time, worker_id, assigned_tasks = heapq.heappop(workers)

    # Menyimpan kondisi sebelum task baru ditambahkan
    start_time = current_time

    # Task diberikan kepada worker tersebut
    assigned_tasks.append(task_duration)

    # Total waktu kerja worker diperbarui
    finish_time = start_time + task_duration
    current_time = finish_time

    print(
        f"Task {task_number} "
        f"(duration = {task_duration}) "
        f"is assigned to Worker {worker_id} "
        f"| start time = {start_time}, finish time = {finish_time}"
    )

    # Worker dimasukkan kembali ke priority queue
    # dengan total waktu kerja yang sudah diperbarui
    heapq.heappush(workers, (current_time, worker_id, assigned_tasks))

# ------------------------------------------------------------
# 4. Hasil akhir distribusi task
# ------------------------------------------------------------
print("")
print("Final Distribution:")
print("----------------------------------------------------")

# Mengurutkan worker berdasarkan nomor worker agar output lebih rapi
workers = sorted(workers, key=lambda x: x[1])

total_times = []

for total_time, worker_id, assigned_tasks in workers:
    total_times.append(total_time)
    print(
        f"Worker {worker_id}: "
        f"tasks = {assigned_tasks} "
        f"| total working time = {total_time}"
    )

# ------------------------------------------------------------
# 5. Expected optimal time
# ------------------------------------------------------------
# Expected optimal time adalah waktu terbesar dari seluruh worker,
# karena seluruh pekerjaan selesai ketika worker terakhir selesai.
optimal_time = max(total_times)

# Menentukan worker yang memiliki total waktu paling besar
slowest_worker = max(workers, key=lambda x: x[0])

print("")
print("Expected Optimal Time:")
print("----------------------------------------------------")
print("Expected optimal time =", optimal_time)
print("The program reaches the expected optimal time at time =", optimal_time)
print(f"This happens when Worker {slowest_worker[1]} finishes all assigned tasks.")

print("====================================================")