"""Collection of methods for converting between Ladybug and .NET colors."""

try:
    from System.Drawing import Color
except ImportError as e:
    print("Ladybug_dotnet is only available when running on Windows/.NET\n{}".format(e))


def color_to_color(color):
    """Convert a ladybug color into .NET color."""
    try:
        return Color.FromArgb(255, color.r, color.g, color.b)
    except AttributeError as e:
        raise AttributeError('Input must be of type of Color:\n{}'.format(e))


def gray():
    """Get a .NET gray color object. Useful when you need a placeholder color."""
    return Color.Gray


def black():
    """Get a .NET black color object. Useful for things like default text."""
    return Color.Black
