from mcstatus import BedrockServer
import socket

def check_bedrock_server():
    ip = input("🖥️ 请输入基岩版服务器 IP（例如：114.514.191.810）: ").strip()
    port = input("🔢 请输入端口（默认 19132，直接回车使用默认）: ").strip()
    port = int(port) if port else 19132

    try:
        socket.inet_aton(ip)
    except socket.error:
        print("❌ 无效的 IP 地址！")
        return

    try:
        server = BedrockServer(ip, port)
        status = server.status()

        print("\n✅ 服务器在线！")
        print(f"📌 IP: {ip}:{port}")
        print(f"🏷️ 服务器名称: {status.motd}")
        print(f"🛠️ 版本: {status.version.name}")
        print(f"👥 在线玩家: {status.players.online}/{status.players.max}")
        print(f"🏓 延迟: {status.latency:.2f} ms")

    except Exception as e:
        print(f"\n❌ 无法连接服务器: {e}")
        print("可能原因：服务器离线、端口错误、防火墙阻止或非基岩版服务器。")

if __name__ == "__main__":
    print("=== Minecraft 基岩版服务器状态查询 ===")
    check_bedrock_server()
    input("\n按 Enter 退出...")
