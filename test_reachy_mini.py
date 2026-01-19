"""Integration test for Reachy Mini daemon lifecycle."""

import time
from reachy_mini.reachy_mini import ReachyMini


def test_daemon_connection():
    """Test that we can connect to the daemon and check its status."""
    print("Testing connection to Reachy Mini daemon...")

    with ReachyMini(media_backend="no_media", connection_mode="network") as mini:
        # Get daemon status
        status = mini.client.get_status()

        print(f"Daemon state: {status['state']}")
        print(f"Simulation enabled: {status['simulation_enabled']}")
        print(f"Wireless version: {status['wireless_version']}")
        print(f"Backend status: {status['backend_status']}")

        # Verify expected status
        assert status['state'] == "running", f"Expected state 'running', got '{status['state']}'"
        assert status['error'] is None, f"Daemon has error: {status['error']}"
        assert status['backend_status']['motor_control_mode'] == "enabled", \
            f"Expected motor_control_mode 'enabled', got '{status['backend_status']['motor_control_mode']}'"

        print("✓ Daemon is running correctly")

        # Test basic functionality - set compliant mode
        print("Testing basic motor control...")
        mini.set_compliant(head=True)
        time.sleep(0.5)

        print("✓ Basic motor control works")

        print("\n=== All tests passed! ===")


if __name__ == "__main__":
    test_daemon_connection()
