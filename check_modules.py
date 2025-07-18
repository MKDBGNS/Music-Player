import pytgcalls
import os

print("\n🔍 Checking pytgcalls installation...")

try:
    # Show installed location
    print("✅ Installed at:", pytgcalls.__path__)
    
    # List contents of types/stream
    stream_path = os.path.join(pytgcalls.__path__[0], "types", "stream")
    print("📁 Contents of types/stream:")
    print(os.listdir(stream_path))
    
    # List contents of types/input_stream
    input_path = os.path.join(pytgcalls.__path__[0], "types", "input_stream")
    print("📁 Contents of types/input_stream:")
    print(os.listdir(input_path))
except Exception as e:
    print("❌ Error during inspection:", e)
