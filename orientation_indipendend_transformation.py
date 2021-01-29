import numpy as np
from sklearn.decomposition import PCA


def orientation_independent_transformation(data):

    data_transformed = []

    for sample in data:
        ax = sample[0]
        ay = sample[1]
        az = sample[2]
        gx = sample[3]
        gy = sample[4]
        gz = sample[5]

        gravity_vector = np.array([[np.mean(ax), np.mean(ay), np.mean(az)]]).T

        vertical_versor = gravity_vector / np.linalg.norm(gravity_vector, ord=2, axis=0) #(3,1)

        A = np.array([ax, ay, az]) # (3,125)
        G = np.array([gx, gy, gz]) # (3,125)

        # project data onto the vertical versor
        projected_vertical_acc = np.matmul(A.T, vertical_versor) #(125,1)
        projected_vertical_gyro = np.matmul(G.T, vertical_versor) #(125,1)

        A_floor = A - np.matmul(vertical_versor, projected_vertical_acc.T)

        # applying PCA
        pca = PCA(n_components=1)
        pca.fit(A_floor.T)

        first_component = pca.components_.T

        horrizontal_versor = first_component / np.linalg.norm(first_component, ord=2, axis=0)

        projected_horrizontal_acc = np.matmul(A.T, horrizontal_versor)
        projected_horrizontal_gyro = np.matmul(G.T, horrizontal_versor)

        lateral_versor = np.cross(vertical_versor, horrizontal_versor, axis=0)

        projected_lateral_acc = np.matmul(A.T, lateral_versor)
        projected_lateral_gyro = np.matmul(G.T, lateral_versor)

        sample_transformed = np.array([projected_vertical_acc.T, projected_horrizontal_acc.T, projected_lateral_acc.T, projected_vertical_gyro.T, projected_horrizontal_gyro.T, projected_lateral_gyro.T ]).reshape((6,125))

        data_transformed.append(sample_transformed)

    return np.array(data_transformed)
