# YOLOTester

YOLOTester 是一個用於測試 YOLO 模型的 Python 專案。該專案可以自動檢查環境設置，自動下載測試影片，並使用 loguru 進行日誌記錄。

## 特性

- 環境檢查
- YOLO 模型載入
- 自動下載測試影片
- 日誌記錄

## 先決條件

- Python 3.8 以上
- pip 套件管理工具

## 安裝

1. 克隆此倉庫
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. 安裝所需的 Python 套件
    ```bash
    pip install -r requirements.txt
    ```

## 使用

1. 確保已經安裝 `ultralytics` 套件
    ```bash
    pip install ultralytics
    ```

2. 運行 YOLOTester
    ```bash
    python yolo_tester.py
    ```

## 文件結構

```plaintext
YOLOTester/
├── yolo_tester.py    # 主程式碼
├── requirements.txt  # 需要安裝的套件列表
├── README.md         # 本說明文件
└── yolotester.log    # 日誌文件（運行程式後生成）
```

## 範例輸出

運行成功後，你應該能在控制台中看到類似如下的輸出：

```plaintext
模型測試成功！
```

同時，`yolotester.log` 文件將包含詳細的日誌記錄，包括環境檢查結果、模型載入狀況以及測試過程中的各種訊息。

## 貢獻

如果你想要貢獻此專案，請先 fork 此倉庫，創建你的分支 (`git checkout -b feature-foo`)，提交你的修改 (`git commit -am 'Add some foo'`)，然後推送到分支 (`git push origin feature-foo`)。最後，創建一個新的 Pull Request。

## 版權

此專案採用 MIT 許可證。詳細內容請參見 LICENSE 文件。

