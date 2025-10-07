from controller import Robot

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Ambil joint berdasarkan nama di MyRobotArm.proto (nanti disesuaikan)
base = robot.getDevice('joint_base')
extension = robot.getDevice('joint_extension')
shoulder = robot.getDevice('joint_shoulder')
wrist_pitch = robot.getDevice('joint_wrist_pitch')
wrist_roll = robot.getDevice('joint_wrist_roll')

# Inisialisasi posisi
for joint in [base, extension, shoulder, wrist_pitch, wrist_roll]:
    joint.setPosition(0.0)

while robot.step(timestep) != -1:
    # Contoh animasi sederhana (bisa dihapus nanti)
    base.setPosition(3.14)
    extension.setPosition(0.05)
    shoulder.setPosition(0.7)
    wrist_pitch.setPosition(-0.5)
    wrist_roll.setPosition(1.57)
