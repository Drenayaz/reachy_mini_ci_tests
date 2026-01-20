"""Integration test for Reachy Mini Lite (USB connection)."""

from reachy_mini.reachy_mini import ReachyMini


def test_lite_daemon_connection():
    """Test that we can connect to the Lite daemon and check its status."""
    print("Testing connection to Reachy Mini Lite daemon...")

    with ReachyMini(
        robot_name="reachy_mini_lite",
        connection_mode="localhost_only",
        media_backend="no_media"
    ) as mini:
        # Get daemon status
        status = mini.client.get_status()

        print(f"[OK] Daemon state: {status['state']}")
        print(f"[OK] Simulation enabled: {status['simulation_enabled']}")
        print(f"[OK] Wireless version: {status['wireless_version']}")
        print(f"[OK] Backend status: {status['backend_status']}")

        # Verify expected status
        assert status['state'] == "running", f"Expected state 'running', got '{status['state']}'"
        assert status['error'] is None, f"Daemon has error: {status['error']}"
        assert status['backend_status']['motor_control_mode'] == "enabled", \
            f"Expected motor_control_mode 'enabled', got '{status['backend_status']['motor_control_mode']}'"
        assert status['wireless_version'] is False, "Expected Lite (non-wireless) version"

        print("\n[SUCCESS] Lite daemon is running correctly")
        print("\n=== All Lite tests passed! ===")


if __name__ == "__main__":
    test_lite_daemon_connection()
