# pdbrc
pdbrc and pdbrc.py for pdb++ (aka pdbpp)

Prequisite is to have pdbpp
```
pip install pdbpp
```

Copy these files to your home directory

```
cp .pdbrc $HOME
cp .pdbrc.py $HOME
```

Begin debugging
```
python -m pdb somefile.py

# go to main and stop
g main

# if in a class init for example, show class var, self.somevar
psv somevar
```
