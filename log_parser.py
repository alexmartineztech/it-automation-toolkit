def parse_logs(file):
    with open(file, "r") as f:
        for line in f:
            if "ERROR" in line:
                print(line.strip())

if __name__ == "__main__":
    parse_logs("system.log")
