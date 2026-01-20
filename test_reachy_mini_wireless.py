"""Integration test for Reachy Mini Wireless (Network connection)."""

from reachy_mini.reachy_mini import ReachyMini


def test_wireless_daemon_connection():
    """Test that we can connect to the Wireless daemon and check its status."""
    print("Testing connection to Reachy Mini Wireless daemon...")

    with ReachyMini(
        robot_name="reachy_mini",
        connection_mode="network",
        media_backend="no_media"
    ) as mini:
        # Get daemon status
        status = mini.client.get_status()

        print(f"[OK] Daemon state: {status['state']}")
        print(f"[OK] Simulation enabled: {status['simulation_enabled']}")
        print(f"[OK] Wireless version: {status['wireless_version']}")
        print(f"[OK] WLAN IP: {status.get('wlan_ip', 'N/A')}")
        print(f"[OK] Backend status: {status['backend_status']}")

        # Verify expected status
        assert status['state'] == "running", f"Expected state 'running', got '{status['state']}'"
        assert status['error'] is None, f"Daemon has error: {status['error']}"
        assert status['backend_status']['motor_control_mode'] == "enabled", \
            f"Expected motor_control_mode 'enabled', got '{status['backend_status']['motor_control_mode']}'"
        assert status['wireless_version'] is True, "Expected Wireless version"
        assert status.get('wlan_ip') is not None, "Expected WLAN IP address"

        print("\n[SUCCESS] Wireless daemon is running correctly")
        print("\n=== All Wireless tests passed! ===")


if __name__ == "__main__":
    test_wireless_daemon_connection()
