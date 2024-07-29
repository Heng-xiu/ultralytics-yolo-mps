# 安裝 ultralytics
# %pip install ultralytics

from ultralytics import YOLO, checks
import torch
import os
from loguru import logger
import requests

class YOLOTester:
    def __init__(self, model_path: str = 'yolov8s.pt'):
        """
        初始化 YOLOTester 類別，載入指定的 YOLO 模型。

        :param model_path: YOLO 模型的檔案路徑
        """
        self.model_path = model_path
        self._setup_logging()
        self._perform_checks()
        self._load_model()

    def _setup_logging(self):
        """
        設定日誌記錄。
        """
        logger.add("yolotester.log", rotation="30 MB")
        logger.info("日誌記錄已設定。")

    def _perform_checks(self):
        """
        執行 ultralytics 環境檢查並記錄結果。
        """
        checks()
        logger.info("Ultralytics 環境檢查完成。")

    def _load_model(self):
        """
        載入 YOLO 模型。
        """
        if not torch.backends.mps.is_available():
            logger.error("MPS (Metal Performance Shaders) 不可用。")
            raise EnvironmentError("MPS (Metal Performance Shaders) 不可用。")
        self.model = YOLO(self.model_path)
        logger.info(f"成功載入模型：{self.model_path}")
    
    def test_model(self, source: str = 'people-detection.mp4', show: bool = False, conf: float = 0.1, save: bool = True):
        """
        測試 YOLO 模型，對指定的來源進行目標檢測。如果本地沒有影片，則自動下載。

        :param source: 輸入資料的來源（影片或圖片路徑）
        :param show: 是否顯示處理結果
        :param conf: 置信度閾值
        :param save: 是否保存處理結果
        :return: 處理結果
        """
        self._ensure_video_exists(source)
        logger.info(f"開始處理輸入檔案：{source}")
        try:
            results = self.model(source=source, show=show, conf=conf, save=save, device='mps')
            logger.info(f"處理完成，結果已保存：{save}")
            return results
        except Exception as e:
            logger.error(f"模型測試過程中發生錯誤：{e}")
            raise RuntimeError(f"模型測試過程中發生錯誤：{e}")

    def _ensure_video_exists(self, source):
        """
        確保測試影片檔案存在。如果不存在，則自動下載。
        """
        if not os.path.exists(source):
            logger.warning(f"輸入檔案不存在：{source}。開始下載測試影片...")
            self._download_video(source)

    def _download_video(self, source):
        """
        下載測試影片檔案。
        """
        video_url = 'https://github.com/intel-iot-devkit/sample-videos/blob/master/people-detection.mp4?raw=true'
        response = requests.get(video_url)
        if response.status_code == 200:
            with open(source, 'wb') as f:
                f.write(response.content)
            logger.info(f"測試影片下載完成：{source}")
        else:
            logger.error("測試影片下載失敗。請檢查網址或網路連接。")
            raise RuntimeError("測試影片下載失敗。")

# 使用範例
if __name__ == "__main__":
    tester = YOLOTester()
    try:
        results = tester.test_model()
        print("模型測試成功！")
    except (EnvironmentError, FileNotFoundError, RuntimeError) as e:
        print(e)
