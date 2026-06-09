import os
import re
import subprocess
import glob

README_PATH = "README.md"


def get_existing_notebooks_in_readme():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    return re.findall(r"##\s+\d+\.\s+(\S+)", content)


def get_next_number():
    with open(README_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    numbers = re.findall(r"##\s+(\d+)\.", content)
    return max(int(n) for n in numbers) + 1 if numbers else 1


def get_new_notebooks():
    all_notebooks = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob("*.ipynb")]
    existing = get_existing_notebooks_in_readme()
    return [nb for nb in all_notebooks if nb not in existing]


def multiline_input(prompt):
    print(prompt)
    print("(입력 완료 후 빈 줄에서 Enter 두 번)")
    lines = []
    empty_count = 0
    while True:
        line = input()
        if line == "":
            empty_count += 1
            if empty_count >= 2:
                break
        else:
            empty_count = 0
            lines.append(line)
    return " ".join(lines)


def build_readme_section(number, title, goal, dataset, description, blog_urls):
    blog_lines = "\n".join(blog_urls) if blog_urls else ""
    return (
        f"\n## {number}. {title}\n"
        f"목표 : {goal}  \n"
        f"활용 데이터셋 : {dataset}  \n\n"
        f"{description}  \n\n\n"
        f"블로그 주소 :  \n"
        f"{blog_lines}  \n"
        f"<br><br><br>\n"
    )


def main():
    print("=" * 50)
    print("  README 자동 업데이트 스크립트")
    print("=" * 50)

    new_notebooks = get_new_notebooks()

    if new_notebooks:
        print("\nREADME에 없는 노트북:")
        for i, nb in enumerate(new_notebooks, 1):
            print(f"  {i}. {nb}")
        print(f"  {len(new_notebooks)+1}. 직접 입력")

        choice = input("\n선택 (번호): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(new_notebooks):
            title = new_notebooks[int(choice) - 1]
        else:
            title = input("노트북 이름 입력: ").strip()
    else:
        title = input("\n프로젝트 제목 입력: ").strip()

    print()
    goal = input("목표 : ").strip()
    dataset = input("활용 데이터셋 : ").strip()
    print()
    description = multiline_input("내용 설명 :")

    print("\n블로그 주소 입력 (없으면 Enter, 여러 개면 한 줄씩 입력, 완료 시 빈 줄 Enter)")
    blog_urls = []
    while True:
        url = input().strip()
        if url == "":
            break
        blog_urls.append(url)

    number = get_next_number()
    section = build_readme_section(number, title, goal, dataset, description, blog_urls)

    print("\n" + "=" * 50)
    print("  미리보기")
    print("=" * 50)
    print(section)
    print("=" * 50)

    confirm = input("README에 추가할까요? (y/n): ").strip().lower()
    if confirm != "y":
        print("취소했습니다. README는 변경되지 않았습니다.")
        return

    with open(README_PATH, "a", encoding="utf-8") as f:
        f.write(section)

    print(f"\nREADME에 '{number}. {title}' 추가 완료!")

    push = input("\ngit commit & push 할까요? (y/n): ").strip().lower()
    if push == "y":
        files_to_add = ["README.md"]
        notebook_file = f"{title}.ipynb"
        if os.path.exists(notebook_file):
            files_to_add.append(notebook_file)
        subprocess.run(["git", "add"] + files_to_add, check=True)
        commit_msg = f"Update README: add {title}"
        subprocess.run(["git", "commit", "-m", commit_msg], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("Push 완료!")
    else:
        print("README만 업데이트했어요. 나중에 직접 push해주세요.")


if __name__ == "__main__":
    main()
