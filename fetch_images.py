import os
from rembg import remove

def process_images():
    os.makedirs('assets/processed', exist_ok=True)
    
    input_path = r"C:\Users\Acer\.gemini\antigravity\brain\751fa247-5074-408d-b083-1cae5e0d6c17\flower_0_1779210450435.png"
    
    print(f"Processing image {input_path} (removing background)...")
    try:
        with open(input_path, 'rb') as i_f:
            input_data = i_f.read()
            output_data = remove(input_data)
        
        for i in range(4):
            processed_path = f'assets/processed/flower_{i}.png'
            with open(processed_path, 'wb') as o_f:
                o_f.write(output_data)
            print(f"Saved processed image {i}")
    except Exception as e:
        print(f"Failed to process image: {e}")

if __name__ == "__main__":
    process_images()
