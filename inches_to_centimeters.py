def inches_to_centimeters(inches):
    """
    Convert inches to centimeters.
    
    Args:
        inches (float): Length in inches.
        
    Returns:
        float: Length in centimeters.
    """
    return inches * 2.54

# 获取用户输入的英寸
inches = float(input("Enter length in inches: "))

# 调用 inches_to_centimeters 函数转换英寸为厘米
centimeters = inches_to_centimeters(inches)

# 打印转换后的厘米
print(f"Length in centimeters: {centimeters} cm")
