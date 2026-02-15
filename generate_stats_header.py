
import base64

def generate_stats_header_svg():
    input_image = 'stats_logo.png'
    output_svg = 'header_stats_logo.svg'
    
    with open(input_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # SVG Dimensions
    width = 600
    height = 200 # increased height for logo
    
    # Monochrome Theme Colors
    bg_color = "transparent"
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
    <defs>
        <filter id="glow-stats">
            <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <style>
            .header-image {{
                animation: pulse 3s ease-in-out infinite;
                filter: drop-shadow(0 0 8px rgba(255, 255, 255, 0.4));
                transform-origin: center;
            }}
            
            @keyframes pulse {{
                0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 5px rgba(255, 255, 255, 0.4)); }}
                50% {{ transform: scale(1.02); filter: drop-shadow(0 0 12px rgba(255, 255, 255, 0.6)); }}
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
    generate_stats_header_svg()
