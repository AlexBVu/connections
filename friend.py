class Friend:
        # ? Do I want to have some number for level of friend, or just name?
        def __init__(self, name: str, last_seen: int) -> None:
                self.name = name
                self.last_seen = last_seen 
                return

def main() -> None:
        # in main, have to include the friend. to get the import right
        friend1 = Friend("Alex", 0)
        print(f"I haven't seen {friend1.name} in {friend1.last_seen} days")

if __name__ == "__main__":
        main()
        
