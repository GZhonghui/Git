import os, time, datetime

def main():
    with open("pack_log_leaset.txt", "w") as f:
        print(f"leaset pack time: {datetime.datetime.now()}", file=f)
    
    with open(f"pack_result_leaset.txt", "w") as f:
        print(f"leaset pack time: {datetime.datetime.now()}", file=f)
        print(f"leaset pack files: {os.listdir()}", file=f)

if __name__ == "__main__":
    main()