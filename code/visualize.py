def generate_digits_preview(number_str, first=50, last=50):
    """Генерирует превью первых и последних цифр."""
    preview = {}
    if len(number_str) > first:
        preview['first'] = number_str[:first] + "..."
    else:
        preview['first'] = number_str
    if len(number_str) > last:
        preview['last'] = "..." + number_str[-last:]
    else:
        preview['last'] = number_str
    return preview

# Использование
number_str = str(10 ** 10000)
preview = generate_digits_preview(number_str)
print(f"Превью: {preview['first']} {preview['last']}")
