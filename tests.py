from unittest import TestCase, mock, main

from plots import dotplot


class DotPlot(TestCase):
    @mock.patch('matplotlib.pyplot.subplots')
    def test_dotplot(self, _plot):
        ax_mock = mock.MagicMock()
        _plot.return_value = [None, ax_mock]

        values = [10.4, 5.4, 3.1, 8.9]
        dotplot(values)

        ax_mock.plot.assert_called_once_with(values, 'k.')


if __name__ == "__main__":
    main()
