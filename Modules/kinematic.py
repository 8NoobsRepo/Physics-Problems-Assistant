"""Modulo para la resolucion de problemas de cinematica."""
import math


class Mru(object):
    """Movimiento rectilineo uniforme."""

    def __init__(self, pos, vel, t=0):
        """Constructor Class."""
        self.pos = pos
        self.vel = vel
        if t is not None:
            try:
                assert t >= 0
                self.t = t
            except AssertionError:
                raise AssertionError("El tiempo introducido es menor a 0")

    def __str__(self):
        """String method."""
        return ("Movimiento Rectilineo Uniforme. \n" +
                "------------------------------- \n" +
                "Datos Iniciales:" +
                "\n x: %s m" % (str(self.pos)) +
                "\n v: %s m/s" % (str(self.vel)) +
                "\n t: %s s" % (str(self.t)))

    def ecuaciones(self):
        """Imprime las ecuaciones del MRU."""
        v = str(self.vel)
        x = str(self.pos - self.vel * self.t)
        print "x(t) = " + x + " + " + v + "t (Ecuacion del movimiento)"
        print "v = " + v + " (Ecuacion de la velocidad)"

    def init_pos(self, pos, t):
        """Devuelve la posicion inicial del movil.

        Datos: tiempo y la distancia recorrida en ese tiempo.
        """
        if self.pos is None:
            return pos - self.vel * (t - self.t)
        else:
            return self.pos

    def init_vel(self, pos, t):
        """Devuelve la velocidad inicial del movil.

        Datos: tiempo y la distancia recorrida en ese tiempo.

        """
        if self.vel is None:
            return (pos - self.pos) / float((t - self.t))

    def dist_rec(self, tiempo):
        """Retorna la distancia recorrida en el tiempo dado."""
        d = self.pos + self.vel * (tiempo - self.t)
        return d

    def time_takes(self, x):
        """Retorna el tiempo que tarda en recorrer una distancia x."""
        t = (x - self.pos) / float(self.vel) + self.t
        return t


class Mrua(Mru, object):
    """Movimiento rectilineo uniformemente acelerado."""

    def __init__(self, pos, vel, ace, t=0):
        """Constructor class."""
        Mru.__init__(self, pos, vel, t)
        self.ace = ace

    def __str__(self):
        """Method string."""
        return ("Movimiento Rectilineo Uniformemente Acelerado. \n" +
                "---------------------------------------------- \n" +
                "Datos Iniciales:" +
                "\n x: %s m" % (str(self.pos)) +
                "\n v: %s m/s" % (str(self.vel)) +
                "\n a: %s m/s^2" % (str(self.ace)) +
                "\n t: %s s" % (str(self.t)))

    def ecuaciones(self):
        """Imprime las ecuaciones del movimiento."""
        v = self.vel
        a = self.ace
        t = self.t
        print ("x(t) = %s + " % (str(self.pos - v * t - 0.5 * a * t)) +
               "%st " % str(self.vel) +
               "%st^2 (Ecuacion del movimiento)" % (str(self.ace * 0.5)))
        print ("v(t) = %s + " % str(self.vel) +
               "%st (Ecuacion de la velocidad)" % str(self.ace))
        print "a(t) = %s (Ecuacion de la aceleracion)" % str(self.ace)

    def spd_rch(self, t):
        """Velocidad alcanzada en un tiempo t."""
        return self.vel + self.ace * t

    def pos_rch(self, t):
        """Posicion alcanzada en un tiempo t."""
        return self.pos + self.vel * t + 0.5 * self.ace * t**2

    def time_spd(self, vel):
        """Tiempo que tarda el movil en alcanzar una velocidad vel."""
        return (vel - self.pos) / (float(self.ace)) + self.t

    def time_pos(self, pos):
        """Tiempo que tarda el movil en alcanzar una posicion pos."""
        c = self.pos - pos
        b = -self.vel
        a = self.ace
        sol1 = 0
        sol2 = 0
        try:
            sol1 = (b + math.sqrt(b**2 + (-2) * a * c)) / float(a)
            assert sol1 >= 0
        except (ValueError, AssertionError):
            sol1 = -1
        try:
            sol2 = (b - math.sqrt(b**2 + (-2) * a * c)) / float(a)
            assert sol2 >= 0
        except (ValueError, AssertionError):
            sol2 = -1
        if sol1 == sol2 == -1:
            return "No hay solucion que obtenga un t>0"
        elif sol1 != sol2 == -1:
            return sol1
        elif sol2 != sol1 == -1:
            return sol2
        else:
            return [sol1, sol2]


class FreeFall(Mrua, object):
    """Caso particular de Mrua."""

    def __init__(self, altura, vel, t=0):
        """Class Constructor."""
        Mrua.__init__(self, altura, vel, -9.8, t)

    def __str__(self):
        """String method."""
        return Mrua.__str__(self)

    def dist_to_floor(self, t):
        """Devuelve la altura a la que se encuentra el movil.

        Datos de entrada: tiempo de caida.

        """
        return Mrua.time_pos(self, t)
