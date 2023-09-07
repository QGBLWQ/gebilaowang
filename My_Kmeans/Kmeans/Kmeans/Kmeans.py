import numpy as np

class Kmeans:
    def __init__(self,data,num_clusters):
        self.data=data
        self.num_clusters
        self.num_examples = data.shape[0]
        self.num_features=data.shape[1]

    def train(self,max_iteration):
        Center_Ids = self.Center_Ids_init(self.data,self.num_clusters)
        Closest_Center_Ids = np.zeros((self.num_examples,1))

        for _ in range(max_iteration):
            Closest_Center_Ids = self.Get_Center_Ids(self.data,Center_Ids)
            Center_Ids = self.Update_Center_Ids(self.data,Closest_Center_Ids)


    
    def Center_Ids_init(slef,data,num_clusters):
        Random_Ids = np.random.permutation(self.num_examples)
        Center_Ids = data[Random_Ids[:num_clusters],:]
        return Center_Ids

    
    def Get_Center_Ids(self,data,Center_Ids):
        Num_Center_Ids = Center_Ids.shape[0]
        Cloest_Center_Ids = np.zeros((self.nun_examples,Num_Center_Ids))
        for Example_Index in range(self.num_examples):
            Distance = np.zeros((self.num_examples,1))
            for Center_Ids_Index in range(Num_Center_Ids):
                Distance_diff = data[Example_Index,:] - data[Center_Ids_Index,:]
                Distance[Center_Ids_Index] = np.sum(Distance_diff**2)
            Cloest_Center_Ids[Example_Index] = np.argmin(Distance)
        return Cloest_Center_Ids


    def Update_Center_Ids(self,data,Closest_Center_Ids):
        Center_Ids = np.zeros((self.num_clusters,self.num_features))
        for Center_Id in range(self.num_clusters):
            Closest_Ids = Closest_Center_Ids == Center_Id
            Center_Ids[Center_Id] = np.mean(data[Closest_Ids.flatten(),:],axis=0)
        return Center_Ids
