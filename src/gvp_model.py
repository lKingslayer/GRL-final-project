
from dgl.nn.pytorch import GVPConv

class GVPModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super(GVPModel, self).__init__()
        self.gvp_layer = GVPConv(input_dim, hidden_dim, output_dim)

    def forward(self, graph):
        graph = self.gvp_layer(graph)
        return graph
