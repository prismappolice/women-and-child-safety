import os
import base64
import time
import io
from werkzeug.utils import secure_filename

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    print("PIL not installed. Install with: pip install Pillow")
    Image = None
    PIL_AVAILABLE = False

class ImageManager:
    """
    Manages image storage for both development and production environments
    """
    
    def __init__(self, upload_folder='static/uploads'):
        self.upload_folder = upload_folder
        self.max_size = (1400, 1000)  # Increased max dimensions for better quality
        
    def save_image(self, file, prefix='image'):
        """
        Save image and return appropriate URL/path
        """
        try:
            # Create filename
            timestamp = int(time.time())
            filename = f"{prefix}_{timestamp}_{secure_filename(file.filename)}"
            
            # For production, you might want to save to cloud
            # For now, saving locally
            os.makedirs(self.upload_folder, exist_ok=True)
            file_path = os.path.join(self.upload_folder, filename)
            
            if PIL_AVAILABLE:
                # Reset file pointer to beginning
                file.seek(0)
                
                # Open and process image
                image = Image.open(file)
                
                # Convert to RGB if necessary (handles RGBA, P mode images)
                if image.mode in ('RGBA', 'P', 'LA'):
                    # Create white background
                    background = Image.new('RGB', image.size, (255, 255, 255))
                    if image.mode == 'P':
                        image = image.convert('RGBA')
                    if image.mode in ('RGBA', 'LA'):
                        background.paste(image, mask=image.split()[-1])  # Use alpha channel as mask
                        image = background
                elif image.mode != 'RGB':
                    image = image.convert('RGB')
                
                # Resize image while maintaining aspect ratio
                image.thumbnail(self.max_size, Image.Resampling.LANCZOS)
                
                # For images close to target size (like 568x500), preserve original quality
                width, height = image.size
                
                # Calculate aspect ratio
                aspect_ratio = width / height
                container_ratio = 450 / 450  # Square-ish container
                
                # If image aspect ratio is close to container, preserve it
                if 0.8 <= aspect_ratio <= 1.4:  # Good ratio for containers
                    # Keep original size if it's reasonable
                    if width >= 400 and height >= 300:
                        pass  # Don't resize, keep original quality
                    else:
                        # Scale up proportionally to minimum size
                        scale_factor = max(500/width, 400/height)
                        new_width = int(width * scale_factor)
                        new_height = int(height * scale_factor)
                        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                else:
                    # For very wide or tall images, resize to fit container better
                    if aspect_ratio > 1.5:  # Very wide
                        new_height = 450
                        new_width = int(new_height * aspect_ratio)
                        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                    elif aspect_ratio < 0.7:  # Very tall
                        new_width = 450
                        new_height = int(new_width / aspect_ratio)
                        image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
                
                # Save optimized image with maximum quality for clarity
                image.save(file_path, 'JPEG', optimize=True, quality=100, progressive=True)
                print(f"Image saved and optimized: {filename}")
            else:
                # Reset file pointer and save directly without resizing if PIL not available
                file.seek(0)
                file.save(file_path)
                print(f"Image saved without optimization: {filename}")
            
            # Return web-accessible path (ensure correct format)
            return f'/static/uploads/{filename}'
            
        except Exception as e:
            print(f"Error saving image: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def get_base64_image(self, file):
        """
        Convert image to base64 for database storage
        Useful for small images that need to work across systems
        """
        if not PIL_AVAILABLE:
            print("PIL not available - cannot convert to base64")
            return None
            
        try:
            # Resize image
            image = Image.open(file)
            image.thumbnail((400, 300), Image.Resampling.LANCZOS)
            
            # Convert to base64
            buffer = io.BytesIO()
            image.save(buffer, format='JPEG', optimize=True, quality=80)
            img_data = buffer.getvalue()
            
            base64_string = base64.b64encode(img_data).decode()
            return f"data:image/jpeg;base64,{base64_string}"
            
        except Exception as e:
            print(f"Error converting to base64: {e}")
            return None
    
    def cleanup_old_images(self, days=30):
        """
        Clean up old images from uploads folder
        """
        try:
            import time
            import glob
            
            cutoff_time = time.time() - (days * 24 * 60 * 60)
            pattern = os.path.join(self.upload_folder, '*')
            
            for file_path in glob.glob(pattern):
                if os.path.getctime(file_path) < cutoff_time:
                    os.remove(file_path)
                    print(f"Cleaned up old image: {file_path}")
                    
        except Exception as e:
            print(f"Error cleaning up images: {e}")

# Usage example:
"""
# In your Flask app:
from image_manager import ImageManager

image_manager = ImageManager()

# Save image normally (for development/local hosting)
image_url = image_manager.save_image(request.files['image'], 'success_story')

# Or save as base64 (works anywhere but larger database)
base64_image = image_manager.get_base64_image(request.files['image'])
"""
