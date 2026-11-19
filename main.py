# Coded By can-codev


import sys
import os
import time
import random
import hashlib
import base64
import json
import requests
import urllib3
from io import BytesIO
urllib3.disable_warnings()
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QFileDialog, QTextEdit, QComboBox,
    QMessageBox, QGroupBox, QCheckBox, QFrame, QScrollArea,
    QSplitter, QSizePolicy, QTabWidget, QLineEdit, QProgressBar,
    QGridLayout, QDialog, QListWidget, QListWidgetItem
)
from PyQt5.QtCore import Qt, QPoint, QThread, pyqtSignal, QTimer, QSize
from PyQt5.QtGui import (
    QPixmap, QFont, QPainter, QColor, QLinearGradient, QPalette,
    QTextOption, QImage, QIcon
)
BRAND_NAME = "Can-CoDev"
COLORS = {
    'background': '#080808',
    'panel': '#141414',
    'dark': '#101010',
    'darker': '#0A0A0A',
    'text': '#EAEAEA',
    'text_secondary': '#9AA0A6',
    'primary': '#00C2FF',
    'primary_dark': '#0099CC',
    'primary_light': '#62D9FF',
    'accent': '#1DB4FF',
    'border': '#2B2B2B',
    'success': '#35C759',
    'danger': '#F44336',
    'button_bg': '#00C2FF',
    'button_hover': '#1DB4FF',
    'button_pressed': '#0099CC',
}
LANGUAGES = {"Türkçe": "tr", "English": "en"}
TRANSLATIONS = {
    "tr": {
        "app_title": "AI Photo Studio",
        "tab_generate": "Fotoğraf Üret",
        "tab_history": "Geçmiş",
        "tab_settings": "Bilgilendirme",
        "style_select": "Stil Seç",
        "aspect_select": "Oran Seç",
        "prompt_label": "Açıklama (Prompt)",
        "prompt_placeholder": "Hayalindeki sahneyi yaz... (örn: uzayda uçan kedi)",
        "generate": "Fotoğraf Üret",
        "regenerate": "Yeniden Üret",
        "random_prompt": "Rastgele Prompt",
        "preview": "Önizleme",
        "no_images": "Henüz görsel üretilmedi",
        "generating": "Görseller oluşturuluyor...",
        "ready": "Hazır",
        "error": "Hata",
        "success": "Başarılı",
        "download": "İndir",
        "download_all": "Tümünü İndir",
        "copy_prompt": "Promptu Kopyala",
        "prompt_copied": "Prompt panoya kopyalandı",
        "image_saved": "Görsel kaydedildi",
        "no_bg_images": "Arka plansız görsel yok",
        "show_no_bg": "Arka Plansız Göster",
        "history_empty": "Geçmiş boş",
        "language": "Dil",
        "clear_history": "Geçmişi Temizle",
        "designed_by": "Coded by",
        "generation_failed": "Görsel üretilemedi. Tekrar deneyin.",
        "prompt_too_short": "En az 3 karakter girin",
        "style_required": "Lütfen stil seçin",
        "aspect_required": "Lütfen oran seçin",
        "images_count": "görsel oluşturuldu",
        "image_list": "Görseller",
        "bg_removed": "Arka plansız",
        "with_bg": "Normal",
        "settings_saved": "Bilgi kaydedildi",
        "api_settings": "Sistem Bilgisi",
        "photoroom_info": "Photoroom API üzerinden görsel üretimi yapılır. Burada değiştirilen bir ayar yok, sadece bilgi var.",
        "about": "Hakkında",
        "about_text": "Can-Codev AI Photo Studio\n\nYapımcı: Can-Codev\n\n"
                      "Photoroom API tabanlı yapay zeka fotoğraf üretim aracı. 80+ stil, 10 oran, otomatik prompt zenginleştirme.\n\n"
                      "Nasıl kullanılır?\n"
                      "1) Açıklama kutusuna istediğin sahneyi yaz (en az 3 karakter). Aklına bir şey gelmezse Rastgele Prompt'a bas.\n"
                      "2) Stil Seç ve Oran Seç kutularından tarzı bi de çerçeveyi belirle.\n"
                      "3) Fotoğraf Üret'e tıkla. 4 görsel gelene kadar bekle, sağ üstte durum yazar.\n"
                      "4) Görselin üstüne tıklayınca büyük önizleme açılır, İndir ile tek tek kaydedersin. Hepsini bir klasöre atmak için Tümünü İndir var.\n"
                      "5) Arka Plansız Göster butonu aktif olursa şeffaf versiyonlar ayrı pencerede açılır, oradan da indirilir.\n"
                      "6) Geçmiş sekmesinde eski promptlar durur, satıra çift tıklayınca ilk görsel tekrar açılır.\n\n"
                      "Burada ayar falan yok, bu sekme sadece bilgilendirme için duruyor. Dil'i değiştirince yazılar da değişir.",
        "cfg_scale": "CFG Scale",
        "steps": "Adım Sayısı",
        "image_count": "Görsel Sayısı",
        "close_confirm_title": "Üretim sürüyor",
        "close_confirm_text": "Görsel üretimi devam ediyor. Yine de kapatmak istiyor musunuz?",
        "loading": "Yükleniyor...",
        "load_failed": "Yüklenemedi",
        "no_background_title": "Arka Plansız Görseller",
        "close": "Kapat",
        "select_folder": "Klasör Seç",
        "history_title": "Geçmiş",
        "about_tab": "Hakkında",
    },
    "en": {
        "app_title": "AI Photo Studio",
        "tab_generate": "Generate",
        "tab_history": "History",
        "tab_settings": "Information",
        "style_select": "Select Style",
        "aspect_select": "Select Aspect",
        "prompt_label": "Prompt",
        "prompt_placeholder": "Describe your scene... (e.g. cat flying in space)",
        "generate": "Generate Photo",
        "regenerate": "Regenerate",
        "random_prompt": "Random Prompt",
        "preview": "Preview",
        "no_images": "No images generated yet",
        "generating": "Generating images...",
        "ready": "Ready",
        "error": "Error",
        "success": "Success",
        "download": "Download",
        "download_all": "Download All",
        "copy_prompt": "Copy Prompt",
        "prompt_copied": "Prompt copied to clipboard",
        "image_saved": "Image saved",
        "no_bg_images": "No background-removed images",
        "show_no_bg": "Show No Background",
        "history_empty": "History empty",
        "language": "Language",
        "clear_history": "Clear History",
        "designed_by": "Coded by",
        "generation_failed": "Generation failed. Try again.",
        "prompt_too_short": "Enter at least 3 characters",
        "style_required": "Please select a style",
        "aspect_required": "Please select an aspect",
        "images_count": "images generated",
        "image_list": "Images",
        "bg_removed": "No background",
        "with_bg": "Normal",
        "settings_saved": "Info saved",
        "api_settings": "System Info",
        "photoroom_info": "Images are generated via Photoroom API. Nothing to configure here, just info.",
        "about": "About",
        "about_text": "Can-Codev AI Photo Studio\n\nCreator: Can-Codev\n\n"
                      "Photoroom API based AI photo generator. 80+ styles, 10 aspects, auto prompt enhancement.\n\n"
                      "How to use?\n"
                      "1) Type the scene into the prompt box (at least 3 chars), or hit Random Prompt.\n"
                      "2) Pick a style and an aspect ratio from the two combo boxes.\n"
                      "3) Click Generate Photo and wait for the 4 images, the status on the top right tells you what's going on.\n"
                      "4) Click any image to open the big preview and save it with Download, or use Download All to drop everything into a folder.\n"
                      "5) If Show No Background becomes active, the transparent versions open in a separate window and can be saved from there too.\n"
                      "6) Old prompts stay in the History tab, double click a row to reopen the first image.\n\n"
                      "No settings in here, this tab is just information. Changing Language translates these texts as well.",
        "cfg_scale": "CFG Scale",
        "steps": "Steps",
        "image_count": "Image Count",
        "close_confirm_title": "Generation running",
        "close_confirm_text": "Image generation is in progress. Close anyway?",
        "loading": "Loading...",
        "load_failed": "Load failed",
        "no_background_title": "No Background Images",
        "close": "Close",
        "select_folder": "Select Folder",
        "history_title": "History",
        "about_tab": "About",
    }
}
ANGLES = ["frnt_vw", "sd_vw", "bck_vw", "tp_vw", "btm_vw", "prspctv", "wd_ang", "mcr_sh", "aerl", "fsh_lns",
          "tlt_shft", "dth_ang", "ovrhd", "ye_lvl", "brd_ye", "wrm_ye"]
LIGHTS = ["gldn_hr", "nn_ngh", "std_soft", "drm_shdw", "vlmtrc_fg", "rm_lght", "cnmtc_amb", "bl_md", "wrm_snst",
          "cld_wntr", "snrse", "mnlght", "cndl_lght", "flsh_ph", "rng_lght", "b_lmnsnt", "lsr_lght", "fr_lght",
          "twlght", "mdngh", "ovrcst", "hrsh_sn", "bcklght", "sllht"]
MOODS = ["epc", "clm", "mystr", "rmntc", "drk_hrr", "drmy", "ftrsc", "vntg_rtr", "grng", "mnmlst", "lxry",
         "brtlst", "chc", "pcfl", "mlnchlc", "jyfl", "hpfl", "dsp", "agrsv", "plyfl", "elgnt", "rw", "ethrl",
         "scr", "mjstc", "ntmt"]
FILTERS = ["kdk_prtr", "fj_prv", "lfrd_bw", "cnstl_800", "plrd_nst", "lmchrm", "gf_vst", "hssbl_nat", "lc_m10",
           "zs_dstgn", "vntg_1970", "nstgrm", "vsc_c1", "snpsd_drm", "lgrm_cnm", "dn_tbl_fm", "anlg_stl", "rdsc",
           "nfrrd", "crss_prc", "blch_bps"]
CAMERAS = ["sony_a7riv", "canon_r5", "nikon_z9", "fujifilm_gfx100", "hasselblad_h6d", "leica_m11", "iphone_15_pro",
           "google_pixel_8", "samsung_s24_ultra", "xiaomi_14_ultra", "oneplus_12", "vivo_x100", "huawei_p60",
           "oppo_find_x7", "realme_gt5", "pixel_fold", "iphone_16_pro"]
ARTISTS = ["picasso", "vangogh", "monet", "rembrandt", "da_vinci", "michelangelo", "dali", "kandinsky", "klimt",
           "hopper", "vermeer", "caravaggio", "botticelli", "raphael", "goya", "munch", "magritte", "frida_kahlo",
           "banksy", "warhol", "haring", "basquiat", "pollock", "rothko", "mondrian", "malevich", "cezanne",
           "degas", "renoir", "seurat", "toulouse", "gauguin", "modigliani", "chagall", "marc", "klee",
           "schiele", "friedrich", "turner", "constable", "hokusai", "hiroshige", "utamaro", "eisen", "sharaku"]
ASPECTS = [("1:1", "Kare"), ("4:5", "Portre"), ("16:9", "Sinema"), ("9:16", "Story"), ("4:3", "Klasik"),
           ("3:4", "Dikey"), ("2:1", "Panorama"), ("21:9", "Genis"), ("32:9", "Super Genis"), ("5:4", "Foto")]
ASPECT_MAP = {"1:1": "SQUARE_HD", "4:5": "PORTRAIT_4_3", "16:9": "LANDSCAPE_16_9", "9:16": "PORTRAIT_16_9",
              "4:3": "LANDSCAPE_4_3", "3:4": "PORTRAIT_4_3", "2:1": "LANDSCAPE_16_9", "21:9": "LANDSCAPE_16_9",
              "32:9": "LANDSCAPE_16_9", "5:4": "LANDSCAPE_4_3"}
STYLES = [
    ("anime", "Anime"), ("realistic", "Gercekci"), ("oil_painting", "Yagli Boya"), ("watercolor", "Sulu Boya"),
    ("sketch", "Cizim"), ("pixel", "Piksel"), ("3d_render", "3D Render"), ("cyberpunk", "Cyberpunk"),
    ("steampunk", "Steampunk"), ("fantasy", "Fantastik"), ("gothic", "Gotik"), ("cartoon", "Cizgi Film"),
    ("comic", "Cizgi Roman"), ("glitch", "Glitch"), ("vaporwave", "Vaporwave"), ("impressionist", "Empresyonist"),
    ("expressionist", "Ekspresyonist"), ("cubist", "Kubist"), ("surrealist", "Surrealist"), ("popart", "Pop Art"),
    ("minimalist", "Minimalist"), ("baroque", "Barok"), ("rococo", "Rokoko"), ("renaissance", "Ronesans"),
    ("abstract", "Soyut"), ("graffiti", "Grafiti"), ("vector", "Vektor"), ("isometric", "Izometrik"),
    ("low_poly", "Low Poly"), ("chalk", "Tebesir"), ("pastel", "Pastel"), ("charcoal", "Komur"),
    ("mosaic", "Mozaik"), ("origami", "Origami"), ("lego", "Lego"), ("collage", "Kolaj"), ("mandala", "Mandala"),
    ("calligraphy", "Hat Sanati"), ("henna", "Kina"), ("polaroid", "Polaroid"), ("infrared", "Kizilotesi"),
    ("thermal", "Termal"), ("underwater", "Su Alti"), ("microscopic", "Mikroskobik"), ("telescopic", "Teleskopik"),
    ("night_vision", "Gece Gorusu"), ("xray", "Rontgen"), ("sonar", "Sonar"), ("radar", "Radar"),
    ("hologram", "Hologram"), ("neon", "Neon"), ("chromatic", "Kromatik"), ("monochrome", "Siyah Beyaz"),
    ("sepia", "Sepya"), ("cyanotype", "Cyanotype"), ("lomography", "Lomografi"), ("tilt_shift", "Tilt Shift"),
    ("macro", "Makro"), ("bokeh", "Bokeh"), ("long_exp", "Uzun Poz"), ("double_exp", "Cift Poz"), ("hdr", "HDR"),
    ("night_mode", "Gece Modu"), ("portrait", "Portre"), ("landscape", "Manzara"), ("street", "Sokak"),
    ("architecture", "Mimari"), ("food", "Yemek"), ("fashion", "Moda"), ("product", "Urun"), ("automotive", "Otomotiv"),
    ("sports", "Spor"), ("wildlife", "Yaban Hayati"), ("macro_insect", "Bocek"), ("astro", "Astro"),
    ("aerial", "Havadan")
]
RANDOM_PROMPTS = ["uzayda kedi", "ates ejderi", "altin sehir", "buyulu orman", "eski robot", "super kahraman",
                  "firavun prensesi", "gelecek misir", "seker gezegeni", "cam dunya", "kristal dag", "ates denizi",
                  "mor gokyuzu", "dev goz", "ucan kale", "uzay gemisi", "uzayli yaratik", "hareketli cicek",
                  "kizgin gunes", "kirik ay", "yakisi melek", "deniz canavari", "su alti sehri", "aden bahcesi",
                  "ates ve buz", "guclu buyucu", "beyaz ejder", "kara sovalye"]
def _h(s): return hashlib.sha256(s.encode()).hexdigest()[:16]
def _c(p): return base64.b64encode(p.encode()).decode()
def _enh(p, sid):
    a = random.choice(ANGLES).replace("_", " ")
    l = random.choice(LIGHTS).replace("_", " ")
    m = random.choice(MOODS).replace("_", " ")
    f = random.choice(FILTERS).replace("_", " ")
    c = random.choice(CAMERAS).replace("_", " ")
    is_art = sid in ["oil_painting", "impressionist", "surrealist", "cubist", "expressionist", "renaissance",
                     "baroque", "watercolor", "sketch", "mandala", "calligraphy"]
    ar = random.choice(ARTISTS) if is_art else ""
    ar_txt = f" style of {ar}" if ar else ""
    v = [8, 12, 16, 24, 32, 48, 64]
    q = random.choice(v)
    return (f"{p}, {a} view, {l} lighting, {m} atmosphere, {f} film, {c} camera{ar_txt}, "
            f"ultra hd {q}k, masterpiece, award winning, trending on artstation, behance featured, "
            f"cgsociety, highres, extremely detailed, professional, national geographic")
def _gt():
    h = {'Content-Type': 'application/json', 'X-Android-Package': 'com.photoroom.app',
         'X-Android-Cert': '0424A4898A4B33940D8BF16E44251B876E97F8D0', 'Accept-Language': 'en-US',
         'X-Client-Version': 'Android/Fallback/X23002000/FirebaseCore-Android',
         'X-Firebase-GMPID': '1:456289768976:android:30c90b24b80bc2d1bfdc95',
         'X-Firebase-Client': 'H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA',
         'X-Firebase-AppCheck': 'eyJlcnJvciI6IlVOS05PV05fRVJST1IifQ==',
         'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 12)', 'Host': 'www.googleapis.com'}
    p = {'key': 'AIzaSyAJGrgbFGB_-h8V2oJLr4b-_ipetqM0duU'}
    j = {'clientType': 'CLIENT_TYPE_ANDROID'}
    r = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser',
                      headers=h, params=p, json=j, timeout=30).json()
    return r["idToken"]
def _gen(p, sid, asp, cfg_scale=9, steps=45, count=4, stop_flag=None):
    sz = ASPECT_MAP.get(asp, "SQUARE_HD")
    t = _gt()
    rid = _h(f"{time.time()}{random.random()}{p[:10]}")
    h = {'Host': 'serverless-api.photoroom.com', 'Accept': 'text/event-stream', 'Authorization': t,
         'Content-Type': 'application/json; charset=utf-8', 'User-Agent': 'okhttp/4.12.0',
         'Pr-App-Version': '2025.47.03 (2180)', 'Pr-Platform': 'android', 'X-Request-ID': rid,
         'X-Enhanced': _c('true')}
    pl = {"userPrompt": _enh(p, sid), "appId": "expert", "styleId": sid, "sizeId": sz,
          "numberOfImages": count, "cfgScale": cfg_scale, "steps": steps,
          "sampler": "dpmpp_2m_karras", "seed": random.randint(1, 999999999),
          "clip_skip": 2, "hires_fix": True, "denoising": 0.75, "face_restore": True, "upscale": 2}
    rs = requests.post("https://serverless-api.photoroom.com/v2/ai-tools/generate-images",
                       headers=h, json=pl, stream=True, verify=False, timeout=(10, 120))
    bg, nb = [], []
    for l in rs.iter_lines():
        if stop_flag is not None and stop_flag():
            break
        if not l:
            continue
        L = l.decode(errors='ignore')
        if '"eventType":"aiImageResult"' in L:
            s = L.find('"imageUrl":"') + 12
            e = L.find('"', s)
            if s > 12:
                bg.append(L[s:e])
        if '"eventType":"aiImageWithoutBackgroundResult"' in L:
            s = L.find('"imageUrl":"') + 12
            e = L.find('"', s)
            if s > 12:
                nb.append(L[s:e])
    return bg, nb
class GenerationThread(QThread):
    finished_ok = pyqtSignal(list, list)
    error = pyqtSignal(str)
    def __init__(self, prompt, sid, asp, cfg=9, steps=45, count=4):
        super().__init__()
        self.prompt = prompt
        self.sid = sid
        self.asp = asp
        self.cfg = cfg
        self.steps = steps
        self.count = count
        self._stop = False
    def stop(self):
        self._stop = True
    def run(self):
        try:
            bg, nb = _gen(self.prompt, self.sid, self.asp, self.cfg, self.steps, self.count,
                          stop_flag=lambda: self._stop)
            if self._stop:
                return
            if not bg:
                self.error.emit("No images generated")
            else:
                self.finished_ok.emit(bg, nb)
        except Exception as e:
            if not self._stop:
                self.error.emit(str(e))
class ImageLoader(QThread):
    loaded = pyqtSignal(QPixmap)
    def __init__(self, url):
        super().__init__()
        self.url = url
    def run(self):
        try:
            r = requests.get(self.url, timeout=60, verify=False)
            r.raise_for_status()
            img = QImage()
            img.loadFromData(r.content)
            self.loaded.emit(QPixmap.fromImage(img))
        except Exception:
            self.loaded.emit(QPixmap())
class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.setFixedHeight(36)
        self.dragging = False
        self.drag_position = QPoint()
        self.setStyleSheet(f"""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 {COLORS['primary']}, stop:1 {COLORS['accent']});
            border-top-left-radius: 10px;
            border-top-right-radius: 10px;
        """)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(12, 0, 8, 0)
        layout.setSpacing(8)
        self.title_label = QLabel(f"  {BRAND_NAME} AI PHOTO STUDIO")
        self.title_label.setStyleSheet("""
            color: white;
            font-weight: 700;
            font-size: 12px;
            background: transparent;
        """)
        layout.addWidget(self.title_label)
        layout.addStretch()
        self.minimize_btn = self.create_button("")
        self.minimize_btn.clicked.connect(self.parent.showMinimized)
        self.maximize_btn = self.create_button("")
        self.maximize_btn.clicked.connect(self.toggle_maximize)
        self.close_btn = self.create_button("", close=True)
        self.close_btn.clicked.connect(self.parent.close)
        layout.addWidget(self.minimize_btn)
        layout.addWidget(self.maximize_btn)
        layout.addWidget(self.close_btn)
    def create_button(self, text, close=False):
        btn = QPushButton(text)
        btn.setFixedSize(30, 24)
        if close:
            btn.setStyleSheet("""
                QPushButton { background-color: rgba(255,255,255,0.15); color: white;
                    border: none; border-radius: 4px; font-weight: bold; }
                QPushButton:hover { background-color: rgba(244,67,54,0.85); }
                QPushButton:pressed { background-color: rgba(211,47,47,0.95); }
            """)
        else:
            btn.setStyleSheet("""
                QPushButton { background-color: rgba(255,255,255,0.15); color: white;
                    border: none; border-radius: 4px; font-weight: bold; }
                QPushButton:hover { background-color: rgba(255,255,255,0.25); }
                QPushButton:pressed { background-color: rgba(255,255,255,0.35); }
            """)
        return btn
    def toggle_maximize(self):
        if self.parent.isMaximized():
            self.parent.showNormal()
        else:
            self.parent.showMaximized()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.drag_position = event.globalPos() - self.parent.frameGeometry().topLeft()
            event.accept()
    def mouseMoveEvent(self, event):
        if self.dragging and event.buttons() == Qt.LeftButton and not self.parent.isMaximized():
            self.parent.move(event.globalPos() - self.drag_position)
            event.accept()
    def mouseReleaseEvent(self, event):
        self.dragging = False
        event.accept()
    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.toggle_maximize()
class ImageLabel(QLabel):
    clicked = pyqtSignal(str)
    def __init__(self, url=None):
        super().__init__()
        self.url = url
        self._pixmap = QPixmap()
        self.setAlignment(Qt.AlignCenter)
        self.setStyleSheet(f"""
            QLabel {{
                background-color: {COLORS['darker']};
                border: 1px solid {COLORS['border']};
                border-radius: 6px;
                color: {COLORS['text_secondary']};
            }}
            QLabel:hover {{
                border: 1px solid {COLORS['primary']};
            }}
        """)
        self.setMinimumSize(200, 200)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
    def set_image_pixmap(self, pixmap):
        self._pixmap = pixmap
        self.update_scaled()
    def update_scaled(self):
        if not self._pixmap.isNull():
            scaled = self._pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.setPixmap(scaled)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.update_scaled()
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.url:
            self.clicked.emit(self.url)
class ImagePreviewDialog(QDialog):
    def __init__(self, image_url, parent=None):
        super().__init__(parent)
        self.lang = getattr(parent, 'lang', 'tr')
        self.setWindowTitle(self.trx("preview"))
        self.resize(900, 700)
        self._pixmap = QPixmap()
        self._loader = None
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['background']};
            }}
            QLabel {{
                color: {COLORS['text']};
                background: transparent;
            }}
            QPushButton#primaryButton {{
                background-color: {COLORS['button_bg']};
                color: #000000;
                border: none;
                border-radius: 6px;
                padding: 10px 24px;
                font-weight: 700;
                font-size: 10pt;
                min-width: 100px;
                min-height: 20px;
            }}
            QPushButton#primaryButton:hover {{
                background-color: {COLORS['button_hover']};
            }}
            QPushButton#primaryButton:pressed {{
                background-color: {COLORS['button_pressed']};
            }}
            QPushButton#secondaryButton {{
                background-color: {COLORS['dark']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 6px;
                padding: 10px 24px;
                font-weight: 700;
                font-size: 10pt;
                min-width: 100px;
                min-height: 20px;
            }}
            QPushButton#secondaryButton:hover {{
                background-color: {COLORS['panel']};
                border-color: {COLORS['primary']};
                color: {COLORS['primary_light']};
            }}
            QPushButton#secondaryButton:pressed {{
                background-color: {COLORS['primary_dark']};
                color: white;
                border-color: {COLORS['primary']};
            }}
        """)
        layout = QVBoxLayout(self)
        self.label = QLabel(self.trx("loading"))
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.label)
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        save_btn = QPushButton(self.trx("download"))
        save_btn.setObjectName("primaryButton")
        save_btn.setCursor(Qt.PointingHandCursor)
        save_btn.clicked.connect(lambda: self.save_image(image_url))
        btn_layout.addWidget(save_btn)
        close_btn = QPushButton(self.trx("close"))
        close_btn.setObjectName("secondaryButton")
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)
        self._loader = ImageLoader(image_url)
        self._loader.loaded.connect(self.on_loaded)
        self._loader.start()
    def trx(self, key):
        return TRANSLATIONS.get(self.lang, TRANSLATIONS["tr"]).get(key, key)
    def on_loaded(self, pixmap):
        if pixmap and not pixmap.isNull():
            self._pixmap = pixmap
            self._update_label()
        else:
            self.label.setText(self.trx("load_failed"))
    def _update_label(self):
        if not self._pixmap.isNull():
            scaled = self._pixmap.scaled(self.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.label.setPixmap(scaled)
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._update_label()
    def closeEvent(self, event):
        if self._loader is not None and self._loader.isRunning():
            self._loader.quit()
            self._loader.wait(1500)
        event.accept()
    def save_image(self, url):
        path, _ = QFileDialog.getSaveFileName(self, self.trx("download"), f"Can-CoDev_{int(time.time())}.png", "PNG (*.png)")
        if path:
            try:
                r = requests.get(url, timeout=60, verify=False)
                with open(path, 'wb') as f:
                    f.write(r.content)
                QMessageBox.information(self, self.trx("success"), self.trx("image_saved"))
            except Exception as e:
                QMessageBox.critical(self, self.trx("error"), str(e))
class GeneratePage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.lang = "tr"
        self.selected_style = None
        self.selected_aspect = None
        self.current_images = []
        self.current_nb_images = []
        self.current_prompt = ""
        self.generation_thread = None
        self._loaders = []
        self.init_ui()
    def trx(self, key):
        return TRANSLATIONS.get(self.lang, TRANSLATIONS["tr"]).get(key, key)
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        splitter = QSplitter(Qt.Horizontal)
        splitter.setChildrenCollapsible(False)
        splitter.setHandleWidth(8)
        left_panel = QWidget()
        left_panel.setObjectName("leftPanel")
        left_panel.setMinimumWidth(360)
        left_panel.setMaximumWidth(500)
        left_outer = QVBoxLayout(left_panel)
        left_outer.setContentsMargins(0, 0, 0, 0)
        scroll = QScrollArea()
        scroll.setObjectName("controlScroll")
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        left_content = QWidget()
        left_content.setObjectName("leftContent")
        ll = QVBoxLayout(left_content)
        ll.setContentsMargins(12, 12, 12, 12)
        ll.setSpacing(12)
        lang_group = QGroupBox()
        lang_layout = QHBoxLayout(lang_group)
        self.language_label = QLabel(self.trx("language"))
        self.language_combo = QComboBox()
        self.language_combo.addItems(list(LANGUAGES.keys()))
        self.language_combo.currentTextChanged.connect(self.on_language_changed)
        lang_layout.addWidget(self.language_label)
        lang_layout.addStretch()
        lang_layout.addWidget(self.language_combo)
        ll.addWidget(lang_group)
        self.prompt_group = QGroupBox()
        self.prompt_group.setTitle(self.trx("prompt_label"))
        pl = QVBoxLayout(self.prompt_group)
        self.prompt_input = QTextEdit()
        self.prompt_input.setPlaceholderText(self.trx("prompt_placeholder"))
        self.prompt_input.setFixedHeight(90)
        pl.addWidget(self.prompt_input)
        prompt_btn_row = QHBoxLayout()
        self.random_btn = QPushButton(self.trx("random_prompt"))
        self.random_btn.setObjectName("secondaryButton")
        self.random_btn.clicked.connect(self.random_prompt)
        prompt_btn_row.addWidget(self.random_btn)
        self.copy_prompt_btn = QPushButton(self.trx("copy_prompt"))
        self.copy_prompt_btn.setObjectName("secondaryButton")
        self.copy_prompt_btn.clicked.connect(self.copy_prompt)
        prompt_btn_row.addWidget(self.copy_prompt_btn)
        pl.addLayout(prompt_btn_row)
        ll.addWidget(self.prompt_group)
        self.style_group = QGroupBox()
        self.style_group.setTitle(self.trx("style_select"))
        sl = QVBoxLayout(self.style_group)
        self.style_combo = QComboBox()
        for sid, sn in STYLES:
            self.style_combo.addItem(sn, sid)
        self.style_combo.currentIndexChanged.connect(self.on_style_changed)
        sl.addWidget(self.style_combo)
        ll.addWidget(self.style_group)
        self.aspect_group = QGroupBox()
        self.aspect_group.setTitle(self.trx("aspect_select"))
        al = QVBoxLayout(self.aspect_group)
        self.aspect_combo = QComboBox()
        for a, n in ASPECTS:
            self.aspect_combo.addItem(f"{n} ({a})", a)
        self.aspect_combo.currentIndexChanged.connect(self.on_aspect_changed)
        al.addWidget(self.aspect_combo)
        ll.addWidget(self.aspect_group)
        self.generate_btn = QPushButton(self.trx("generate"))
        self.generate_btn.setObjectName("primaryButton")
        self.generate_btn.setMinimumHeight(48)
        self.generate_btn.clicked.connect(self.generate)
        ll.addWidget(self.generate_btn)
        self.progress = QProgressBar()
        self.progress.setRange(0, 0)
        self.progress.setVisible(False)
        self.progress.setStyleSheet(f"""
            QProgressBar {{
                background-color: {COLORS['darker']};
                border: 1px solid {COLORS['border']};
                border-radius: 4px;
                height: 6px;
                text-align: center;
                color: transparent;
            }}
            QProgressBar::chunk {{
                background-color: {COLORS['primary']};
                border-radius: 3px;
            }}
        """)
        ll.addWidget(self.progress)
        ll.addStretch()
        scroll.setWidget(left_content)
        left_outer.addWidget(scroll)
        right_panel = QWidget()
        right_panel.setObjectName("rightPanel")
        right_panel.setMinimumWidth(500)
        rl = QVBoxLayout(right_panel)
        rl.setContentsMargins(12, 12, 12, 12)
        rl.setSpacing(10)
        top_row = QHBoxLayout()
        self.preview_title = QLabel(self.trx("preview"))
        self.preview_title.setStyleSheet(f"""
            color: {COLORS['primary']};
            font-size: 13px;
            font-weight: 700;
            background: transparent;
        """)
        self.status_label = QLabel(self.trx("ready"))
        self.status_label.setStyleSheet(f"""
            color: {COLORS['text_secondary']};
            font-size: 10px;
            background: transparent;
        """)
        top_row.addWidget(self.preview_title)
        top_row.addStretch()
        top_row.addWidget(self.status_label)
        rl.addLayout(top_row)
        self.image_grid = QGridLayout()
        self.image_grid.setSpacing(10)
        self.image_labels = []
        for i in range(4):
            lbl = ImageLabel()
            lbl.setText(self.trx("no_images"))
            lbl.clicked.connect(self.show_preview)
            self.image_labels.append(lbl)
            self.image_grid.addWidget(lbl, i // 2, i % 2)
        rl.addLayout(self.image_grid, 1)
        action_row = QHBoxLayout()
        self.regen_btn = QPushButton(self.trx("regenerate"))
        self.regen_btn.setObjectName("secondaryButton")
        self.regen_btn.clicked.connect(self.generate)
        self.regen_btn.setEnabled(False)
        action_row.addWidget(self.regen_btn)
        self.nobg_btn = QPushButton(self.trx("show_no_bg"))
        self.nobg_btn.setObjectName("secondaryButton")
        self.nobg_btn.clicked.connect(self.show_no_bg)
        self.nobg_btn.setEnabled(False)
        action_row.addWidget(self.nobg_btn)
        self.download_all_btn = QPushButton(self.trx("download_all"))
        self.download_all_btn.setObjectName("secondaryButton")
        self.download_all_btn.clicked.connect(self.download_all)
        self.download_all_btn.setEnabled(False)
        action_row.addWidget(self.download_all_btn)
        rl.addLayout(action_row)
        splitter.addWidget(left_panel)
        splitter.addWidget(right_panel)
        splitter.setSizes([390, 760])
        splitter.setStretchFactor(0, 0)
        splitter.setStretchFactor(1, 1)
        layout.addWidget(splitter)
    def on_language_changed(self, lang_name):
        self.lang = LANGUAGES.get(lang_name, "tr")
        self.retranslate_ui()
        self.main_window.set_language(self.lang)
    def retranslate_ui(self):
        self.prompt_group.setTitle(self.trx("prompt_label"))
        self.prompt_input.setPlaceholderText(self.trx("prompt_placeholder"))
        self.style_group.setTitle(self.trx("style_select"))
        self.aspect_group.setTitle(self.trx("aspect_select"))
        self.generate_btn.setText(self.trx("generate"))
        self.regen_btn.setText(self.trx("regenerate"))
        self.random_btn.setText(self.trx("random_prompt"))
        self.copy_prompt_btn.setText(self.trx("copy_prompt"))
        self.preview_title.setText(self.trx("preview"))
        self.nobg_btn.setText(self.trx("show_no_bg"))
        self.download_all_btn.setText(self.trx("download_all"))
        self.language_label.setText(self.trx("language"))
        if not self.current_images:
            self.status_label.setText(self.trx("ready"))
            for lbl in self.image_labels:
                if lbl._pixmap.isNull() and not lbl.url:
                    lbl.setText(self.trx("no_images"))
    def on_style_changed(self, idx):
        self.selected_style = self.style_combo.itemData(idx)
    def on_aspect_changed(self, idx):
        self.selected_aspect = self.aspect_combo.itemData(idx)
    def random_prompt(self):
        self.prompt_input.setPlainText(random.choice(RANDOM_PROMPTS))
    def copy_prompt(self):
        txt = self.prompt_input.toPlainText().strip()
        if txt:
            QApplication.clipboard().setText(txt)
            self.status_label.setText(self.trx("prompt_copied"))
            QTimer.singleShot(2000, lambda: self.status_label.setText(self.trx("ready")))
    def _track_loader(self, loader):
        self._loaders.append(loader)
        loader.finished.connect(lambda l=loader: self._loaders.remove(l) if l in self._loaders else None)
    def generate(self):
        prompt = self.prompt_input.toPlainText().strip()
        if len(prompt) < 3:
            self.show_msg(self.trx("error"), self.trx("prompt_too_short"), QMessageBox.Warning)
            return
        if not self.selected_style:
            self.selected_style = self.style_combo.itemData(0)
        if not self.selected_aspect:
            self.selected_aspect = self.aspect_combo.itemData(0)
        if self.generation_thread is not None and self.generation_thread.isRunning():
            self.generation_thread.stop()
            self.generation_thread.quit()
            self.generation_thread.wait(2000)
        self.current_prompt = prompt
        self.generate_btn.setEnabled(False)
        self.regen_btn.setEnabled(False)
        self.progress.setVisible(True)
        self.status_label.setText(self.trx("generating"))
        for lbl in self.image_labels:
            lbl._pixmap = QPixmap()
            lbl.setPixmap(QPixmap())
            lbl.url = None
            lbl.setText("...")
        self.generation_thread = GenerationThread(prompt, self.selected_style, self.selected_aspect)
        self.generation_thread.finished_ok.connect(self.on_generation_done)
        self.generation_thread.error.connect(self.on_generation_error)
        self.generation_thread.start()
    def on_generation_done(self, bg_urls, nb_urls):
        self.progress.setVisible(False)
        self.generate_btn.setEnabled(True)
        self.regen_btn.setEnabled(True)
        self.current_images = bg_urls
        self.current_nb_images = nb_urls
        for i, url in enumerate(bg_urls[:4]):
            loader = ImageLoader(url)
            loader.loaded.connect(lambda pix, idx=i, u=url: self.set_image(idx, pix, u))
            self._track_loader(loader)
            loader.start()
        self.status_label.setText(f"{len(bg_urls)} {self.trx('images_count')}")
        self.nobg_btn.setEnabled(bool(nb_urls))
        self.download_all_btn.setEnabled(bool(bg_urls))
        self.main_window.add_history({
            "prompt": self.current_prompt,
            "style": self.selected_style,
            "aspect": self.selected_aspect,
            "images": bg_urls,
            "time": time.time()
        })
    def set_image(self, idx, pixmap, url):
        if idx < len(self.image_labels):
            self.image_labels[idx].url = url
            if not pixmap.isNull():
                self.image_labels[idx].set_image_pixmap(pixmap)
            else:
                self.image_labels[idx].setText(self.trx("load_failed"))
    def on_generation_error(self, msg):
        self.progress.setVisible(False)
        self.generate_btn.setEnabled(True)
        self.status_label.setText(f"{self.trx('error')}: {msg}")
        self.show_msg(self.trx("error"), self.trx("generation_failed"), QMessageBox.Critical)
        for lbl in self.image_labels:
            lbl._pixmap = QPixmap()
            lbl.setPixmap(QPixmap())
            lbl.url = None
            lbl.setText(self.trx("no_images"))
    def show_preview(self, url):
        ImagePreviewDialog(url, self).exec_()
    def show_no_bg(self):
        if not self.current_nb_images:
            self.show_msg(self.trx("error"), self.trx("no_bg_images"), QMessageBox.Warning)
            return
        dlg = QDialog(self)
        dlg.setWindowTitle(self.trx("no_background_title"))
        dlg.resize(900, 700)
        dlg.setStyleSheet(f"""
            QDialog {{
                background-color: {COLORS['background']};
            }}
            QLabel {{
                color: {COLORS['text']};
                background: transparent;
            }}
            QPushButton#secondaryButton {{
                background-color: {COLORS['dark']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 6px;
                padding: 10px 24px;
                font-weight: 700;
                font-size: 10pt;
                min-width: 100px;
                min-height: 20px;
            }}
            QPushButton#secondaryButton:hover {{
                background-color: {COLORS['panel']};
                border-color: {COLORS['primary']};
                color: {COLORS['primary_light']};
            }}
            QPushButton#secondaryButton:pressed {{
                background-color: {COLORS['primary_dark']};
                color: white;
                border-color: {COLORS['primary']};
            }}
        """)
        layout = QVBoxLayout(dlg)
        grid = QGridLayout()
        labels = []
        for i, url in enumerate(self.current_nb_images[:4]):
            lbl = ImageLabel(url)
            lbl.clicked.connect(lambda u: ImagePreviewDialog(u, dlg).exec_())
            labels.append(lbl)
            grid.addWidget(lbl, i // 2, i % 2)
        layout.addLayout(grid)
        close_btn = QPushButton(self.trx("close"))
        close_btn.setObjectName("secondaryButton")
        close_btn.setCursor(Qt.PointingHandCursor)
        close_btn.clicked.connect(dlg.close)
        layout.addWidget(close_btn)
        dlg._loaders = []
        for i, url in enumerate(self.current_nb_images[:4]):
            loader = ImageLoader(url)
            loader.loaded.connect(lambda pix, idx=i: labels[idx].set_image_pixmap(pix) if not pix.isNull() else None)
            dlg._loaders.append(loader)
            loader.start()
        dlg.exec_()
        for loader in dlg._loaders:
            if loader.isRunning():
                loader.quit()
                loader.wait(1000)
    def download_all(self):
        if not self.current_images:
            return
        folder = QFileDialog.getExistingDirectory(self, self.trx("select_folder"))
        if not folder:
            return
        ts = int(time.time())
        saved = 0
        for i, url in enumerate(self.current_images):
            try:
                r = requests.get(url, timeout=60, verify=False)
                path = os.path.join(folder, f"Can-CoDev_{ts}_{i+1}.png")
                with open(path, 'wb') as f:
                    f.write(r.content)
                saved += 1
            except Exception:
                pass
        self.show_msg(self.trx("success"), f"{saved} {self.trx('image_saved')}", QMessageBox.Information)
    def show_msg(self, title, text, icon):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(icon)
        msg.setStyleSheet(f"""
            QMessageBox {{ background-color: {COLORS['dark']}; }}
            QMessageBox QLabel {{ color: {COLORS['text']}; min-width: 240px; }}
            QMessageBox QPushButton {{
                background-color: {COLORS['button_bg']}; color: black;
                border: none; border-radius: 6px; padding: 8px 16px; min-width: 80px;
            }}
        """)
        msg.exec_()
class HistoryPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.lang = "tr"
        self.init_ui()
    def trx(self, key):
        return TRANSLATIONS.get(self.lang, TRANSLATIONS["tr"]).get(key, key)
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        top = QHBoxLayout()
        self.title = QLabel(self.trx("history_title"))
        self.title.setStyleSheet(f"color: {COLORS['primary']}; font-size: 14px; font-weight: bold;")
        top.addWidget(self.title)
        top.addStretch()
        self.clear_btn = QPushButton(self.trx("clear_history"))
        self.clear_btn.setObjectName("secondaryButton")
        self.clear_btn.clicked.connect(self.clear_history)
        top.addWidget(self.clear_btn)
        layout.addLayout(top)
        self.list_widget = QListWidget()
        self.list_widget.setStyleSheet(f"""
            QListWidget {{
                background-color: {COLORS['darker']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 8px;
                padding: 6px;
                font-size: 12px;
            }}
            QListWidget::item {{
                padding: 8px;
                border-bottom: 1px solid {COLORS['border']};
            }}
            QListWidget::item:selected {{
                background-color: {COLORS['primary']};
                color: black;
            }}
        """)
        self.list_widget.itemDoubleClicked.connect(self.on_item_double_click)
        layout.addWidget(self.list_widget)
        self.refresh()
    def retranslate_ui(self):
        self.title.setText(self.trx("history_title"))
        self.clear_btn.setText(self.trx("clear_history"))
        self.refresh()
    def refresh(self):
        self.list_widget.clear()
        for item in reversed(self.main_window.history):
            ts = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["time"]))
            style_name = dict(STYLES).get(item["style"], item["style"])
            text = f"[{ts}] {style_name} | {item['aspect']}\n{item['prompt'][:80]}"
            li = QListWidgetItem(text)
            li.setData(Qt.UserRole, item)
            self.list_widget.addItem(li)
    def clear_history(self):
        self.main_window.history.clear()
        self.refresh()
    def on_item_double_click(self, item):
        data = item.data(Qt.UserRole)
        if data and data.get("images"):
            ImagePreviewDialog(data["images"][0], self).exec_()
class SettingsPage(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.lang = "tr"
        self.init_ui()
    def trx(self, key):
        return TRANSLATIONS.get(self.lang, TRANSLATIONS["tr"]).get(key, key)
    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(16)
        self.info_group = QGroupBox(self.trx("about"))
        self.info_group.setStyleSheet(f"""
            QGroupBox {{
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 8px;
                margin-top: 10px;
                padding: 16px;
                font-weight: bold;
                background-color: {COLORS['dark']};
            }}
            QGroupBox::title {{
                color: {COLORS['primary']};
                left: 12px; padding: 0 6px;
            }}
        """)
        il = QVBoxLayout(self.info_group)
        self.about_label = QLabel(self.trx("about_text"))
        self.about_label.setWordWrap(True)
        self.about_label.setStyleSheet(f"color: {COLORS['text']}; font-weight: normal; line-height: 1.5;")
        il.addWidget(self.about_label)
        layout.addWidget(self.info_group)
        self.api_group = QGroupBox(self.trx("api_settings"))
        self.api_group.setStyleSheet(f"""
            QGroupBox {{
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 8px;
                margin-top: 10px;
                padding: 16px;
                font-weight: bold;
                background-color: {COLORS['dark']};
            }}
            QGroupBox::title {{
                color: {COLORS['primary']};
                left: 12px; padding: 0 6px;
            }}
        """)
        ail = QVBoxLayout(self.api_group)
        api_label = QLabel(self.trx("photoroom_info") + "\n\n" +
                           "• Endpoint: serverless-api.photoroom.com\n" +
                           "• Model: expert\n" +
                           "• Sampler: dpmpp_2m_karras\n" +
                           "• Hires fix: aktif\n" +
                           "• Face restore: aktif\n" +
                           "• Upscale: 2x")
        api_label.setWordWrap(True)
        api_label.setStyleSheet(f"color: {COLORS['text_secondary']}; font-weight: normal; font-family: 'Consolas';")
        ail.addWidget(api_label)
        layout.addWidget(self.api_group)
        layout.addStretch()
        self.footer = QLabel(f"{self.trx('designed_by')} {BRAND_NAME}")
        self.footer.setAlignment(Qt.AlignCenter)
        self.footer.setStyleSheet(f"color: {COLORS['primary']}; font-size: 12px; font-weight: bold; padding: 10px;")
        layout.addWidget(self.footer)
    def retranslate_ui(self):
        self.info_group.setTitle(self.trx("about"))
        self.api_group.setTitle(self.trx("api_settings"))
        self.about_label.setText(self.trx("about_text"))
        self.footer.setText(f"{self.trx('designed_by')} {BRAND_NAME}")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.lang = "tr"
        self.history = []
        self.setWindowTitle(f"{BRAND_NAME} AI Photo Studio")
        self.setGeometry(100, 80, 1280, 820)
        self.setMinimumSize(1020, 700)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.init_ui()
        self.apply_styles()
        self.set_dark_palette()
    def trx(self, key):
        return TRANSLATIONS.get(self.lang, TRANSLATIONS["tr"]).get(key, key)
    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        self.title_bar = CustomTitleBar(self)
        main_layout.addWidget(self.title_bar)
        content = QWidget()
        content.setObjectName("contentWidget")
        cl = QVBoxLayout(content)
        cl.setContentsMargins(10, 10, 10, 10)
        self.tabs = QTabWidget()
        self.tabs.setObjectName("mainTabs")
        self.generate_page = GeneratePage(self)
        self.history_page = HistoryPage(self)
        self.settings_page = SettingsPage(self)
        self.tabs.addTab(self.generate_page, "" + self.trx("tab_generate"))
        self.tabs.addTab(self.history_page, "" + self.trx("tab_history"))
        self.tabs.addTab(self.settings_page, "" + self.trx("tab_settings"))
        cl.addWidget(self.tabs)
        main_layout.addWidget(content)
    def set_language(self, code):
        self.lang = code
        self.history_page.lang = code
        self.settings_page.lang = code
        self.tabs.setTabText(0, "" + self.trx("tab_generate"))
        self.tabs.setTabText(1, "" + self.trx("tab_history"))
        self.tabs.setTabText(2, "" + self.trx("tab_settings"))
        self.history_page.retranslate_ui()
        self.settings_page.retranslate_ui()
    def add_history(self, item):
        self.history.append(item)
        if hasattr(self, 'history_page'):
            self.history_page.refresh()
    def apply_styles(self):
        self.setStyleSheet(f"""
            QMainWindow {{
                background: transparent;
                color: {COLORS['text']};
                font-family: 'Segoe UI';
                font-size: 9pt;
            }}
            #contentWidget {{
                background-color: {COLORS['background']};
                border-bottom-left-radius: 10px;
                border-bottom-right-radius: 10px;
            }}
            #leftPanel, #rightPanel, #leftContent {{
                background-color: {COLORS['panel']};
                border-radius: 8px;
            }}
            QScrollArea, #controlScroll {{
                background-color: {COLORS['panel']};
                border: none;
            }}
            QScrollArea > QWidget > QWidget {{
                background-color: {COLORS['panel']};
            }}
            QTabWidget::pane {{
                border: 1px solid {COLORS['border']};
                background: {COLORS['background']};
                border-radius: 8px;
                top: -1px;
            }}
            QTabBar::tab {{
                background: {COLORS['dark']};
                color: {COLORS['text_secondary']};
                border: 1px solid {COLORS['border']};
                padding: 10px 22px;
                margin-right: 4px;
                min-width: 130px;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                font-weight: 600;
            }}
            QTabBar::tab:selected {{
                background: {COLORS['panel']};
                color: {COLORS['primary']};
                border-bottom: 1px solid {COLORS['panel']};
            }}
            QTabBar::tab:hover {{
                color: {COLORS['primary_light']};
            }}
            QSplitter {{
                background: transparent;
            }}
            QSplitter::handle {{
                background-color: {COLORS['border']};
                margin: 4px 0;
                border-radius: 3px;
            }}
            QSplitter::handle:hover {{
                background-color: {COLORS['primary_dark']};
            }}
            QGroupBox {{
                border: 1px solid {COLORS['border']};
                border-radius: 8px;
                margin-top: 10px;
                padding-top: 14px;
                font-weight: bold;
                font-size: 9pt;
                background-color: {COLORS['dark']};
                color: {COLORS['text']};
            }}
            QGroupBox::title {{
                subcontrol-origin: margin;
                left: 10px;
                padding: 0 6px;
                color: {COLORS['primary']};
                background-color: {COLORS['dark']};
            }}
            QLabel {{
                color: {COLORS['text']};
                background: transparent;
            }}
            QTextEdit, QComboBox, QLineEdit {{
                background-color: {COLORS['darker']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                border-radius: 5px;
                padding: 6px;
                selection-background-color: {COLORS['primary']};
                selection-color: black;
            }}
            QTextEdit:focus, QComboBox:focus, QLineEdit:focus {{
                border: 1px solid {COLORS['primary']};
            }}
            QComboBox::drop-down {{
                border: none;
                width: 20px;
            }}
            QComboBox::down-arrow {{
                image: none;
                border-left: 4px solid transparent;
                border-right: 4px solid transparent;
                border-top: 5px solid {COLORS['primary']};
                margin-right: 6px;
            }}
            QComboBox QAbstractItemView {{
                background-color: {COLORS['darker']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
                selection-background-color: {COLORS['primary']};
                selection-color: black;
                outline: none;
            }}
            QPushButton {{
                border-radius: 6px;
                padding: 8px 12px;
                font-weight: 600;
                border: 1px solid {COLORS['border']};
            }}
            QPushButton#primaryButton {{
                background-color: {COLORS['button_bg']};
                color: black;
                border: none;
                font-size: 10pt;
            }}
            QPushButton#primaryButton:hover {{
                background-color: {COLORS['button_hover']};
            }}
            QPushButton#primaryButton:pressed {{
                background-color: {COLORS['button_pressed']};
            }}
            QPushButton#primaryButton:disabled {{
                background-color: {COLORS['darker']};
                color: {COLORS['text_secondary']};
            }}
            QPushButton#secondaryButton {{
                background-color: {COLORS['dark']};
                color: {COLORS['text']};
                border: 1px solid {COLORS['border']};
            }}
            QPushButton#secondaryButton:hover {{
                background-color: {COLORS['panel']};
                border-color: {COLORS['primary']};
                color: {COLORS['primary_light']};
            }}
            QPushButton#secondaryButton:pressed {{
                background-color: {COLORS['primary_dark']};
                color: white;
                border-color: {COLORS['primary']};
            }}
            QPushButton#secondaryButton:disabled {{
                background-color: {COLORS['darker']};
                color: {COLORS['text_secondary']};
                border-color: {COLORS['border']};
            }}
            QScrollBar:vertical {{
                background: {COLORS['darker']};
                width: 10px;
                border-radius: 4px;
                margin: 2px;
            }}
            QScrollBar::handle:vertical {{
                background: {COLORS['border']};
                border-radius: 4px;
                min-height: 24px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {COLORS['primary_dark']};
            }}
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
                height: 0px;
            }}
            QScrollBar:horizontal {{
                background: {COLORS['darker']};
                height: 10px;
                border-radius: 4px;
                margin: 2px;
            }}
            QScrollBar::handle:horizontal {{
                background: {COLORS['border']};
                border-radius: 4px;
                min-width: 24px;
            }}
            QScrollBar::handle:horizontal:hover {{
                background: {COLORS['primary_dark']};
            }}
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
                width: 0px;
            }}
        """)
    def set_dark_palette(self):
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(COLORS['background']))
        palette.setColor(QPalette.WindowText, QColor(COLORS['text']))
        palette.setColor(QPalette.Base, QColor(COLORS['dark']))
        palette.setColor(QPalette.AlternateBase, QColor(COLORS['darker']))
        palette.setColor(QPalette.Text, QColor(COLORS['text']))
        palette.setColor(QPalette.Button, QColor(COLORS['dark']))
        palette.setColor(QPalette.ButtonText, QColor(COLORS['text']))
        palette.setColor(QPalette.Highlight, QColor(COLORS['primary']))
        palette.setColor(QPalette.HighlightedText, Qt.black)
        self.setPalette(palette)
    def closeEvent(self, event):
        gen = self.generate_page.generation_thread
        if gen is not None and gen.isRunning():
            reply = QMessageBox.question(
                self,
                self.trx("close_confirm_title"),
                self.trx("close_confirm_text"),
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply != QMessageBox.Yes:
                event.ignore()
                return
            gen.stop()
            gen.quit()
            if not gen.wait(3000):
                gen.terminate()
                gen.wait(1000)
        for loader in list(self.generate_page._loaders):
            try:
                if loader.isRunning():
                    loader.quit()
                    if not loader.wait(1500):
                        loader.terminate()
                        loader.wait(500)
            except Exception:
                pass
        self.generate_page._loaders.clear()
        event.accept()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(COLORS['background']))
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.rect(), 10, 10)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0, QColor(COLORS['dark']))
        gradient.setColorAt(1, QColor(COLORS['background']))
        painter.setBrush(gradient)
        painter.drawRoundedRect(self.rect().adjusted(1, 1, -1, -1), 9, 9)
def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setFont(QFont("Segoe UI", 9))
    window = MainWindow()
    window.show()
    ret = app.exec_()
    try:
        gen = window.generate_page.generation_thread
        if gen is not None and gen.isRunning():
            gen.stop()
            gen.terminate()
            gen.wait(1000)
    except Exception:
        pass
    try:
        for loader in list(window.generate_page._loaders):
            if loader.isRunning():
                loader.terminate()
                loader.wait(500)
        window.generate_page._loaders.clear()
    except Exception:
        pass
    sys.exit(ret)
if __name__ == "__main__":
    main()
