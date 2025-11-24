import struct
import os

def get_png_dimensions(filepath):
    with open(filepath, 'rb') as f:
        data = f.read(24)
        if data[:8] == b'\x89PNG\r\n\x1a\n':
            w, h = struct.unpack('>LL', data[16:24])
            return w, h
    return None, None

# Check the uploaded slideshow image
image_file = 'static/uploads/slideshow_20251124_113332_Screenshot_2025-11-12_144603.png'

if os.path.exists(image_file):
    width, height = get_png_dimensions(image_file)
    
    if width and height:
        aspect_ratio = width / height
        file_size = os.path.getsize(image_file) / 1024  # KB
        
        # Check if 16:9
        is_16_9 = abs(aspect_ratio - (16/9)) < 0.01
        
        print("="*60)
        print("📷 UPLOADED IMAGE ANALYSIS")
        print("="*60)
        print(f"\n📁 File: {os.path.basename(image_file)}")
        print(f"📐 Resolution: {width} x {height} pixels")
        print(f"📊 Aspect Ratio: {aspect_ratio:.2f}:1")
        print(f"💾 File Size: {file_size:.1f} KB")
        
        print("\n" + "="*60)
        print("✅ ANALYSIS RESULT")
        print("="*60)
        
        if is_16_9:
            print("✅ PERFECT! Image is already 16:9 ratio")
            print("✅ No cropping needed")
            print("✅ Will display without distortion")
        else:
            recommended_height = int(width * 9 / 16)
            print(f"❌ Current ratio: {aspect_ratio:.2f}:1 (NOT 16:9)")
            print(f"⚠️  CROP NEEDED to avoid distortion")
            print(f"\n📝 RECOMMENDED ACTION:")
            print(f"   Crop/Resize to: {width} x {recommended_height} pixels")
            print(f"   OR")
            print(f"   Crop/Resize to: 1920 x 1080 pixels (Full HD 16:9)")
            
            # Calculate what's getting cut
            if aspect_ratio > (16/9):
                # Image is wider - sides will be cropped
                print(f"\n⚠️  CURRENT ISSUE: Image is TOO WIDE")
                print(f"   Left and right sides may be cut off in slideshow")
            else:
                # Image is taller - top/bottom will be cropped
                print(f"\n⚠️  CURRENT ISSUE: Image is TOO TALL")
                print(f"   Top and bottom may be cut off in slideshow")
        
        print("\n" + "="*60)
        print("💡 RECOMMENDATION FOR BEST DISPLAY:")
        print("="*60)
        print("📐 Ideal Size: 1920 x 1080 pixels (16:9)")
        print("📐 Minimum Size: 1600 x 900 pixels (16:9)")
        print("💾 File Size: < 500 KB")
        print("📝 Format: JPG or PNG")
        print("="*60)
    else:
        print("❌ Could not read image dimensions")
else:
    print(f"❌ File not found: {image_file}")
