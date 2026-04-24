from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_PAGE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>الشابة | لؤلؤة المهدية</title>
    
    <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><rect width='100' height='100' rx='20' fill='%23d38b5d'/><path d='M30 80 H70 V40 L60 30 V20 H40 V30 L30 40 Z' fill='white'/></svg>">

    <style>
        :root { --main: #d38b5d; --blue: #0077be; --dark: #1a202c; }
        body { font-family: 'Segoe UI', Tahoma, sans-serif; margin: 0; background-color: #f0f2f5; color: var(--dark); }
        
        /* واجهة Dashboard احترافية */
        .sidebar { width: 250px; background: var(--dark); height: 100vh; position: fixed; right: 0; top: 0; color: white; padding: 20px; box-sizing: border-box; display: none; }
        
        .main-content { margin-right: 0; padding: 0; }

        /* قسم الصورة الكبيرة (Hero) */
        .hero { 
            height: 450px; 
            background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.5)), 
                        url('https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&q=80&w=1500');
            background-size: cover;
            background-position: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            color: white;
            border-bottom: 8px solid var(--main);
        }

        .hero h1 { font-size: 4rem; margin: 0; text-shadow: 2px 4px 10px rgba(0,0,0,0.5); }

        /* كروت لوحة التحكم */
        .dashboard-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 25px;
            padding: 40px;
            max-width: 1200px;
            margin: -80px auto 50px;
        }

        .card {
            background: white;
            border-radius: 25px;
            overflow: hidden;
            box-shadow: 0 15px 35px rgba(0,0,0,0.1);
            transition: 0.4s;
            border: 1px solid #eee;
        }

        .card:hover { transform: translateY(-10px); }

        .card-img {
            width: 100%;
            height: 200px;
            background-size: cover;
            background-position: center;
        }

        .card-body { padding: 25px; text-align: center; }
        .card-body h2 { color: var(--main); margin: 0 0 10px; font-size: 1.5rem; }
        .card-body p { color: #666; line-height: 1.6; }

        footer { background: var(--dark); color: white; padding: 40px; text-align: center; }
        .badge { background: var(--main); padding: 5px 15px; border-radius: 50px; font-size: 0.8rem; }
        
        @media (max-width: 768px) {
            .hero h1 { font-size: 2.5rem; }
            .dashboard-grid { padding: 20px; margin-top: -40px; }
        }
    </style>
</head>
<body>

    <div class="main-content">
        <header class="hero">
            <h1>الشابة - لؤلؤة الساحل</h1>
            <p>مرحباً بك في مدينة برج خديجة التاريخي</p>
        </header>

        <div class="dashboard-grid">
            <div class="card">
                <div class="card-img" style="background-image: url('https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/Borj_Khadija_Chebba.jpg/800px-Borj_Khadija_Chebba.jpg');"></div>
                <div class="card-body">
                    <h2>برج خديجة</h2>
                    <p>المعلم الأثري الشامخ الذي يحرس سواحل الشابة منذ قرون. رمز الصمود والجمال الرملي.</p>
                </div>
            </div>

            <div class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=600');"></div>
                <div class="card-body">
                    <h2>ميناء الصيد</h2>
                    <p>أنشط موانئ ولاية المهدية، حيث تلتقي مراكب الصيد التقليدية مع زرقة المتوسط لتنتج أجود أنواع السمك.</p>
                </div>
            </div>

            <div class="card">
                <div class="card-img" style="background-image: url('https://images.unsplash.com/photo-1559128010-7c1ad6e1b6a5?w=600');"></div>
                <div class="card-body">
                    <h2>شواطئ فيروزية</h2>
                    <p>تمتع بأجمل لحظات الاستجمام على رمال الشابة الذهبية ومياهها الصافية التي تجذب الزوار من كل مكان.</p>
                </div>
            </div>
        </div>

        <footer>
            <p>جميع الحقوق محفوظة لمدينة الشابة - ولاية المهدية</p>
            <div style="margin-top: 15px;">
                <span class="badge">تطوير: آدم - مكنين 🇹🇳</span>
            </div>
            <p style="opacity: 0.4; font-size: 0.7rem; margin-top: 20px;">تصميم Dashboard احترافي 2026</p>
        </footer>
    </div>

</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
