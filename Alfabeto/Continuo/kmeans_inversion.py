import pickle

from Continuo import ContinuoConverter as CC, ContinuoMarkov as CM
from Continuo import ContinuoConverters as converters

from time import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.metrics import silhouette_samples, silhouette_score
from alfabeto_sources import all_sources


def inversion_data(corpus):
    continuo_corpus = []
    all_data = []
    for x in corpus:
        continuo_corpus.append(CC.book_converter_pc(x, 'all'))
    for w in continuo_corpus:

        for thing in w:
            frequency_dict = {}
            total_numbers = 0
            freq_list = []
            for number in range(12):
                for inversion_list in converters.triad_inversions_pc:
                    for inversion in inversion_list:
                        frequency_dict[str((number, inversion))] = 0
                        for x in thing:
                            if x[0] == number and x[1] == inversion:
                                frequency_dict[str((x[0], inversion))] += 1
                                total_numbers += 1
        # print(frequency_dict, total_numbers)
            for number in range(12):
                for inversion_list in converters.triad_inversions_pc:
                    for inversion in inversion_list:
                        for x, y in frequency_dict.items():
                            if x == str((number, inversion)):
                                # freq_list.append(y/total_numbers * 100)
                                freq_list.append(y/total_numbers * 100)
            # print(frequency_dict, total_numbers)
            all_data.append(freq_list)
    return all_data
#
# def inversion_data_corpus(list_of_data):
#     for w in list_of_data:
#
#         for thing in w:
#             frequency_dict = {}
#             total_numbers = 0
#             freq_list = []
#             for number in range(12):
#                 for inversion_list in converters.triad_inversions_pc:
#                     for inversion in inversion_list:
#                         frequency_dict[str((number, inversion))] = 0
#                         for x in thing:
#                             if x[0] == number and x[1] == inversion:
#                                 frequency_dict[str((x[0], inversion))] += 1
#                                 total_numbers += 1
#         # print(frequency_dict, total_numbers)
#             for number in range(12):
#                 for inversion_list in converters.triad_inversions_pc:
#                     for inversion in inversion_list:
#                         for x, y in frequency_dict.items():
#                             if x == str((number, inversion)):
#                                 # freq_list.append(y/total_numbers * 100)
#                                 freq_list.append(y/total_numbers * 100)
#             # print(frequency_dict, total_numbers)
#             all_data.append(freq_list)
#     return all_data
#
def label_maker_alf(corpus_list):

    final_labels = []
    alf_labels = []
    for x in corpus_list:
        for z in x.values():
            #print(z['data']['key'])
            a = z['data']['key']
            b = z['data']['final']
            c = (a, b)
            final_labels.append(c)

    for x in final_labels:
    # for x in corpus_list: #do this if the tuples are in list of list

        if x == ('f',2):
            alf_labels.append('$♭:D$')
        elif x == ('n',4):
            alf_labels.append('$♮:E$')
        elif x == ('n',9):
            alf_labels.append('$♮:A$')
        elif x == ('f',7):
            alf_labels.append('$♭:G$')
        elif x == ('n',2):
            alf_labels.append('$♮:D$')
        elif x == ('f',9):
            alf_labels.append('$♭:A$')
        elif x == ('f',0):
            alf_labels.append('$♭:C$')
        elif x == ('f',10):
            alf_labels.append('$♭:B♭$')
        elif x == ('n',5):
            alf_labels.append('$♮:F$')
        elif x == ('n',0):
            alf_labels.append('$♮:C$')
        elif x == ('f',5):
            alf_labels.append('$♭:F$')
        elif x == ('n',7):
            alf_labels.append('$♮:G$')
        elif x[0] == '*':
            if x[1:] == str(('f', 2)):
                alf_labels.append('*$♭:D$')
            elif x[1:] == str(('n', 4)):
                alf_labels.append('*$♮:E$')
            elif x[1:] == str(('n', 9)):
                alf_labels.append('*$♮:A$')
            elif x[1:] == str(('f', 7)):
                alf_labels.append('*$♭:G$')
            elif x[1:] == str(('n', 2)):
                alf_labels.append('*$♮:D$')
            elif x[1:] == str(('f', 9)):
                alf_labels.append('*$♭:A$')
            elif x[1:] == str(('f', 0)):
                alf_labels.append('*$♭:C$')
            elif x[1:] == str(('f', 10)):
                alf_labels.append('*$♭:B♭$')
            elif x[1:] == str(('n', 5)):
                alf_labels.append('*$♮:F$')
            elif x[1:] == str(('n', 0)):
                alf_labels.append('*$♮:C$')
            elif x[1:] == str(('f', 5)):
                alf_labels.append('*$♭:F$')
            elif x[1:] == str(('n', 7)):
                alf_labels.append('*$♮:G$')
        elif x == 'Temperley MAJOR' or x == 'TMAJ':
            alf_labels.append('$M$')
        elif x == 'Temperley MINOR' or x == 'TMIN':
            alf_labels.append('$m$')
        else:
            alf_labels.append('o')
    return alf_labels


def k_means_data(list_of_lists, cluster_number, label_markers):
    np.random.seed(42)

    digits = np.array(list_of_lists)
    # data = scale(digits)
    data = digits
    label_dict = {}
    label_numbers = []
    n = 0
    label_dict[label_markers[0]] = 0
    for j in range(1, len(label_markers)):
        if label_markers[j] not in label_dict:
            label_dict[label_markers[j]] = n+1
            n += 1

    for i in label_markers:
        label_numbers.append(label_dict[i])
    n_samples, n_features = data.shape
    n_digits = cluster_number
    labels = np.array(label_numbers)
    # print('label numbers', label_numbers)
    # sample_size = 300

    sample_size = len(data)
    # print(sample_size, 'Sample Size')


    print("n_digits: %d, \t n_samples %d, \t n_features %d"
          % (n_digits, n_samples, n_features))

    print(79 * '_')
    print('% 9s' % 'init'
                   '        time     inertia  homo     compl   v-meas  ARI  AMI   silhouette')

    def bench_k_means(estimator, name, data):
        t0 = time()
        estimator.fit(data)
        print('% 9s   %.2fs    %i   %.3f   %.3f   %.3f   %.3f   %.3f    %.3f'
              % (name, (time() - t0), estimator.inertia_,
                 metrics.homogeneity_score(labels, estimator.labels_),
                 metrics.completeness_score(labels, estimator.labels_),
                 metrics.v_measure_score(labels, estimator.labels_),
                 metrics.adjusted_rand_score(labels, estimator.labels_),
                 metrics.adjusted_mutual_info_score(labels, estimator.labels_),
                 metrics.silhouette_score(data, estimator.labels_,
                                          metric='euclidean',
                                          sample_size=sample_size)))


    bench_k_means(KMeans(init='k-means++', n_clusters=n_digits, n_init=10),
                  name="k-means++", data=data)

    bench_k_means(KMeans(init='random', n_clusters=n_digits, n_init=10),
                  name="random", data=data)

    # in this case the seeding of the centers is deterministic, hence we run the
    # kmeans algorithm only once with n_init=1
    pca = PCA(n_components=n_digits).fit(data)
    bench_k_means(KMeans(init=pca.components_, n_clusters=n_digits, n_init=1),
                  name="PCA-based",
                  data=data)
    print(79 * '_')

    ###############################################################################
    # Visualize the results on PCA-reduced data

    reduced_data = PCA(n_components=2).fit_transform(data)
    kmeans = KMeans(init='k-means++', n_clusters=n_digits, n_init=10)
    kmeans.fit(reduced_data)

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02  # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 2, reduced_data[:, 0].max() + 2
    y_min, y_max = reduced_data[:, 1].min() - 2, reduced_data[:, 1].max() + 2
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    # plt.set_size_inches(6, 4)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    for x, y, z in zip(reduced_data[:, 0], reduced_data[:, 1], label_markers):
        if z == '$Temperley MAJOR$' or z == '$M$':
            plt.plot(x, y, 'k.', marker='$M$', color='white', markeredgecolor='none', markersize=40)
        elif z == '$Temperley MINOR$' or z == '$m$':
            plt.plot(x, y, 'k.', marker='$m$', color='white', markeredgecolor='none', markersize=40)
        elif z[0] == '*':
            # plt.plot(x, y, 'k.', marker=z[1:], color='white', markeredgecolor='none', markersize=40)
            plt.plot(x, y, 'k.', marker='o', color='white', markeredgecolor='none', markersize=10)
        else:
            plt.plot(x, y, 'k.', marker=z, alpha=.3, markersize=len(z)*4)
            # plt.plot(x, y, 'k.', marker='.', alpha=.4)
#     plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.')
        # plt.plot(x, y, 'k.')

    # for x in alf_labels:
    #         plt.plot(reduced_data[:, 0], reduced_data[:, 1], 'k.', marker = x, markersize=5)
    #     print('reduced data:', reduced_data)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    # plt.title('PCA-reduced data\n'
    #           'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.savefig(path, bbox_inches='tight')
    k_data = KMeans(init='k-means++', n_clusters=n_digits, n_init=10).fit(data)
    return {'silhouette': metrics.silhouette_score(data, k_data.labels_, metric='euclidean', sample_size=sample_size),
            'completeness': metrics.completeness_score(data, k_data.labels_),
            'pca': PCA(n_components=2).fit_transform(data)}
    # return reduced_data, metrics.silhouette_score(data, k_data.labels_, metric='euclidean', sample_size=sample_size)
    # return

def silhouette_analysis(list_of_lists, max_clusters):

    X = np.array(list_of_lists)
    y = np.array([x for x in range(len(X))])
    range_n_clusters = [x for x in range(2, max_clusters)]

    for n_clusters in range_n_clusters:
        # Create a subplot with 1 row and 2 columns
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(18, 7)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, random_state=10)
        cluster_labels = clusterer.fit_predict(X)

        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(X, cluster_labels)
        print("For n_clusters =", n_clusters,
              "The average silhouette_score is :", silhouette_avg)

        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(X, cluster_labels)

        y_lower = 10
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = \
                sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.spectral(float(i) / n_clusters)
            ax1.fill_betweenx(np.arange(y_lower, y_upper),
                              0, ith_cluster_silhouette_values,
                              facecolor=color, edgecolor=color, alpha=0.7)

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhoutte score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        colors = cm.spectral(cluster_labels.astype(float) / n_clusters)
        ax2.scatter(X[:, 0], X[:, 1], marker='.', s=30, lw=0, alpha=0.7,
                    c=colors)

        # Labeling the clusters
        centers = clusterer.cluster_centers_
        # Draw white circles at cluster centers
        ax2.scatter(centers[:, 0], centers[:, 1],
                    marker='o', c="white", alpha=1, s=200)

        for i, c in enumerate(centers):
            ax2.scatter(c[0], c[1], marker='$%d$' % i, alpha=1, s=50)

        ax2.set_title("The visualization of the clustered data.")
        ax2.set_xlabel("Feature space for the 1st feature")
        ax2.set_ylabel("Feature space for the 2nd feature")

        plt.suptitle(("Silhouette analysis for KMeans clustering on sample data "
                      "with n_clusters = %d" % n_clusters),
                     fontsize=14, fontweight='bold')

        plt.show()

# A = inversion_data(all_sources.GetAll.all_alf)
#
# PAL = all_sources.GetAll.all_alf


