import numpy as np
import scipy as sp
import scipy.stats
import mdshare
import pyemma
from pyemma.util.contexts import settings
import MDAnalysis as mda
import matplotlib.pyplot as plt



# --- METHODS FOR CLUSTERING ---
    
    
def obtain_clusters(data, algorithm='kmeans', 
                    num_clusters=2, min_dist=12, max_iter=100,
                    plot=True, saveas=None):
    """
    Clusters the provided data.
    
    Parameters
    ----------
        data : float array)
            Trajectory data. Format: [frames,frame_data]
        algorithm : string) 
            The algorithm to use for the clustering. 
            Options: kmeans, rspace. 
            Default: kmeans
        num_clusters : int, optional
            Number of clusters for k-means clustering. 
            Default: 2.
        min_dist : float, optional
            Minimum distance for regspace clustering. 
            Default: 12.
        max_iter : int, optional
            Maximum number of iterations. 
            Default: 100.
        plot : bool, optional
            Create a plot. 
            Default: True
        saveas : str, optional
            Name of the file in which to save the plot.
            (only needed if "plot" is True)
        
    Returns
    -------
        cidx : int array
            Cluster indices for each frame.
        total_wss : float
            With-in-sum-of-squares (WSS).
        centroids :float array
            Centroids for all the clusters.
    
    """
    
    # Perform PyEMMA clustering
    assert algorithm in ['kmeans','rspace']
    if algorithm == 'kmeans':
        clusters = pyemma.coordinates.cluster_kmeans(data,num_clusters,max_iter=max_iter)
    elif algorithm == 'rspace':
        clusters = pyemma.coordinates.cluster_regspace(data,min_dist)
    
    # Extract cluster indices
    cidx = clusters.get_output()[0][:,0]
    
    # Calculate centroids and total within-cluster sum of square
    centroids = []
    total_wss = 0
    for i in np.unique(cidx):
        # get the data for this cluster
        cluster_data = data[np.where(cidx==i)]
        # calcualte the centroid
        cluster_centroid = np.mean(cluster_data,0)
        centroids.append(cluster_centroid)
        # calculate the within-cluster sum of square
        cluster_wss = np.sum( (cluster_data - cluster_centroid)**2 )
        total_wss += cluster_wss
        
    # Count and plot
    if plot:
        fig,ax = plt.subplots(1,1,figsize=[4,3],dpi=300)
        c, nc = np.unique(cidx,return_counts=True)
        ax.bar(c,nc)
        if saveas is not None:
            fig.savefig(saveas,dpi=300)
    
    return cidx, total_wss, centroids


def obtain_combined_clusters(data_a, data_b, label_a = 'Sim A', label_b = 'Sim B', start_frame = 0,
                             algorithm='kmeans', num_clusters=2, min_dist=12, max_iter=100,
                             plot=True, saveas=None):
    """
    Clusters a combination of two data sets.
    
    Parameters
    ----------
        data_a : float array
            Trajectory data [frames,frame_data]
        data_b : float array
            Trajectory data [frames,frame_data]
        label_a : str, optional
            Label for the plot.
            Default: Sim A.
        label_b : str, optional
            Label for the plot.
            Default: Sim B.
        start_frame : int
            Frame from which the clustering data starts.
            Default: 0.
        algorithm : string
            The algorithm to use for the clustering. 
            Options: kmeans, rspace. 
            Default: kmeans
        num_clusters : int, optional
            Number of clusters for k-means clustering. 
            Default: 2.
        min_dist : float, optional
            Minimum distance for regspace clustering. 
            Default: 12.
        max_iter : int, optional
            Maximum number of iterations. 
            Default: 100.
        plot : bool, optional
            Create a plot. 
            Default: True
        saveas : str, optional
            Name of the file in which to save the plot.
            (only needed if "plot" is True)
        
    Returns
    -------
        cidx : int array
            Cluster indices for each frame.
        cond : int array
            Index of the simulation the data came frome.
        oidx : int array
            Index of each frame in the original simulation (taking into account cutoff)
        total_wss : float
            With-in-sum-of-squares (WSS).
        centroids : float array
            Centroids for all the clusters.
           
    """
    
    # Combine the data
    data = np.concatenate([data_a,data_b],0)

    # Remember which simulation the data came frome
    cond = np.concatenate([np.zeros(len(data_a)), np.ones(len(data_b))])

    # Remember the index in the respective simulation (taking into account cutoff)
    oidx = np.concatenate([np.arange(len(data_a))+start_frame, np.arange(len(data_b))+start_frame])

    # Perform PyEMMA clustering
    assert algorithm in ['kmeans','rspace']
    if algorithm == 'kmeans':
        clusters = pyemma.coordinates.cluster_kmeans(data,k=num_clusters,max_iter=100)
    elif algorithm == 'rspace':
        clusters = pyemma.coordinates.cluster_regspace(data,min_dist)

    # Extract cluster indices
    cidx = clusters.get_output()[0][:,0]

    # Calculate centroids and total within-cluster sum of square
    centroids = []
    total_wss = 0
    for i in np.unique(cidx):
        # get the data for this cluster
        cluster_data = data[np.where(cidx==i)]
        # calcualte the centroid
        cluster_centroid = np.mean(cluster_data,0)
        centroids.append(cluster_centroid)
        # calculate the within-cluster sum of square
        cluster_wss = np.sum( (cluster_data - cluster_centroid)**2 )
        total_wss += cluster_wss
    
    # Count and plot
    if plot:
        fig,ax = plt.subplots(1,1,figsize=[4,3],sharex=True,dpi=300)
        c, nc   = np.unique(cidx,return_counts=True)
        ca, nca = np.unique(cidx[cond==1],return_counts=True)
        cb, ncb = np.unique(cidx[cond==0],return_counts=True)
        ax.bar(ca-0.15,nca,0.3,label=label_a)
        ax.bar(cb+0.15,ncb,0.3,label=label_b)
        ax.legend()
        ax.set_xticks(c)
        ax.set_xlabel('clusters')
        ax.set_ylabel('population')
        fig.tight_layout()
        if saveas is not None:
            fig.savefig(saveas,dpi=300)
    
    return cidx, cond, oidx, total_wss, centroids


