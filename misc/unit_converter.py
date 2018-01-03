# class Converter:
#     def __init__(self): # the initializer
#         # Initializer: instantiate the unit classes
#         self.conversiondata = (
#             ('Mass', self.Mass()),
#             ('Length', self.Length()),
#             ('Weight', self.Force()),
#             ('Force', self.Force()),
#             ('Temperature', self.Temperature())
#         )
#
#     def convert(self, unittype=0, oldvalue=1.0, oldunit=0, newunit=0):
#         # convert the current entry value from old to the new units
#         conv = self.conversiondata[unittype][1].conversions
#         # newvalue = (float(oldvalue) * conv[oldunit][1] + conv[oldunit][2] - conv[newunit][2]) / conv[newunit][1]
#         newvalue = (float(oldvalue) * conv[oldunit][1]) / conv[newunit][1]
#         newvaluetext = '{:.5}'.format(newvalue)
#         if newvalue <= 0.001 or newvalue >= 1000.:
#             newvaluetext = '{:.5e}'.format(newvalue)
#         # return newvalue
#         return newvaluetext
#
#     class Force: # these subclasses do not need initializers
#         conversions = (
#             ('Newtons', 1.0, 0.), ('pounds-force', 4.448222, 0.),
#         ('dynes', 1.0e-5, 0.), ('kilogram-force', 9.80665, 0.))
#
#     class Length:
#         conversions = [
#             ('cms', 1.0, 0.),
#             ('meters', 1.0e2, 0.),
#             ('kilometers', 1.0e5, 0.),
#             ('inches', 2.54, 0.),
#             ('feet', 30.48, 0.),
#             ('yards', 91.44, 0.),
#             ('miles', 1.609344e5, 0.)
#         ]
#
#     class Mass:
#         conversions = [
#             ('grams', 1.0, 0.),
#             ('kilograms', 1.0e3, 0.),
#             ('ounces', 28.34952, 0.),
#             ('pounds', 453.59237, 0.),
#             ('tons', 9.07185e5, 0.)
#         ]
#
#     class Temperature:
#         conversions = (('Celsius', 1.0, 0.), ('Fahrenheit', 100./180, -160./9),
#         ('Kelvin', 1.0, -274.15))



class Converter:
    def __init__(self):
        self.conversion_data = {
            'length' : self.Length()
        }

    def convert(self, unit_type, unit_value, old_unit, new_unit):
        conversion_table = self.conversion_data[unit_type].conversions
        new_value = float(unit_value) * conversion_table[old_unit] / conversion_table[new_unit]
        return new_value

    class Length:
        conversions = {
            'centimeters'   :   1.0,
            'meters'        :   100,
            'yards'         :   91.44
        }

a = Converter()
# Mass, 1 unit, gram, pounds
print(a.convert('length',1,'meters','yards'))
