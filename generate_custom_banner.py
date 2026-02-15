
import base64

def generate_banner_svg():
    input_image = 'banner_dezikrie.png'
    output_svg = 'banner.svg'
    
    with open(input_image, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    
    # SVG Dimensions
    width = 800
    height = 300
    
    # Monochrome Theme Colors
    bg_color = "#111111"  # Very dark grey/black
    fg_color = "#FFFFFF"  # White
    accent_color = "#333333" # Dark grey
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" style="background-color: {bg_color}; font-family: 'Verdana', sans-serif;">
    <defs>
        <filter id="monochrome-shimmer">
             <feColorMatrix type="matrix" values="0.3333 0.3333 0.3333 0 0
                                                  0.3333 0.3333 0.3333 0 0
                                                  0.3333 0.3333 0.3333 0 0
                                                  0      0      0      1 0"/>
        </filter>
        <filter id="glow">
            <feGaussianBlur stdDeviation="2.5" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <style>
            .banner-image {{
                animation: float 6s ease-in-out infinite;
                filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.3));
            }}
            .particle {{
                fill: {fg_color};
                opacity: 0.5;
                animation: particle-rise 10s infinite linear;
            }}
            @keyframes float {{
                0%, 100% {{ transform: translate(0, 0); }}
                50% {{ transform: translate(0, -10px); }}
            }}
            @keyframes particle-rise {{
                0% {{ transform: translateY(0) scale(0.5); opacity: 0; }}
                20% {{ opacity: 0.5; }}
                80% {{ opacity: 0.5; }}
                100% {{ transform: translateY(-100px) scale(1); opacity: 0; }}
            }}
        </style>
    </defs>
    
    <!-- Background Particles for Elegance -->
    <circle cx="100" cy="300" r="2" class="particle" style="animation-delay: 0s" />
    <circle cx="300" cy="320" r="3" class="particle" style="animation-delay: 2s" />
    <circle cx="500" cy="310" r="2" class="particle" style="animation-delay: 4s" />
    <circle cx="700" cy="330" r="1.5" class="particle" style="animation-delay: 6s" />
    <circle cx="200" cy="350" r="2.5" class="particle" style="animation-delay: 1s" />
    <circle cx="600" cy="340" r="2" class="particle" style="animation-delay: 3s" />

    <!-- Centered Animated Image -->
    <!-- Assuming the image is roughly centered in ratio, we scale it to fit nicely -->
    <image x="150" y="50" width="500" height="200" xlink:href="data:image/png;base64,{encoded_string}" class="banner-image" />
    
</svg>'''
    
    with open(output_svg, 'w') as f:
        f.write(svg_content)
    print(f"Generated {output_svg}")

if __name__ == "__main__":
    generate_banner_svg()
