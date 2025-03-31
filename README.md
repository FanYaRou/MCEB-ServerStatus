# MCBE 伺服器狀態查詢程式

## 功能說明
- 此程式可查詢 Minecraft 基岩版伺服器即時狀態
- 輸入伺服器 IP 與埠號即可獲取以下資訊：
  - 伺服器名稱與版本
  - 當前在線玩家數量
  - 伺服器響應延遲
  - 最大玩家容量

## 環境需求
### 必要條件
- 需安裝 Python 3.7 或更新版本
- 需具備終端機操作權限

## 安裝步驟
1. 安裝必要套件：
```bash
pip install mcstatus
```

## 使用方式
- 執行指令：
```bash
python Status.py
```
## 注意事項
基岩版預設埠號為 19132
若連接失敗請檢查：
- 伺服器是否正常運作
- 防火牆設定是否允許 UDP 連接
- 輸入的 IP 與埠號是否正確

**願此工具助君暢遊方塊世界！**
