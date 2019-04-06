# rok narozeniny
petar=2010
marko=2011
dusan=2016

print("Petar je starsi nez Marko o",marko-petar,"rok")
print("petar je starsi nez dusan o",dusan-petar,"roku")
print("marko je starsi nez dusan o",dusan-marko,"roku")

igor=1975

print("igor je star nez petar o",petar - igor,"roku")

tentorok = 2019

print("petar ma ",tentorok - petar,"roku")
print("marko ma",tentorok - marko,"roku")
print("igor ma ",tentorok-igor,"roku")

for rok in (2019,2020,2025):
    print("v roce",rok,"marko bude mit",rok-marko)
    print("v roce",rok,"petar bude mit",rok - petar,"roku")

for rok in range(2020,2031):
    print("v roce",rok,"igor bude mit",rok - igor,"let")