def define_config():
    return {
        "reporter": [["list"]],  # Minimal terminal output; Allure handles reporting
        "use": {
            "screenshot": "only-on-failure",  # Auto-screenshots for UI
            "trace": "on-first-retry"
        },
        "testDir": "tests"
    }