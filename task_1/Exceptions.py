class KillError(Exception):
    pass


class DrunkError(KillError):
    pass


class CarCrushError(KillError):
    pass


class GluttonyError(KillError):
    pass


class DepressionError(KillError):
    pass
