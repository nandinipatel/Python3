print(dir())

#if anything starts with "_", we shouldn't change it without a reason
#"_" means its private in its module

for m in dir(__builtins__):
    print(m)