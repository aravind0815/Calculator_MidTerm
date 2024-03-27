'''Test cases of different operations performed'''
import pytest

from app import App

def test_app_get_environment_variable():
    '''Test how the REPL handles the command.'''
    app = App()
#   Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Optionally, check for specific exit code or message
    # assert excinfo.value.code == expected_exit_code
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_add_command(capfd, monkeypatch):
    """Test how the REPL handles an add command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['add', '10', '10', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operations is 20" in captured.out


def test_app_subtract_command(capfd, monkeypatch):
    """Test how the REPL handles a subtract command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['subtract', '9', '6', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operations is 3" in captured.out


def test_app_mul_command(capfd, monkeypatch):
    """Test how the REPL handles a multiply command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['multiply', '5', '2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operation is 10" in captured.out


def test_app_div_command(capfd, monkeypatch):
    """Test how the REPL handles a divide command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['divide', '16', '4', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):
        app.start()

    captured = capfd.readouterr()
    assert "The result of the operation is 4" in captured.out

def test_app_divby0_command(capfd, monkeypatch):
    """Test how the REPL handles an div command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['divide', '2', '0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "This action results in Divide by zero error" in captured.out

def test_app_load_command(capfd, monkeypatch):
    """Test how the REPL handles an fetch command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['load', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "Calculator history data:" in captured.out

def test_app_delete_command(capfd, monkeypatch):
    """Test how the REPL handles an delete command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['delete', 1, 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "Data history of calculator after deletion:" in captured.out

def test_app_clear_command(capfd, monkeypatch):
    """Test how the REPL handles an clear command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['clear', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "History has been cleared!" in captured.out

def test_app_menu_command(capfd, monkeypatch):
    """Test how the REPL handles an menu command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit) :
        app.start()

    captured = capfd.readouterr()
    assert "The Menu options are:" in captured.out
