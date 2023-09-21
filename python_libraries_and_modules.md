### Functions
- DRY - Dont repeat yourself 

### Libraries and modules
- **module** - single file of functions, classes, variables etc. Bring in and use in other python files
- **library** - collection of modules. Needs to be installed iwth pip 

##### Examples of libraries 
1. Requests - Making HTTP requests simpler
2. Matplotlib - Good for creating graphs and data visualisation
3. NumPy - good for scientific and numerical computing
4. Pandas - good for data science for scientific and mathmatical commands.
5. Random - generate random items/numbers/strings
6. SciPy - data visualisation and manipulation
7. Math - basic maths functions 

#### Examples of using libraries

1. Math Library
```print(math.ceil(num_float))```

2. Random library

```
rand_num = random.randint(1,10)
print(rand_num)
```

3. Request Library 

```
requests_bbc = requests.get("https://www.bbc.co.uk/")
print(requests_bbc.content)
```