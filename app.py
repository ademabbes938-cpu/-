from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الشابة - مدينة برج خديجة</title>
    <style>
        body { font-family: sans-serif; margin: 0; background: #f4f7f6; text-align: center; }
        
        /* الصورة العلوية الكبيرة */
        header { 
            background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), 
            url('https://www.tourismtunisia.com/wp-content/uploads/2016/01/mahdia.jpg'); 
            background-size: cover; 
            background-position: center;
            height: 400px; 
            color: white; 
            display: flex; 
            flex-direction: column; 
            justify-content: center; 
            align-items: center; 
        }

        .container { padding: 40px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }
        
        .card { 
            background: white; 
            padding: 15px; 
            border-radius: 20px; 
            box-shadow: 0 10px 30px rgba(0,0,0,0.1); 
            width: 350px; 
        }

        /* تنسيق الصور داخل البطاقات لضمان ظهورها */
        .card img { 
            width: 100%; 
            height: 220px; 
            border-radius: 15px; 
            object-fit: cover; /* يحافظ على أبعاد الصورة */
            display: block;
            background: #eee; /* لون مؤقت إذا تأخر التحميل */
        }

        h2 { color: #d38b5d; }
    </style>
</head>
<body>
    <header>
        <h1>مدينة الشابة</h1>
        <p>جمال الطبيعة وعراقة التاريخ</p>
    </header>

    <div class="container">
        <div class="card">
            <h2>برج خديجة</h2>
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Borj_Khadija_Chebba.jpg/800px-Borj_Khadija_Chebba.jpg" alt="برج خديجة">
            <p>المعلم الأثري الشامخ بمدينة الشابة.</p>
        </div>

        <div class="card">
            <h2>ميناء الشابة</h2>
            <img src="https://st2.depositphotos.com/3362143/12093/i/950/depositphotos_120937812-stock-photo-harbor-with-fishing-boats-in.jpg" alt="الميناء">
            <p>من أجمل موانئ الصيد في تونس.</p>
        </div>
    </div>
    
    <footer>تطوير: آدم - مكنين 🇹🇳 2026</footer>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
