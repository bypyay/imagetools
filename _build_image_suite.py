import os
import re
import json
import shutil

BASE_DIR = r"D:\Codding\Claude Cowork code\Image Tools"
SITE_URL = "https://bypyay.github.io/imagetools"
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CSS_DIR = os.path.join(ASSETS_DIR, "css")
JS_TOOLS_DIR = os.path.join(ASSETS_DIR, "js", "image-tools")

# All 27 Image Tools with SEO metadata
IMAGE_TOOLS = [
    # 1. Compress
    {
        "slug": "compress-image-kb",
        "name": "Compress Image to KB",
        "category": "compress",
        "color": "#e5322d",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 12v9"/><path d="m8 17 4 4 4-4"/></svg>',
        "title": "Compress Image to Specific KB Online Free — Reduce Image Size in KB",
        "desc": "Reduce image size to exact KB (20KB, 50KB, 100KB, 200KB, etc.) online for free. Perfect for government exam forms, passport applications, and websites. 100% browser-based.",
        "h1": "Compress Image to Exact KB Online",
        "tagline": "Reduce JPEG, PNG, or WebP file size to your exact target KB with intelligent binary-search quality optimization.",
        "faqs": [
            ("How do I compress an image to exact 20KB or 50KB?", "Upload your photo, type your target KB value (e.g. 20 or 50), or click one of the quick preset chips. The tool will automatically optimize the image quality to match your target file size."),
            ("Is my uploaded image secure and private?", "Yes, 100%! All compression is processed locally in your browser memory using HTML5 Canvas. Your photos are never uploaded to any remote server.")
        ]
    },
    {
        "slug": "increase-image-kb",
        "name": "Increase Image Size in KB",
        "category": "compress",
        "color": "#d97706",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 14.899A7 7 0 1 1 15.71 8h1.79a4.5 4.5 0 0 1 2.5 8.242"/><path d="M12 21v-9"/><path d="m8 16 4-4 4 4"/></svg>',
        "title": "Increase Image Size in KB Online — Expand Image File Size Safely",
        "desc": "Increase image size in KB without distorting quality to meet minimum upload requirements for government job portals, exam forms, and visa applications.",
        "h1": "Increase Image File Size in KB Online",
        "tagline": "Safely expand photo file size to satisfy strict minimum upload requirements on application portals.",
        "faqs": [
            ("Why do government portals have minimum file size limits?", "Many application systems require photos to be at least 20KB or 50KB to ensure they aren't thumbnail-sized. This tool safely pads the file to meet that requirement.")
        ]
    },

    # 2. Passport & Exam
    {
        "slug": "passport-photo-maker",
        "name": "Passport Photo Maker",
        "category": "passport",
        "color": "#2563eb",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="12" cy="10" r="3"/><path d="M7 18c0-2.5 2.2-4 5-4s5 1.5 5 4"/></svg>',
        "title": "Online Passport Photo Maker — 3.5x4.5cm, 35x45mm, 2x2 Inch ID Photos",
        "desc": "Create standard passport photos online for free. Supports 3.5x4.5cm, 35x45mm, 2x2 inch visa sizes with white/blue background and printable 4x6 / A4 multi-photo sheets.",
        "h1": "Free Online Passport &amp; Visa Photo Maker",
        "tagline": "Generate official biometric passport photos with white or blue backgrounds and download printable multi-photo sheets.",
        "faqs": [
            ("What are standard passport photo dimensions?", "In India and UK/Europe, 3.5x4.5cm (35x45mm) is standard. In the US, 2x2 inches (51x51mm) is required. Both presets are supported.")
        ]
    },
    {
        "slug": "exam-photo-resizer",
        "name": "Govt Exam Photo Resizer",
        "category": "passport",
        "color": "#7c3aed",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>',
        "title": "Govt Exam Photo Resizer — SSC, UPSC, PAN Card, Railway, IBPS Specs",
        "desc": "1-click photo and signature resizer for Indian government competitive exams (SSC CGL/CHSL, UPSC, IBPS Bank, Railway RRB, and PAN Card).",
        "h1": "Govt Exam Photo &amp; Signature Resizer",
        "tagline": "Instant 1-click photo and signature dimension & KB presets for all major competitive recruitment portals.",
        "faqs": [
            ("Which exam presets are available?", "We provide instant 1-click formatting for SSC, UPSC Civil Services, IBPS Bank PO/Clerk, Railway RRB, NTA NEET/JEE, and NSDL PAN Card.")
        ]
    },
    {
        "slug": "add-name-date-photo",
        "name": "Add Name & Date on Photo",
        "category": "passport",
        "color": "#059669",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="16" rx="2"/><line x1="7" y1="15" x2="17" y2="15"/><line x1="7" y1="18" x2="13" y2="18"/></svg>',
        "title": "Add Name and Date on Photo Online — DOP & DOB Photo Generator",
        "desc": "Stamp candidate Name and Date of Photo (DOP) or Date of Birth (DOB) at the bottom of exam photos online. Required for SSC, Police, and state recruitment forms.",
        "h1": "Add Candidate Name &amp; Date on Photo",
        "tagline": "Add official white strip with candidate name and Date of Photo (DOP) at the bottom of passport photos.",
        "faqs": [
            ("Is Name and Date mandatory for SSC exams?", "Yes, SSC notification requires candidate name and the date on which the photograph was taken (DOP) clearly printed at the bottom.")
        ]
    },
    {
        "slug": "merge-photo-signature",
        "name": "Merge Photo & Signature",
        "category": "passport",
        "color": "#0891b2",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="10" rx="2"/><rect x="3" y="15" width="18" height="6" rx="2"/></svg>',
        "title": "Merge Photo and Signature Online — Combine Photo & Sign in One File",
        "desc": "Combine candidate photograph and handwritten signature into a single unified image file for online application portals.",
        "h1": "Merge Photo &amp; Signature Online",
        "tagline": "Combine portrait photo and signature card vertically into a single uploadable image file.",
        "faqs": [
            ("How do I combine photo and signature?", "Upload your photo in box 1 and signature in box 2, click Merge, and download the combined image instantly.")
        ]
    },

    # 3. Resize & Crop
    {
        "slug": "resize-image-pixels",
        "name": "Resize by Pixels",
        "category": "resize",
        "color": "#ea580c",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="15 3 21 3 21 9"/><polyline points="9 21 3 21 3 15"/><line x1="21" y1="3" x2="14" y2="10"/><line x1="3" y1="21" x2="10" y2="14"/></svg>',
        "title": "Resize Image in Pixels Online — Change Width & Height (px)",
        "desc": "Resize JPG, PNG, and WebP image dimensions in exact pixels with aspect ratio preservation and percentage scaling.",
        "h1": "Resize Image by Pixels Online",
        "tagline": "Change image width and height dimensions with pixel precision and aspect ratio lock.",
        "faqs": [
            ("Can I maintain original proportions?", "Yes, aspect ratio lock is enabled by default so your images never look stretched or squished.")
        ]
    },
    {
        "slug": "resize-image-cm-mm",
        "name": "Resize in CM / MM / Inches",
        "category": "resize",
        "color": "#0d9488",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><line x1="6" y1="6" x2="6" y2="10"/><line x1="10" y1="6" x2="10" y2="8"/><line x1="14" y1="6" x2="14" y2="10"/><line x1="18" y1="6" x2="18" y2="8"/></svg>',
        "title": "Resize Image in CM, MM, Inches Online — Print Dimensions with DPI",
        "desc": "Resize photos to exact real-world print dimensions (cm, mm, inch) with 150, 300, 600 DPI resolution settings.",
        "h1": "Resize Image in CM, MM &amp; Inches",
        "tagline": "Convert physical print dimensions (centimeters, millimeters, inches) into high-resolution pixel matrices.",
        "faqs": [
            ("What DPI should I choose for print?", "300 DPI is standard professional quality for paper and photo printing.")
        ]
    },
    {
        "slug": "crop-image",
        "name": "Crop Image",
        "category": "resize",
        "color": "#0284c7",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 2v14a2 2 0 0 0 2 2h14"/><path d="M18 22V8a2 2 0 0 0-2-2H2"/></svg>',
        "title": "Crop Image Online Free — Circle, 1:1 Square, 16:9 & Custom Crop",
        "desc": "Crop JPG, PNG, and WebP images online with interactive circular, 1:1 square, 16:9 widescreen, and freeform bounding boxes.",
        "h1": "Crop Image Online for Free",
        "tagline": "Cut out unnecessary margins, make circular profile avatars, or crop to social media aspect ratios.",
        "faqs": [
            ("Can I crop photos into a perfect circle?", "Yes! Choose the 'Circle Avatar' preset to crop profile pictures with a clean circular mask.")
        ]
    },
    {
        "slug": "instagram-grid-maker",
        "name": "Instagram 3x3 Grid Splitter",
        "category": "resize",
        "color": "#c026d3",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="3" y1="15" x2="21" y2="15"/><line x1="9" y1="3" x2="9" y2="21"/><line x1="15" y1="3" x2="15" y2="21"/></svg>',
        "title": "Instagram 3x3 Grid Maker — Split Panorama Photos for Instagram Profile",
        "desc": "Slice panorama photos into 3x3, 3x2, or 3x1 numbered square tiles for giant Instagram feed grids. Download all tiles packaged in a ZIP.",
        "h1": "Instagram 3x3 Grid Photo Splitter",
        "tagline": "Slice panoramic photos into numbered square tiles to create giant grid banners on your Instagram profile.",
        "faqs": [
            ("How do I post the split grid on Instagram?", "Upload the numbered tiles starting from tile 9 to tile 1 so they align perfectly on your profile feed.")
        ]
    },
    {
        "slug": "bulk-image-resizer",
        "name": "Bulk Image Resizer",
        "category": "resize",
        "color": "#4f46e5",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="8" y="8" width="13" height="13" rx="2"/><path d="M4 16V4a2 2 0 0 1 2-2h12"/></svg>',
        "title": "Bulk Image Resizer Online — Batch Resize Multiple Photos to ZIP",
        "desc": "Resize dozens of JPG, PNG, and WebP photos simultaneously. Set max dimensions or percentage and download all resized photos in a ZIP.",
        "h1": "Bulk Image Resizer &amp; Batch Processor",
        "tagline": "Resize hundreds of photos simultaneously in seconds and download them packaged in a single ZIP file.",
        "faqs": [
            ("How many photos can I batch resize?", "You can select 20, 50, or 100+ images at once. Processing runs client-side with parallel canvas pipelines.")
        ]
    },

    # 4. Convert
    {
        "slug": "png-to-jpg",
        "name": "PNG to JPG",
        "category": "convert",
        "color": "#e11d48",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>',
        "title": "PNG to JPG Converter Online Free — Fast Transparent PNG to JPG",
        "desc": "Convert transparent or high-res PNG images to standard JPG format with clean white background fill and quality control.",
        "h1": "Convert PNG to JPG Online",
        "tagline": "Convert lossless PNG images into universally compatible JPEG format with adjustable quality.",
        "faqs": [
            ("What happens to transparency in PNG?", "Transparent areas are cleanly filled with pure white background, ensuring standard JPEG compatibility.")
        ]
    },
    {
        "slug": "jpg-to-png",
        "name": "JPG to PNG",
        "category": "convert",
        "color": "#9333ea",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>',
        "title": "JPG to PNG Converter Online Free — Convert JPEG to Lossless PNG",
        "desc": "Convert JPG and JPEG pictures to lossless PNG format online for crisp graphics and logo editing.",
        "h1": "Convert JPG to PNG Online",
        "tagline": "Convert compressed JPG files into lossless PNG format instantly in your web browser.",
        "faqs": [
            ("Why convert JPG to PNG?", "PNG uses lossless compression, preventing further quality degradation when editing graphics and icons.")
        ]
    },
    {
        "slug": "webp-to-jpg",
        "name": "WEBP to JPG",
        "category": "convert",
        "color": "#16a34a",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12a9 9 0 0 0-9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>',
        "title": "WEBP to JPG Converter Online Free — Convert Google WebP to JPG",
        "desc": "Convert modern WebP images downloaded from the web into standard JPG format for easy viewing and offline sharing.",
        "h1": "Convert WEBP to JPG Online",
        "tagline": "Turn modern WebP web graphics into standard JPG images compatible with all photo viewers and devices.",
        "faqs": [
            ("Why can't some apps open WebP images?", "WebP is a modern web format. Many older photo viewers and form submission websites require standard JPG.")
        ]
    },
    {
        "slug": "heic-to-jpg",
        "name": "HEIC to JPG",
        "category": "convert",
        "color": "#475569",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="5" y="2" width="14" height="20" rx="2"/><line x1="12" y1="18" x2="12.01" y2="18"/></svg>',
        "title": "HEIC to JPG Converter Online — Convert iPhone HEIC/HEIF to JPG",
        "desc": "Convert Apple iPhone and iPad .HEIC and .HEIF photos to high-quality JPG format online without uploading files to a server.",
        "h1": "Convert Apple iPhone HEIC to JPG",
        "tagline": "Convert iOS .HEIC / .HEIF camera photos into universal JPG files right in your browser via WebAssembly.",
        "faqs": [
            ("How does in-browser HEIC conversion work?", "We use a client-side WebAssembly HEIC decoder (heic2any) that decodes Apple's High Efficiency format directly on your CPU.")
        ]
    },
    {
        "slug": "image-to-jpg",
        "name": "Image to JPG",
        "category": "convert",
        "color": "#e5322d",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>',
        "title": "Image to JPG Converter — Convert PNG, GIF, SVG, BMP, WebP to JPG",
        "desc": "Universal image converter to JPG. Convert any picture format into high quality JPEG format in seconds.",
        "h1": "Universal Image to JPG Converter",
        "tagline": "Convert any image format (PNG, WebP, GIF, SVG, BMP) into standardized, high-quality JPG format.",
        "faqs": [
            ("What formats can I convert to JPG?", "You can convert PNG, WebP, GIF, SVG, BMP, and TIFF files.")
        ]
    },
    {
        "slug": "favicon-generator",
        "name": "Favicon Generator",
        "category": "convert",
        "color": "#ca8a04",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="4"/></svg>',
        "title": "Favicon Generator Online Free — Multi-Size Favicon Package (16x16 to 180x180)",
        "desc": "Generate complete website favicon packages from your logo. Generates 16x16, 32x32, 48x48, and Apple Touch Icon (180x180) in a ZIP.",
        "h1": "Free Online Favicon Generator",
        "tagline": "Turn any logo or icon into a multi-resolution favicon suite for modern web browsers and mobile home screens.",
        "faqs": [
            ("Which sizes are included in the favicon package?", "The ZIP package includes 16x16 (browser tab), 32x32 (retina tab), 48x48 (desktop icon), and 180x180 (Apple Touch Icon).")
        ]
    },
    {
        "slug": "image-to-text-ocr",
        "name": "Image to Text (OCR)",
        "category": "convert",
        "color": "#2563eb",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="4 7 4 4 20 4 20 7"/><line x1="9" y1="20" x2="15" y2="20"/><line x1="12" y1="4" x2="12" y2="20"/></svg>',
        "title": "Image to Text OCR Online Free — Extract Text from Photos & Screenshots",
        "desc": "Extract editable text from images, scanned documents, receipts, and screenshots using neural OCR engine. 100% private in your browser.",
        "h1": "Extract Text from Images (OCR)",
        "tagline": "Optical Character Recognition (OCR) neural worker extracts selectable text from pictures, receipts, and book pages.",
        "faqs": [
            ("Does it work on scanned documents and receipts?", "Yes! It recognizes printed Latin text, numbers, and symbols with high optical accuracy.")
        ]
    },

    # 5. Edit & Effects
    {
        "slug": "watermark-image",
        "name": "Watermark Image",
        "category": "edit",
        "color": "#d97706",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2.69l5.66 5.66a8 8 0 1 1-11.31 0z"/></svg>',
        "title": "Watermark Image Online Free — Add Text & Logo Watermark with Dragging",
        "desc": "Stamp text or logo watermarks on photos with interactive click & drag positioning. Protect your copyright against unauthorized copying.",
        "h1": "Watermark Photos Online for Free",
        "tagline": "Protect your creative photography with customizable text stamps and logo watermarks with draggable cursor positioning.",
        "faqs": [
            ("Can I position the watermark with my cursor?", "Yes! You can click and drag the watermark directly on the live image canvas to position it anywhere.")
        ]
    },
    {
        "slug": "rotate-flip-image",
        "name": "Rotate & Flip Image",
        "category": "edit",
        "color": "#10b981",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>',
        "title": "Rotate and Flip Image Online — 90°, 180°, 270° & Mirror Flip",
        "desc": "Rotate photos 90 degrees clockwise, 180 degrees, or flip horizontally and vertically in 1 click online.",
        "h1": "Rotate &amp; Flip Images Online",
        "tagline": "Correct sideways smartphone photos or mirror flip selfie camera shots in 1 click.",
        "faqs": [
            ("Does rotating decrease image quality?", "No, canvas rotation preserves original pixel quality and resolution.")
        ]
    },
    {
        "slug": "blur-censor-image",
        "name": "Blur & Censor Image",
        "category": "edit",
        "color": "#ef4444",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg>',
        "title": "Blur & Censor Image Online — Hide Sensitive Info, Faces & Blackout Docs",
        "desc": "Hide sensitive personal information, blur faces, pixelate license plates, or blackout private text on documents with interactive brush.",
        "h1": "Blur, Pixelate &amp; Censor Images",
        "tagline": "Interactive privacy brush lets you pixelate faces, blur credit card numbers, or blackout private text.",
        "faqs": [
            ("Can censored data be reversed or unblurred?", "No! When exported, the blurred or blacked out pixels are permanently re-rendered into the new JPEG, making recovery impossible.")
        ]
    },
    {
        "slug": "grayscale-image",
        "name": "Grayscale & Black/White",
        "category": "edit",
        "color": "#475569",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 2a10 10 0 0 1 0 20z"/></svg>',
        "title": "Convert Image to Grayscale Online — Black & White Photo Filter",
        "desc": "Convert full-color photographs into artistic Black and White or monochrome grayscale online for free.",
        "h1": "Convert Image to Black &amp; White (Grayscale)",
        "tagline": "Transform full-color pictures into timeless monochrome and black-and-white portraits.",
        "faqs": [
            ("Why convert documents to black and white?", "Grayscale photos consume significantly less printer ink and toner when printing on paper.")
        ]
    },
    {
        "slug": "add-border-image",
        "name": "Add Border to Photo",
        "category": "edit",
        "color": "#6366f1",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><rect x="7" y="7" width="10" height="10"/></svg>',
        "title": "Add Border to Photo Online — White Frame & Custom Color Borders",
        "desc": "Add stylish white photo frames, vintage borders, or custom colored borders to photos with adjustable border thickness.",
        "h1": "Add Border &amp; Frame to Photos",
        "tagline": "Frame your photography with aesthetic white borders or custom colored margins.",
        "faqs": [
            ("Can I customize the border width and color?", "Yes, you can adjust the pixel margin width and select any color using the color palette.")
        ]
    },
    {
        "slug": "join-images",
        "name": "Join Multiple Images",
        "category": "edit",
        "color": "#8b5cf6",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="4" width="9" height="16" rx="1"/><rect x="13" y="4" width="9" height="16" rx="1"/></svg>',
        "title": "Join Images Online Free — Combine Multiple Photos Horizontally & Vertically",
        "desc": "Stitch and combine multiple photos side-by-side (horizontally) or stacked top-to-bottom (vertically) into a single image.",
        "h1": "Join &amp; Stitch Multiple Photos",
        "tagline": "Combine multiple pictures into a before/after comparison collage or continuous vertical strip.",
        "faqs": [
            ("Can I join photos horizontally or vertically?", "Yes! You can choose side-by-side (horizontal) or stacked (vertical) alignment.")
        ]
    },
    {
        "slug": "split-image",
        "name": "Split Image into Pieces",
        "category": "edit",
        "color": "#ec4899",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="2" x2="12" y2="22"/><line x1="2" y1="12" x2="22" y2="12"/><rect x="2" y="2" width="20" height="20" rx="2"/></svg>',
        "title": "Split Image into Pieces Online — Cut Photo into Grid Rows & Columns",
        "desc": "Slice any picture into custom rows and columns grid and download all cut tiles in a ZIP archive.",
        "h1": "Split Image into Grid Pieces",
        "tagline": "Slice graphics and photo maps into equal rows and columns grid tiles with automatic ZIP export.",
        "faqs": [
            ("How many pieces can I split an image into?", "You can customize any grid size, such as 2x2 (4 pieces), 3x3 (9 pieces), or 4x4 (16 pieces).")
        ]
    },
    {
        "slug": "image-color-picker",
        "name": "Image Color Picker",
        "category": "edit",
        "color": "#f59e0b",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m15 2 5 5L8 19l-5 1 1-5 11-13Z"/></svg>',
        "title": "Image Color Picker Online — Eyedropper HEX, RGB & HSL Color Sampler",
        "desc": "Click anywhere on your photo to sample exact pixel colors. Copies HEX code, RGB, and HSL values directly to your clipboard.",
        "h1": "Image Color Picker &amp; Eyedropper",
        "tagline": "Inspect pixel colors across any photo or design and copy HEX, RGB, and HSL color values in 1 click.",
        "faqs": [
            ("How do I sample a color from my image?", "Upload your image, move your cursor over any pixel to see the live color zoom lens, and click to copy the HEX code.")
        ]
    },
    {
        "slug": "exif-metadata-remover",
        "name": "Remove EXIF Metadata",
        "category": "edit",
        "color": "#10b981",
        "icon": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
        "title": "Remove EXIF Metadata Online Free — Clean GPS Location & Camera Tags",
        "desc": "Strip hidden GPS coordinates, camera serial numbers, shooting date/time, and device tags from photos before sharing online.",
        "h1": "Remove EXIF &amp; GPS Metadata from Photos",
        "tagline": "Clean hidden GPS location coordinates and device serial tags to protect your online privacy before posting.",
        "faqs": [
            ("What metadata is removed?", "GPS location coordinates, camera model, lens serial number, capture date/time, and software editing tags are completely scrubbed.")
        ]
    }
]

CATEGORIES = [
    ("all", "All Image Tools", "🌟", len(IMAGE_TOOLS)),
    ("compress", "Compress in KB", "⚡", 2),
    ("passport", "Passport & Exam", "🪪", 4),
    ("resize", "Resize & Crop", "📐", 5),
    ("convert", "Convert Formats", "🔄", 7),
    ("edit", "Edit & Effects", "🎨", 9),
]

def make_header(root_rel, page_title, page_desc, canonical_url):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{page_title}</title>
<meta name="description" content="{page_desc}">
<link rel="canonical" href="{canonical_url}">
<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{page_desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical_url}">
<meta name="twitter:card" content="summary_large_image">
<meta name="robots" content="index, follow">
<link rel="stylesheet" href="{root_rel}assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container">
    <a href="{root_rel}index.html" class="brand">Daily1Step Image<span class="dot">.</span></a>
    <nav class="main-nav">
      <a href="{root_rel}index.html">All Image Tools</a>
      <a href="{root_rel}tools/compress-image-kb/">Compress in KB</a>
      <a href="{root_rel}tools/passport-photo-maker/">Passport Photo</a>
      <a href="{root_rel}tools/resize-image-pixels/">Resize Pixels</a>
      <a href="{root_rel}tools/heic-to-jpg/">HEIC to JPG</a>
      <a href="{root_rel}about.html">About</a>
    </nav>
  </div>
</header>
"""

def make_footer(root_rel):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <h4>Daily1Step Image Tools</h4>
        <p style="font-size:.88rem; line-height:1.6; margin-top:8px;">Fast, private, and 100% browser-based photo and image tools. Compress to exact KB, make passport photos, crop, watermark, and convert formats with zero server uploads.</p>
      </div>
      <div class="footer-col">
        <h4>Popular Compress &amp; Exam</h4>
        <ul>
          <li><a href="{root_rel}tools/compress-image-kb/">Compress Image to KB</a></li>
          <li><a href="{root_rel}tools/passport-photo-maker/">Passport Photo Maker</a></li>
          <li><a href="{root_rel}tools/exam-photo-resizer/">Govt Exam Photo Resizer</a></li>
          <li><a href="{root_rel}tools/add-name-date-photo/">Add Name & Date on Photo</a></li>
          <li><a href="{root_rel}tools/merge-photo-signature/">Merge Photo & Signature</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Resize &amp; Convert</h4>
        <ul>
          <li><a href="{root_rel}tools/resize-image-pixels/">Resize by Pixels</a></li>
          <li><a href="{root_rel}tools/crop-image/">Crop Image</a></li>
          <li><a href="{root_rel}tools/heic-to-jpg/">HEIC to JPG Converter</a></li>
          <li><a href="{root_rel}tools/png-to-jpg/">PNG to JPG Converter</a></li>
          <li><a href="{root_rel}tools/image-to-text-ocr/">Image to Text (OCR)</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company &amp; Legal</h4>
        <ul>
          <li><a href="{root_rel}about.html">About Us</a></li>
          <li><a href="{root_rel}contact.html">Contact Us</a></li>
          <li><a href="{root_rel}privacy-policy.html">Privacy Policy</a></li>
          <li><a href="{root_rel}terms.html">Terms of Service</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div>&copy; 2026 Daily1Step Image Tools. All rights reserved. 100% Client-Side Processing.</div>
      <div>
        <a href="{root_rel}privacy-policy.html" style="margin-right:12px;">Privacy Policy</a>
        <a href="{root_rel}terms.html">Terms of Service</a>
      </div>
    </div>
  </div>
</footer>
<script src="{root_rel}vendor/jszip.min.js"></script>
<script src="{root_rel}vendor/heic2any.min.js"></script>
<script src="{root_rel}vendor/tesseract.min.js"></script>
</body>
</html>
"""

# 2. Build Tool Pages
for t in IMAGE_TOOLS:
    slug = t["slug"]
    name = t["name"]
    title = t["title"]
    desc = t["desc"]
    h1 = t["h1"]
    tagline = t["tagline"]
    canonical = f"{SITE_URL}/tools/{slug}/"

    # Read original PHP file body if present in PDF Tools
    src_php = os.path.join(r"D:\Codding\Claude Cowork code\PDF Tools\image-tools", slug, "index.php")
    body_ui = ""
    if os.path.exists(src_php):
        with open(src_php, "r", encoding="utf-8") as f:
            c = f.read()
        # Remove php tags and headers/footers
        c = re.sub(r'<\?php.*?\?>', '', c, flags=re.DOTALL)
        body_ui = c.strip()

    faq_entities = []
    faq_html = ""
    for q, a in t["faqs"]:
        faq_entities.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        faq_html += f"""
        <div class="faq-item">
          <button class="faq-question" type="button">
            <span>{q}</span>
            <span style="font-size:1.2rem;">+</span>
          </button>
          <div class="faq-answer" style="display:none;">
            <p>{a}</p>
          </div>
        </div>
        """

    schema_data = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebApplication",
                "name": name,
                "url": canonical,
                "description": desc,
                "applicationCategory": "MultimediaApplication",
                "operatingSystem": "All modern browsers (Windows, Mac, iOS, Android)",
                "offers": {
                    "@type": "Offer",
                    "price": "0",
                    "priceCurrency": "USD"
                }
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {
                        "@type": "ListItem",
                        "position": 1,
                        "name": "Home",
                        "item": f"{SITE_URL}/"
                    },
                    {
                        "@type": "ListItem",
                        "position": 2,
                        "name": "Image Tools",
                        "item": f"{SITE_URL}/#tools"
                    },
                    {
                        "@type": "ListItem",
                        "position": 3,
                        "name": name,
                        "item": canonical
                    }
                ]
            },
            {
                "@type": "FAQPage",
                "mainEntity": faq_entities
            }
        ]
    }

    tool_html = make_header("../../", title, desc, canonical) + f"""
<script type="application/ld+json">
{json.dumps(schema_data, indent=2)}
</script>

<main class="tool-page">
  <div class="container">
    <div class="breadcrumb" style="max-width:920px; margin:0 auto 16px;">
      <a href="../../index.html">Home</a> &gt; <a href="../../index.html">Tools</a> &gt; <span>{name}</span>
    </div>

    <div class="tool-header">
      <h1>{h1}</h1>
      <p>{tagline}</p>
    </div>

    <!-- Ad Slot Top -->
    <div class="ad-slot-wrap">
      <span>Advertisement</span>
    </div>

    {body_ui}

    <!-- Ad Slot Middle -->
    <div class="ad-slot-wrap" style="margin-top:32px;">
      <span>Advertisement</span>
    </div>

  </div>
</main>

<article class="seo-article">
  <div class="content-container">
    <h2>How to Use {name} Online in 3 Simple Steps</h2>
    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">1</div>
        <h4>Upload Your Image</h4>
        <p>Drag and drop your photo or click the box to select JPG, PNG, WebP, or HEIC files from your phone or PC.</p>
      </div>
      <div class="step-card">
        <div class="step-num">2</div>
        <h4>Configure Parameters</h4>
        <p>Set exact target KB, dimensions, borders, or crop areas using real-time sliders and preset buttons.</p>
      </div>
      <div class="step-card">
        <div class="step-num">3</div>
        <h4>Download Instant Output</h4>
        <p>Click the download button to save your high-resolution processed image directly to your device.</p>
      </div>
    </div>

    <h2>Why Choose Daily1Step {name}?</h2>
    <p>Daily1Step {name} delivers unmatched processing speed, precision, and privacy. Unlike cloud-based photo editors that upload private pictures to external servers, all transformations execute on your device using hardware-accelerated <strong>HTML5 Canvas 2D &amp; WebAssembly</strong>.</p>
    <ul>
      <li><strong>100% Private &amp; Secure:</strong> Photos are never uploaded or stored on any server.</li>
      <li><strong>Pixel-Perfect Accuracy:</strong> Exact target KB binary search and millimetric DPI scaling.</li>
      <li><strong>Instant Performance:</strong> Zero waiting for file uploads or server queues.</li>
      <li><strong>Cross-Device Compatibility:</strong> Works seamlessly on Windows, Mac, iPhone, iPad, and Android.</li>
    </ul>

    <h2>Frequently Asked Questions (FAQ)</h2>
    <div class="faq-list">
      {faq_html}
    </div>

    <!-- Ad Slot Bottom -->
    <div class="ad-slot-wrap" style="margin-top:40px;">
      <span>Advertisement</span>
    </div>
  </div>
</article>

<script>
// FAQ Accordion interaction
document.querySelectorAll('.faq-question').forEach(function(btn) {{
  btn.addEventListener('click', function() {{
    var ans = btn.nextElementSibling;
    var isOpen = ans.style.display === 'block';
    ans.style.display = isOpen ? 'none' : 'block';
    btn.querySelector('span:last-child').textContent = isOpen ? '+' : '−';
  }});
}});
</script>
""" + make_footer("../../")

    # Fix script paths from ../../assets to correct relative path
    tool_html = tool_html.replace('src="../../assets/', 'src="../../assets/')
    tool_html = tool_html.replace('src="../../vendor/', 'src="../../vendor/')

    # Save to tools/<slug>/index.html
    t_dir = os.path.join(TOOLS_DIR, slug)
    os.makedirs(t_dir, exist_ok=True)
    with open(os.path.join(t_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(tool_html)

    # Save alias to root <slug>/index.html for dual compatibility
    alias_dir = os.path.join(BASE_DIR, slug)
    os.makedirs(alias_dir, exist_ok=True)
    alias_html = tool_html.replace('../../', '../')
    with open(os.path.join(alias_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(alias_html)

print("Generated all 27 tool pages.")

# 3. Build Homepage Hub (index.html)
tab_buttons_html = ""
for cat_key, cat_name, cat_icon, count in CATEGORIES:
    active = " active" if cat_key == "all" else ""
    tab_buttons_html += f"""
    <button class="category-tab{active}" data-category="{cat_key}">
      <span>{cat_icon} {cat_name}</span>
      <span class="tab-count">{count}</span>
    </button>
    """

tool_cards_html = ""
for t in IMAGE_TOOLS:
    tool_cards_html += f"""
    <a href="tools/{t['slug']}/" class="tool-card" data-category="{t['category']}" data-title="{t['name'].lower()}" data-desc="{t['desc'].lower()}">
      <div class="icon" style="background:{t['color']};">{t['icon']}</div>
      <h3>{t['name']}</h3>
      <p>{t['desc']}</p>
    </a>
    """

home_schema = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Daily1Step Image Tools",
    "url": f"{SITE_URL}/",
    "description": "Free online image tools suite. Compress image to exact KB, create passport photos, resize in pixels/cm/mm, crop, watermark, and convert PNG/JPG/HEIC.",
    "potentialAction": {
        "@type": "SearchAction",
        "target": f"{SITE_URL}/?q={{search_term_string}}",
        "query-input": "required name=search_term_string"
    }
}

home_faqs = [
    ("Are all image tools on Daily1Step free to use?", "Yes! All 27 image tools are 100% free with no daily limits, hidden subscriptions, or watermark stamps."),
    ("Are my private photos uploaded to a cloud server?", "No! Daily1Step processes all images locally inside your web browser using HTML5 Canvas. Your photos never leave your device."),
    ("Can I compress images to an exact KB size for govt job forms?", "Yes! Our Compress Image to KB tool allows you to specify exact file sizes like 20KB, 50KB, 100KB, or 200KB."),
    ("What photo formats are supported?", "We support JPG, JPEG, PNG, WebP, Apple HEIC/HEIF, GIF, SVG, and BMP.")
]

home_faq_html = ""
for q, a in home_faqs:
    home_faq_html += f"""
    <div class="faq-item">
      <button class="faq-question" type="button">
        <span>{q}</span>
        <span style="font-size:1.2rem;">+</span>
      </button>
      <div class="faq-answer" style="display:none;">
        <p>{a}</p>
      </div>
    </div>
    """

home_html = make_header("", "Daily1Step Image Tools — Free Online Image Compress, Resize, Passport Photo & Convert", "Free online image tools suite. Compress to exact KB, make passport photos, resize in pixels/cm/mm, crop, watermark, and convert PNG/JPG/HEIC/WebP 100% in browser.", f"{SITE_URL}/") + f"""
<script type="application/ld+json">
{json.dumps(home_schema, indent=2)}
</script>

<section class="hero">
  <div class="container">
    <h1>Every Image Tool You Need, In One Place</h1>
    <p>Compress to exact KB, make passport photos, resize in pixels/cm/mm, crop, watermark, and convert images &mdash; 100% free, no signup, and processed right in your browser.</p>
  </div>
</section>

<!-- Ad Slot Top -->
<div class="container">
  <div class="ad-slot-wrap">
    <span>Advertisement</span>
  </div>
</div>

<section class="container" id="tools">
  <div class="tool-controls-wrap">
    <div class="tool-search-box">
      <span class="search-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
      </span>
      <input type="text" id="toolSearchInput" placeholder="Search 27 image tools (e.g. compress, passport, resize, crop, jpg)..." autocomplete="off">
    </div>

    <div class="category-tabs" id="categoryTabs">
      {tab_buttons_html}
    </div>
  </div>

  <div class="tool-grid" id="mainToolGrid">
    {tool_cards_html}
  </div>

  <div id="noResultsMsg" style="display:none; text-align:center; padding:50px 20px; color:var(--ink-soft);">
    <p style="font-size:1.4rem; font-weight:700; color:var(--ink); margin-bottom:6px;">No image tools found</p>
    <p>Try searching for different keywords like "compress", "passport", "resize", "crop", or "jpg".</p>
  </div>
</section>

<!-- Ad Slot Middle -->
<div class="container">
  <div class="ad-slot-wrap">
    <span>Advertisement</span>
  </div>
</div>

<article class="seo-article">
  <div class="content-container">
    <h2>Why Choose Daily1Step Image Tools?</h2>
    <p>Daily1Step Image Tools runs entirely in your web browser. Unlike conventional online photo converters, your images are <strong>never uploaded to a server</strong> &mdash; all compression, cropping, and effects happen locally on your computer or smartphone using client-side HTML5 Canvas and WebAssembly.</p>

    <div class="step-card-grid">
      <div class="step-card">
        <div class="step-num">🎯</div>
        <h4>Exact KB Target Sizing</h4>
        <p>Compress photos to exact 20KB, 50KB, or 100KB limits required by competitive exam portals.</p>
      </div>
      <div class="step-card">
        <div class="step-num">🔒</div>
        <h4>100% Device-Local Privacy</h4>
        <p>Your photos never leave your device. Zero server uploads ensure complete security for private documents.</p>
      </div>
      <div class="step-card">
        <div class="step-num">🪪</div>
        <h4>Official Govt Exam Specs</h4>
        <p>1-click photo and signature formatting for SSC, UPSC, PAN Card, Railway, and Visa applications.</p>
      </div>
      <div class="step-card">
        <div class="step-num">⚡</div>
        <h4>Instant WebAssembly Speed</h4>
        <p>High-speed parallel batch resizing and instant Apple iPhone HEIC decoding.</p>
      </div>
    </div>

    <h2>Frequently Asked Questions</h2>
    <div class="faq-list">
      {home_faq_html}
    </div>
  </div>
</article>

<script>
(function() {{
  var searchInput = document.getElementById('toolSearchInput');
  var categoryTabs = document.querySelectorAll('.category-tab');
  var toolCards = document.querySelectorAll('.tool-card');
  var noResults = document.getElementById('noResultsMsg');
  var currentCategory = 'all';

  function filterTools() {{
    var query = (searchInput.value || '').trim().toLowerCase();
    var visibleCount = 0;

    toolCards.forEach(function(card) {{
      var cat = card.getAttribute('data-category');
      var title = card.getAttribute('data-title');
      var desc = card.getAttribute('data-desc');

      var matchesCat = (currentCategory === 'all' || cat === currentCategory);
      var matchesQuery = !query || title.indexOf(query) !== -1 || desc.indexOf(query) !== -1;

      if (matchesCat && matchesQuery) {{
        card.style.display = 'flex';
        visibleCount++;
      }} else {{
        card.style.display = 'none';
      }}
    }});

    if (noResults) {{
      noResults.style.display = (visibleCount === 0) ? 'block' : 'none';
    }}
  }}

  categoryTabs.forEach(function(tab) {{
    tab.addEventListener('click', function() {{
      categoryTabs.forEach(function(t) {{ t.classList.remove('active'); }});
      tab.classList.add('active');
      currentCategory = tab.getAttribute('data-category');
      filterTools();
    }});
  }});

  if (searchInput) {{
    searchInput.addEventListener('input', filterTools);
  }}

  // FAQ Accordion
  document.querySelectorAll('.faq-question').forEach(function(btn) {{
    btn.addEventListener('click', function() {{
      var ans = btn.nextElementSibling;
      var isOpen = ans.style.display === 'block';
      ans.style.display = isOpen ? 'none' : 'block';
      btn.querySelector('span:last-child').textContent = isOpen ? '+' : '−';
    }});
  }});
}})();
</script>
""" + make_footer("")

with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(home_html)

print("Generated homepage index.html.")

# 4. Generate AdSense Legal Pages
# Privacy Policy
privacy_html = make_header("", "Privacy Policy — Daily1Step Image Tools", "Privacy policy for Daily1Step Image Tools. Learn how client-side processing keeps your photos private.", f"{SITE_URL}/privacy-policy.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Privacy Policy</span>
    </div>
    <h1>Privacy Policy</h1>
    <p><em>Last updated: August 17, 2026</em></p>

    <h2>1. 100% Client-Side Privacy Architecture</h2>
    <p>At Daily1Step Image Tools (<code>https://bypyay.github.io/imagetools/</code>), we operate with a strict client-side privacy model. All image processing, compression, resizing, and photo modifications occur directly in your browser's memory using HTML5 Canvas. <strong>Your photos are never uploaded to any remote server or stored in any database.</strong></p>

    <h2>2. Google AdSense & Cookies</h2>
    <p>We may display advertisements served by Google AdSense to support the free operation of our website. Google uses cookies (including DoubleClick) to serve ads based on user visits. You may opt out of personalized advertising by visiting Google Ads Settings.</p>

    <h2>3. GDPR & CCPA Compliance</h2>
    <p>Because we do not collect, process, or store personal files or personal identifiers on remote servers, no user data is sold, rented, or shared with third parties.</p>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "privacy-policy.html"), "w", encoding="utf-8") as f:
    f.write(privacy_html)

# Terms of Service
terms_html = make_header("", "Terms of Service — Daily1Step Image Tools", "Terms of service for Daily1Step Image Tools.", f"{SITE_URL}/terms.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Terms of Service</span>
    </div>
    <h1>Terms of Service</h1>
    <p><em>Last updated: August 17, 2026</em></p>

    <h2>1. Acceptance of Terms</h2>
    <p>By using Daily1Step Image Tools, you agree to these Terms of Service. All tools are provided free of charge on an 'as-is' basis without warranties.</p>

    <h2>2. Ownership & Copyright</h2>
    <p>You retain 100% copyright and ownership of any images, graphics, and photographs processed using our tools.</p>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "terms.html"), "w", encoding="utf-8") as f:
    f.write(terms_html)

# About Us
about_html = make_header("", "About Us — Daily1Step Image Tools", "About Daily1Step Image Tools — Private browser-based photo utilities.", f"{SITE_URL}/about.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>About Us</span>
    </div>
    <h1>About Daily1Step Image Tools</h1>
    <p class="lead" style="font-size:1.15rem; color:var(--ink-soft); margin-bottom:24px;">Fast, private, and free browser-based photo utilities for students, job applicants, and photographers.</p>

    <h2>Our Mission</h2>
    <p>Daily1Step Image Tools provides 27 browser-native tools to resize, compress, crop, and convert photos without ever uploading them to remote servers. This eliminates bandwidth bottlenecks and guarantees total user privacy.</p>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "about.html"), "w", encoding="utf-8") as f:
    f.write(about_html)

# Contact Us
contact_html = make_header("", "Contact Us — Daily1Step Image Tools", "Get in touch with Daily1Step Image Tools.", f"{SITE_URL}/contact.html") + """
<main class="seo-article">
  <div class="content-container">
    <div class="breadcrumb">
      <a href="index.html">Home</a> &gt; <span>Contact Us</span>
    </div>
    <h1>Contact Us</h1>
    <p>Have questions, feedback, or suggestions? We'd love to hear from you!</p>

    <div style="max-width:680px; margin:28px 0; background:var(--bg-soft); border:1px solid var(--border); border-radius:var(--radius-lg); padding:28px;">
      <form onsubmit="event.preventDefault(); alert('Thank you for your message! Our team will get back to you soon.');">
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Your Name</label>
          <input type="text" required placeholder="Enter your full name" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:16px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Your Email</label>
          <input type="email" required placeholder="name@example.com" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem;">
        </div>
        <div style="margin-bottom:20px;">
          <label style="display:block; font-weight:700; font-size:.9rem; margin-bottom:6px; color:var(--ink);">Message</label>
          <textarea rows="5" required placeholder="How can we help you?" style="width:100%; padding:12px 14px; border:1px solid var(--border); border-radius:var(--radius-sm); font-size:1rem; font-family:inherit;"></textarea>
        </div>
        <button type="submit" class="btn" style="width:100%;">Send Message</button>
      </form>
    </div>
  </div>
</main>
""" + make_footer("")
with open(os.path.join(BASE_DIR, "contact.html"), "w", encoding="utf-8") as f:
    f.write(contact_html)

# 5. Generate Robots.txt and Sitemap.xml
robots_txt = f"""User-agent: *
Allow: /

Sitemap: {SITE_URL}/sitemap.xml
"""
with open(os.path.join(BASE_DIR, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_txt)

sitemap_urls = [
    f"{SITE_URL}/",
    f"{SITE_URL}/about.html",
    f"{SITE_URL}/contact.html",
    f"{SITE_URL}/privacy-policy.html",
    f"{SITE_URL}/terms.html",
]
for t in IMAGE_TOOLS:
    sitemap_urls.append(f"{SITE_URL}/tools/{t['slug']}/")

sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
"""
for u in sitemap_urls:
    sitemap_xml += f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-08-17</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
"""
sitemap_xml += "</urlset>\n"

with open(os.path.join(BASE_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print("Generated sitemap.xml with 32 URLs and robots.txt.")
