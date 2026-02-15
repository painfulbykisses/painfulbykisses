
import base64

def generate_header_svg():
    input_image = 'stack_logo.png'
    output_svg = 'header_tech_logo.svg'
    
    with open(input_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # SVG Dimensions
    width = 600
    height = 200 # increased height for logo
    
    # Monochrome Theme Colors
    bg_color = "transparent"
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <filter id="glow">
            <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <style>
            .header-image {{
                animation: float 4s ease-in-out infinite;
                filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.5));
                transform-origin: center;
            }}
            
            @keyframes float {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-8px); }}
            }}
        </style>
    </defs>
    
    <!-- Centered Animated Image -->
    <image x="100" y="25" width="400" height="150" xlink:href="data:image/png;base64,{encoded_string}" class="header-image" preserveAspectRatio="xMidYMid meet" />
    
</svg>'''
    
    with open(output_svg, 'w') as f:
        f.write(svg_content)
    print(f"Generated {output_svg}")

if __name__ == "__main__":
    generate_header_svg()
