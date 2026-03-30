class AnomalyDetectionService:
    def __init__(self, threshold: float = 0.5):
        self.threshold = threshold

    def detect(self, data):
        """Detect anomalies in the provided data.
        Args:
            data: List of numerical values to analyze.

        Returns:
            List of indices in the data that are considered anomalies.
        """        
        mean = sum(data) / len(data)
        anomalies = []
        for i, value in enumerate(data):
            if abs(value - mean) > self.threshold:
                anomalies.append(i)
        return anomalies

# Example usage:
# if __name__ == '__main__':
#     service = AnomalyDetectionService(threshold=1.0)
#     data = [1, 2, 3, 10, 2, 1, 3]
#     print(service.detect(data))  # Output indices of anomalies