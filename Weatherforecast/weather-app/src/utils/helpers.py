def format_temperature(temp):
    return f"{temp:.1f}°C"

def log_error(message):
    with open("error.log", "a") as error_file:
        error_file.write(message + "\n")