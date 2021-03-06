from unittest import TestCase, mock

from clickable.commands.run import RunCommand
from ..mocks import ConfigMock, empty_fn


class TestRunCommand(TestCase):
    def setUp(self):
        self.config = ConfigMock({})
        self.command = RunCommand(self.config)

    @mock.patch('clickable.container.Container.run_command', side_effect=empty_fn)
    @mock.patch('clickable.container.Container.setup_dependencies', side_effect=empty_fn)
    def test_run(self, mock_setup_dependencies, mock_run_command):
        self.command.run('echo foo')

        mock_setup_dependencies.assert_called_once()
        mock_run_command.assert_called_once_with('echo foo', use_dir=False)

    def test_run_no_command(self):
        with self.assertRaises(ValueError):
            self.command.run()
