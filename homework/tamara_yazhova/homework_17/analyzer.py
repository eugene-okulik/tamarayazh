import argparse
import os


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("log_path", type=str, help="Path to logs")
    parser.add_argument("--text", type=str, help="Text to search", required=True)
    return parser.parse_args()


def search_in_files(log_path, search_text):
    results = []
    log_files = [os.path.join(log_path, file) for file in os.listdir(log_path) if file.endswith(".log")]
    for file_path in log_files:
        line_number = 0
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                line_number += 1
                words = line.split()

                if search_text in words:
                    index = words.index(search_text)
                    part_of_text = ' '.join(words[max(index - 5, 0): index + 6])
                    results.append((os.path.basename(file_path), line_number, part_of_text))
    return results


args = parse_arguments()
search_results = search_in_files(args.log_path, args.text)

if search_results:
    for file_path, line_number, part_of_text in search_results:
        print(f"Название файла: {file_path}\nНомер строки: {line_number}\nЧасть текста: {part_of_text}\n")
else:
    print("Не найдено")
