import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from pathlib import Path
from typing import Tuple, Union

class ImageEncryptor:
    """
    A class for encrypting and decrypting images using pixel manipulation.
    Supports basic XOR encryption with configurable key.
    """
    
    def __init__(self):
        self._validate_dependencies()
        
    def _validate_dependencies(self) -> None:
        """Check required dependencies are available"""
        try:
            import numpy as np
            from PIL import Image
        except ImportError as e:
            raise ImportError(
                "Required dependencies not found. Please install Pillow and numpy: "
                "pip install pillow numpy matplotlib"
            ) from e

    def load_image(self, image_path: Union[str, Path]) -> np.ndarray:
        """
        Load image from file and convert to numpy array
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Numpy array of the image
            
        Raises:
            FileNotFoundError: If image file doesn't exist
            ValueError: If image cannot be loaded
        """
        path = Path(image_path)
        if not path.exists():
            raise FileNotFoundError(f"Image file not found: {image_path}")
            
        try:
            with Image.open(path) as img:
                if img.mode not in ('RGB', 'RGBA'):
                    img = img.convert('RGB')
                return np.array(img)
        except Exception as e:
            raise ValueError(f"Failed to load image: {e}") from e

    def save_image(self, image_array: np.ndarray, output_path: Union[str, Path]) -> None:
        """
        Save numpy array as image file
        
        Args:
            image_array: Image data as numpy array
            output_path: Path to save the output image
            
        Raises:
            ValueError: If image cannot be saved
        """
        try:
            img = Image.fromarray(image_array)
            img.save(output_path)
        except Exception as e:
            raise ValueError(f"Failed to save image: {e}") from e

    def display_image(self, image_array: np.ndarray, title: str = "Image") -> None:
        """
        Display image using matplotlib
        
        Args:
            image_array: Image data as numpy array
            title: Title for the plot
        """
        plt.figure()
        plt.imshow(image_array)
        plt.title(title)
        plt.axis('off')
        plt.show()

    def _validate_key(self, key: int) -> int:
        """Validate and normalize encryption key"""
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")
        return key % 256  # Ensure key is in 0-255 range

    def encrypt_image(self, image_array: np.ndarray, key: int) -> np.ndarray:
        """
        Encrypt image by performing XOR operation on each pixel with the key
        
        Args:
            image_array: Original image as numpy array
            key: Encryption key (0-255)
            
        Returns:
            Encrypted image array
        """
        key = self._validate_key(key)
        return np.bitwise_xor(image_array, key)

    def decrypt_image(self, encrypted_array: np.ndarray, key: int) -> np.ndarray:
        """
        Decrypt image by performing XOR operation again
        
        Args:
            encrypted_array: Encrypted image as numpy array
            key: Encryption key (same as used for encryption)
            
        Returns:
            Decrypted image array
        """
        # Decryption is same as encryption for XOR
        return self.encrypt_image(encrypted_array, key)

    def process_image(
        self,
        operation: str,
        input_path: Union[str, Path],
        output_path: Union[str, Path],
        key: int,
        show_results: bool = True
    ) -> None:
        """
        Process image with encryption or decryption
        
        Args:
            operation: 'encrypt' or 'decrypt'
            input_path: Path to input image
            output_path: Path to save output image
            key: Encryption/decryption key
            show_results: Whether to display before/after images
            
        Raises:
            ValueError: For invalid operations or processing errors
        """
        try:
            # Load image
            img_array = self.load_image(input_path)
            
            if operation.lower() == 'encrypt':
                processed = self.encrypt_image(img_array, key)
                action = "Encryption"
            elif operation.lower() == 'decrypt':
                processed = self.decrypt_image(img_array, key)
                action = "Decryption"
            else:
                raise ValueError("Operation must be 'encrypt' or 'decrypt'")
            
            # Save result
            self.save_image(processed, output_path)
            
            # Show results if requested
            if show_results:
                self.display_image(img_array, f"Original Image ({action})")
                self.display_image(processed, f"Processed Image ({action})")
                
            print(f"{action} completed successfully. Output saved to {output_path}")
            
        except Exception as e:
            raise ValueError(f"Image processing failed: {e}") from e


def get_user_input() -> Tuple[str, str, str, int]:
    """Get user input for image processing"""
    print("\nImage Encryption Tool")
    print("=" * 40)
    
    while True:
        operation = input("Choose operation (encrypt/decrypt): ").lower()
        if operation in ('encrypt', 'decrypt'):
            break
        print("Invalid operation. Please enter 'encrypt' or 'decrypt'")
    
    while True:
        input_path = input("Enter input image path: ").strip()
        if Path(input_path).exists():
            break
        print("File not found. Please enter a valid image path")
    
    output_path = input("Enter output image path: ").strip()
    
    while True:
        try:
            key = int(input("Enter encryption key (0-255): "))
            if 0 <= key <= 255:
                break
            print("Key must be between 0 and 255")
        except ValueError:
            print("Please enter a valid integer key")
    
    return operation, input_path, output_path, key


def main():
    """Main application entry point"""
    encryptor = ImageEncryptor()
    
    try:
        operation, input_path, output_path, key = get_user_input()
        encryptor.process_image(
            operation=operation,
            input_path=input_path,
            output_path=output_path,
            key=key
        )
    except Exception as e:
        print(f"\nError: {e}")
        print("Operation failed. Please check your inputs and try again.")
    finally:
        print("\nOperation completed. Exiting program.")


if __name__ == "__main__":
    main()