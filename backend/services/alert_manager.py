class AlertManager:
    def __init__(self):
        self.alerts = []

    def add_alert(self, alert):
        self.alerts.append(alert)
        print(f"Alert added: {alert}")

    def remove_alert(self, alert):
        self.alerts.remove(alert)
        print(f"Alert removed: {alert}")

    def list_alerts(self):
        return self.alerts

# Example usage
if __name__ == '__main__':
    manager = AlertManager()
    manager.add_alert('High CPU usage')
    manager.add_alert('Disk space low')
    print(manager.list_alerts())
    manager.remove_alert('High CPU usage')
    print(manager.list_alerts())
