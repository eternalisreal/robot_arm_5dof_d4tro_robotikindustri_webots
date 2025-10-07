from controller import Robot

TIME_STEP = 32
robot = Robot()

# Inisialisasi motor
motors = [
    robot.getDevice("base_motor"),
    robot.getDevice("extend_motor"),
    robot.getDevice("shoulder_motor"),
    robot.getDevice("wrist_pitch_motor"),
    robot.getDevice("wrist_roll_motor")
]

# Set posisi awal motor
motors[0].setPosition(0.0)
motors[2].setPosition(0.0)
motors[3].setPosition(0.0)
motors[4].setPosition(0.0)

# Aktifkan mode kontrol posisi
for motor in motors:
    motor.setVelocity(1.0)

print("Robot controller aktif - menjalankan pergerakan otomatis")

# Gerakan sederhana bolak-balik
while robot.step(TIME_STEP) != -1:
    t = robot.getTime()
    motors[0].setPosition(1.5 * (1 if int(t) % 4 < 2 else -1))
    motors[2].setPosition(0.5 * (1 if int(t) % 4 < 2 else -1))
    motors[3].setPosition(0.3 * (1 if int(t) % 4 < 2 else -1))
    motors[4].setPosition(1.0 * (1 if int(t) % 4 < 2 else -1))
