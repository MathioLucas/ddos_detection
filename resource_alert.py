import logging

logging.basicConfig(
    filename="logs/resource_alert.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def simulate_scaling(action):
    logging.info(f"Scaling action: {action}")
    print(f"Action Taken: {action}")

def alert_system(anomaly_status):
    if anomaly_status == "Potential DDoS Attack":
        alert_message = "Alert: Potential DDoS Attack detected! Initiating mitigation actions."
        logging.warning(alert_message)
        print(alert_message)
        simulate_scaling("Scaling additional servers by 20%")
    else:
        logging.info("Traffic is normal. No action required.")
        print("Traffic is normal.")

if __name__ == "__main__":
    test_status = "Potential DDoS Attack"
    alert_system(test_status)
