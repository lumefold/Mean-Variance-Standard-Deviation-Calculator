from mean_var_std import calculate

if __name__ == "__main__":
    example = [0,1,2,3,4,5,6,7,8]
    print("Example input:", example)
    result = calculate(example)
    print("\nResult:")
    print(result)
    print("\nRun tests with: python3 -m unittest test_module.py")
