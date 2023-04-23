from matplotlib import pyplot as plt

ax = plt.figure().add_subplot(projection='3d')

def transpose(lst):
    return list(zip(*lst))


def render_list(lst):
    
    ax.plot3D(*transpose(lst))

    ax.set_xlabel("X label")
    ax.set_ylabel("Y label")
    ax.set_zlabel("Z label")

    plt.show()



