import subprocess
import sys
import traceback

reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]


try:
    if 'atomicwrites' in installed_packages:
        assert True
        print("1. PASS, atomicwrites is installed")
    else:
        print("1. FAIL atomicwrites is NOT installed")
except AssertionError:
    assert False


try:
    if 'attrs' in installed_packages:
        assert True
        print("2. PASS, attrs is installed")
    else:
         print("2. FAIL attrs is NOT installed")
except AssertionError:
    assert False

try:
    if 'beautifulsoup4' in installed_packages:
         assert True
         print("3. PASS, beautifulsoup4 is installed")
    else:
        print("3. FAIL beautifulsoup4 is NOT intalled")
except AssertionError:
    assert False

try:
    if 'requests' in installed_packages:
         assert True
         print("4. PASS, requests is installed")
    else:
        print("4. FAIL, requests is NOT installed")
except AssertionError:
    assert False

try:
    if 'idna' in installed_packages:
         assert True
         print( "5. PASS, idna is installed")
    else:
        print("5. FAIL, idna is NOT installed")
except AssertionError:
    assert False

try:

    if 'importlib-metadata' in installed_packages:
         assert True
         print("6. PASS, importlib-metadata is installed")
    else:
        print("6. FAIL, importlib-metadata is NOT installed")
except AssertionError:
    assert False

try:

    if 'more-itertools' in installed_packages:
         assert True
         print("7. PASS, more-itertools is installed")
    else:
        print("7. FAIL, more-itertools is NOT installed")
except AssertionError:
    assert False

try:
    if 'packaging' in installed_packages:
         assert True
         print("8. PASS packaging is installed")
    else:
        print("8. FAIL, packaging is NOT installed")
except AssertionError:
    assert False

try:

    if 'py' in installed_packages:
         assert True
         print("9. PASS, py is installed")
    else:
        print("9. FAIL, py is NOT installed")
except AssertionError:
    assert False
try:

    if 'pluggy' in installed_packages:
         assert True
         print("10. PASS, pluggy is installed")
    else:
        print("10. pluggy is NOT installed")
except AssertionError:
    assert False

try:

    if 'pyparsing' in installed_packages:
         assert True
         print("11. PASS, pyparsing is installed")
    else:
        print("11. FAIL, pyparsing is NOT installed")
except AssertionError:
    assert False
try:

    if 'six' in installed_packages:
         assert True
         print("12. PASS, six is installed")
    else:
        print("12. FAIL, six is NOT installed")
except AssertionError:
    assert False

try:
    if 'soupsieve' in installed_packages:
         assert True
         print("13. PASS, soupsieve is installed")
    else:
        print("13. FAIL, soupsieve is NOT installed")
except AssertionError:
    assert False
try:

    if 'urllib3' in installed_packages:
         assert True
         print("14. PASS, urllib3 is installed")
    else:
        print("14. FAIL, urllib3 is NOT installed")
except AssertionError:
    assert False
try:
    if 'wcwidth' in installed_packages:
         assert True
         print("15. PASS, wcwidth is installed")
    else:
        print("15. FAIL, wcwidth is NOT installed")
except AssertionError:
    assert False
try:
    if 'zipp' in installed_packages:
         assert True
         print("16. PASS, zipp is installed")
    else:
        print("16. FAIL, zipp is NOT installed")
except AssertionError:
    assert False
