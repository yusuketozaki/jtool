import json
import argparse


def load_json(file_name):
    """
    指定されたファイル名のJSONデータをロード
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading JSON file: {e}")
        return None


def explore_json(data, path="root"):
    """
    JSONデータを再帰的に探索
    """
    if isinstance(data, dict):
        print(f"\nCurrent level: {path}")
        print("Keys available:")
        for key in data.keys():
            print(f"- {key}")

        user_input = input("\nEnter a key to explore, or '..' to go up, 'exit' to quit: ").strip()

        if user_input == "exit":
            return
        elif user_input == "..":
            return True
        elif user_input in data:
            return explore_json(data[user_input], f"{path}/{user_input}")
        else:
            print("Invalid key, please try again.")
            return explore_json(data, path)

    elif isinstance(data, list):
        print(f"\nCurrent level: {path}")
        print(f"This is a list with {len(data)} elements.")
        user_input = input("Enter an index to explore (0-based), or '..' to go up, 'exit' to quit: ").strip()

        if user_input == "exit":
            return
        elif user_input == "..":
            return True
        else:
            try:
                index = int(user_input)
                if 0 <= index < len(data):
                    return explore_json(data[index], f"{path}/{index}")
                else:
                    print("Invalid index, please try again.")
                    return explore_json(data, path)
            except ValueError:
                print("Please enter a valid index.")
                return explore_json(data, path)
    else:
        print(f"\nFinal value at {path}: {data}")
        input("Press Enter to go back.")
        return True


def start_inspector(file_name):
    """
    対話形式でJSONデータの探索を開始
    """
    data = load_json(file_name)
    if data is None:
        return

    print("#" * 40)
    print("Starting JSON inspector...")
    print("target file: ", file_name)
    print("#" * 40)

    while explore_json(data):
        pass


def main():
    parser = argparse.ArgumentParser(description="Interactive JSON Inspector")
    parser.add_argument('file_name', help='Path to the JSON file')

    args = parser.parse_args()
    start_inspector(args.file_name)


if __name__ == "__main__":
    main()
