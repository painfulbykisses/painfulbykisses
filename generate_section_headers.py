
def generate_section_svg(text, filename):
    width = 600
    height = 80
    
    # Monochrome Theme
    bg_color = "transparent"
    fg_color = "#FFFFFF" 
    accent_color = "#CCCCCC"
    
    svg_content = f'''<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <defs>
        <filter id="glow-{filename}">
            <feGaussianBlur stdDeviation="2" result="coloredBlur"/>
            <feMerge>
                <feMergeNode in="coloredBlur"/>
                <feMergeNode in="SourceGraphic"/>
            </feMerge>
        </filter>
        <style>
            .header-text {{
                font-family: 'Verdana', sans-serif;
                font-size: 40px;
                font-weight: 900;
                fill: {fg_color};
                stroke: {accent_color};
                stroke-width: 1px;
                text-transform: uppercase;
                filter: url(#glow-{filename});
                letter-spacing: 4px;
            }}
            .underline {{
                stroke: {fg_color};
                stroke-width: 2;
                stroke-dasharray: 10,5;
                animation: dash 30s linear infinite;
            }}
            @keyframes dash {{
                to {{ stroke-dashoffset: -1000; }}
            }}
        </style>
    </defs>
    
    <!-- Text -->
    <text x="50%" y="50%" text-anchor="middle" dominant-baseline="middle" class="header-text">{text}</text>
    
    <!-- Animated Underline -->
    <line x1="100" y1="70" x2="500" y2="70" class="underline" />
    
    <!-- Decorative Stars -->
    <path d="M50,40 L55,45 L60,40 L55,35 Z" fill="{fg_color}">
        <animateTransform attributeName="transform" type="rotate" from="0 55 40" to="360 55 40" dur="4s" repeatCount="indefinite"/>
    </path>
    <path d="M540,40 L545,45 L550,40 L545,35 Z" fill="{fg_color}">
        <animateTransform attributeName="transform" type="rotate" from="0 545 40" to="-360 545 40" dur="5s" repeatCount="indefinite"/>
    </path>

</svg>'''
    
    with open(filename, 'w') as f:
        f.write(svg_content)
    print(f"Generated {filename}")

if __name__ == "__main__":
    generate_section_svg("Tech Stack", "header_tech.svg")
    generate_section_svg("Stats & Streaks", "header_stats.svg")
    generate_section_svg("Connect", "header_connect.svg")
