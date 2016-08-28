"""Conjunto de clases y metodos que resuelven los problemas mas comunes de la fisica en la rama de la cinematica"""


class Mru(object):
    """Movimiento rectilineo uniforme."""

    def __init__(self, pos, vel, t=0):
        """Mru(position, speed, time)."""
        self.pos = pos
        try:
            assert vel >= 0
            self.vel = vel
        except AssertionError:
            raise AssertionError("La velocidad introducida es menor a 0")

        try:
            assert t >= 0
            self.t = t
        except AssertionError:
            raise AssertionError("El tiempo introducido es menor a 0")

    def __str__(self):
        """String method."""
        x = str(self.pos)
        v = str(self.vel)
        t = str(self.t)
        cad = ("Movimiento Rectilineo Uniforme. \n" +
               "Datos Iniciales: \n X:" +
               x + " m \n V: " + v + " m/s \n Tiempo: " + t + " s")
        return cad

    def ecuaciones(self):
        """Imprime las ecuaciones del MRU."""
        v = str(self.vel)
        x = str(self.pos - self.vel * self.t)
        print "X(t) = " + x + " + " + v + "t (Ecuacion del movimiento)"
        print "V = " + v + " (Ecuacion de la velocidad)"

    def dist_rec(self, tiempo):
        """Retorna la distancia recorrida en el tiempo dado."""
        d = self.pos + self.vel * (tiempo - self.t)
        return d

    def time_takes(self, x):
        """Retorna el tiempo que tarda en recorrer una distancia x."""
        t = (x - self.pos) / float(self.vel) + self.t
        return t
