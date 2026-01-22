#!/usr/bin/env python3
"""Test script for Reachy Mini Simulation daemon."""

from reachy_mini import ReachyMini


def test_sim_daemon_connection():
    """Test that we can connect to the Simulation daemon and check its status."""
    print("Testing connection to Reachy Mini Simulation daemon...")

    with ReachyMini(
        robot_name="reachy_mini_sim",
        connection_mode="localhost_only",
        media_backend="no_media"
    ) as mini:
        status = mini.client.get_status()

        print(f"[OK] Daemon state: {status['state']}")
        assert status['state'] == "running", f"Expected 'running', got '{status['state']}'"

        print(f"[OK] Simulation enabled: {status['simulation_enabled']}")
        assert status['simulation_enabled'] is True, "Expected simulation_enabled to be True"

        print("\n[SUCCESS] Simulation daemon is running correctly")


if __name__ == "__main__":
    test_sim_daemon_connection()
