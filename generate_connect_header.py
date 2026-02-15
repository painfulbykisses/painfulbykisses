
import base64

def generate_connect_header_svg():
    input_image = 'connect_logo.png'
    output_svg = 'header_connect_logo.svg'
    
    with open(input_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # SVG Dimensions
    width = 600
    height = 200 # increased height for logo
    
    # Monochrome Theme Colors
    bg_color = "transparent"
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <filter id="glow-connect">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <style>
            .header-image {{
                animation: drip-float 4s ease-in-out infinite;
                filter: drop-shadow(0 0 6px rgba(255, 255, 255, 0.4));
                transform-origin: center top;
            }}
            
            @keyframes drip-float {{
                0% {{ transform: translateY(0) scaleY(1); }}
                50% {{ transform: translateY(12px) scaleY(1.05); }}
                100% {{ transform: translateY(0) scaleY(1); }}
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
    generate_connect_header_svg()
