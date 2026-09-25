# Hướng Dẫn Dành Cho Lập Trình Viên (Developer Guide)

Tài liệu này hướng dẫn cách cài đặt môi trường, mở rộng thêm công cụ mới, kiểm thử và quản lý quy trình triển khai lên GitHub Pages cho dự án **Znews Editorial Studio**.

---

## 🛠️ 1. Cài Đặt Môi Trường & Chạy Cục Bộ (Local Setup)

Dự án không yêu cầu cài đặt các framework phức tạp (như Webpack, React hay Vite). Bạn có thể chạy ngay với các công cụ có sẵn.

### Cách 1: Sử dụng Python (Đơn giản nhất, có sẵn trên macOS/Linux)
```bash
# Di chuyển vào thư mục dự án
cd "Công cụ AI Znews"

# Khởi động server HTTP tĩnh ở cổng 8080
python3 -m http.server 8080
```
Mở trình duyệt truy cập: `http://localhost:8080`

### Cách 2: Sử dụng Node.js / npx
```bash
# Chạy tức thì với gói serve hoặc live-server
npx serve .
# Hoặc
npx live-server .
```

---

## ➕ 2. Quy Trình Thêm Một Công Cụ Mới Vào Studio

Khi ban biên tập có nhu cầu thêm một công cụ mới (ví dụ: *Trình tạo Infographic số liệu*, *Khung phỏng vấn Q&A*):

### Bước 1: Tạo tệp HTML cho công cụ
Tạo tệp mới, ví dụ: `infographic-tool.html`. Tuân thủ các nguyên tắc:
- Chạy 100% Client-side.
- CSS phải được bao bọc trong một class namespace riêng (Ví dụ: `.znews-infographic`).
- Cung cấp nút "Sao chép mã CMS" tiện lợi.

### Bước 2: Đăng ký công cụ vào `index.html`
Mở `index.html` và thực hiện 3 thao tác nhỏ:

1. **Thêm thẻ Card hiển thị vào danh sách công cụ**:
```html
<article class="tool-card" data-category="special" data-keywords="infographic so lieu bieu do thong ke">
  <div class="card-top">
    <div class="card-meta-row">
      <div class="tool-icon-wrap">📊</div>
      <span class="category-badge">Đồ hoạ số liệu</span>
    </div>
    <h3 class="tool-title">Trình tạo Infographic Số Liệu</h3>
    <p class="tool-desc">Mô tả ngắn gọn về tính năng và công dụng...</p>
    <ul class="features-list">
      <li>...Tính năng 1...</li>
      <li>...Tính năng 2...</li>
    </ul>
  </div>
  <div class="card-actions">
    <button class="btn btn-primary" onclick="launchApp('infographic-tool.html', 'Trình tạo Infographic')">
      🚀 Mở công cụ
    </button>
    <a href="infographic-tool.html" target="_blank" class="btn btn-secondary">Tab mới</a>
  </div>
</article>
```

2. **Thêm vào danh sách chuyển đổi nhanh (Tool Switcher)**:
Trong thẻ `<select id="toolSwitcher">`, thêm dòng:
```html
<option value="infographic-tool.html">Trình tạo Infographic</option>
```

3. **Cập nhật số đếm trên filter chips (nếu có)**.

### Bước 3: Kiểm thử
1. Mở `index.html` trên trình duyệt.
2. Kiểm tra tìm kiếm bằng phím `/`.
3. Bấm mở công cụ trong chế độ Studio (Iframe) xem thanh điều hướng và nút đóng có hoạt động mượt mà không.
4. Kiểm tra nút mở tab riêng.

---

## 🔄 3. Quy Trình Triển Khai Lên GitHub Pages (Deployment)

Mọi thay đổi sau khi được đẩy (`git push`) lên nhánh `main` của repository GitHub sẽ tự động được GitHub Pages xuất bản trong vòng **30 đến 60 giây**.

### Các lệnh cập nhật chuẩn:
```bash
# 1. Kiểm tra trạng thái các tệp đã sửa
git status

# 2. Thêm toàn bộ các thay đổi
git add -A

# 3. Tạo commit với thông điệp rõ ràng
git commit -m "feat: thêm công cụ infographic và cập nhật tài liệu hướng dẫn"

# 4. Đẩy mã nguồn lên GitHub
git push origin main
```

### Kiểm tra trạng thái deploy bằng GitHub CLI:
```bash
# Xem trạng thái build của GitHub Pages
gh api repos/latanhusesai-beep/znews-editorial-tools/pages --jq .status
# Khi trả về: "built" nghĩa là website đã cập nhật thành công!
```

---

## 📝 4. Tiêu Chuẩn Viết Mã (Coding Standards)

1. **Quy chuẩn Font**: Chỉ sử dụng font hệ thống (`Be Vietnam Pro`, `Inter`, `Newsreader`, `system-ui`). Tuyệt đối không gọi Google Fonts trong đoạn mã sinh ra để dán vào CMS.
2. **Quy chuẩn URL**: Không dùng đường dẫn tuyệt đối kiểu `C:\...` hoặc `/Users/anhle/...`. Luôn dùng đường dẫn tương đối hoặc link CDN HTTPS chính thức của Znews.
3. **Responsive Mobile First**: Mọi khối nội dung sinh ra phải được kiểm tra cẩn thận trên độ phân giải màn hình 375px (iPhone tiêu chuẩn) để đảm bảo không bị tràn chiều ngang (overflow-x).
4. **Không phụ thuộc thư viện nặng**: Tránh dùng jQuery, Bootstrap hay các thư viện cồng kềnh. Hãy viết bằng CSS hiện đại (Flexbox/Grid) và Vanilla Javascript (ES6+).
