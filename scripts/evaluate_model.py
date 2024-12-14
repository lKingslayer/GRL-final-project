
def evaluate_model(model, data_loader):
    """Evaluate the model."""
    correct = 0
    total = 0
    with torch.no_grad():
        for data in data_loader:
            output = model(data.x, data.edge_index)
            pred = output.argmax(dim=1)
            correct += (pred == data.y).sum().item()
            total += data.y.size(0)
    return correct / total
