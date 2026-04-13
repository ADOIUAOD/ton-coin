import json

exact_symbol = "U\U000E00C8S\U000E00C9D\U000E00CA\U00016A4B"
data = {
  "name": "Tethee USD",
  "symbol": exact_symbol,
  "decimals": "9",
  "image": "https://i.postimg.cc/pr6dvdYC/1151.jpg"
}

# 强制锁定！指定生成到你的电脑桌面
desktop_path = r"C:\Users\40207\Desktop\manifest.json"

try:
    with open(desktop_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("✅ 大功告成！文件已经强制钉在你的桌面上了！")
except Exception as e:
    print("❌ 保存失败，可能是被杀毒软件拦截了:", e)