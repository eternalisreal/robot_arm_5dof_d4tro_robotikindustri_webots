# Robot Arm 5 DOF (D4 TRO - Robotik Industri)

Simulasi robot arm 5 DOF menggunakan Webots dan Python Controller.

## Struktur DOF
1. Base Rotation (360°)
2. Linear Extension (memanjang/memendek)
3. Shoulder Pitch (+50° / -30°)
4. Wrist Pitch (±45°)
5. Wrist Roll (360°)

## Struktur Folder
- `/controllers/robot_controller/robot_controller.py` → kontrol logika robot.
- `/protos/MyRobotArm.proto` → definisi struktur robot.
- `/worlds/robot_workspace.wbt` → world simulasi berisi meja dan robot.

## Cara Menjalankan di Webots.cloud
1. Upload seluruh folder ini ke repo GitHub (public).
2. Masuk ke [webots.cloud](https://webots.cloud).
3. Klik **Add Simulation → Import from GitHub**.
4. Masukkan URL repo GitHub ini.
5. Jalankan simulasi!

---

Dibuat oleh **Wildan (D4 TRO Robotik Industri)**.
