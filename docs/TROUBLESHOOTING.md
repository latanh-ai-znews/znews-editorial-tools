# Cẩm Nang Xử Lý Sự Cố & Khắc Phục Lỗi (Troubleshooting)

Tài liệu này tổng hợp toàn bộ các sự cố thường gặp nhất trong quá trình dựng bài đặc biệt trên CMS Znews, phân tích nguyên nhân gốc rễ và cung cấp giải pháp khắc phục tức thì.

---

## 🚨 Sự cố 1: Banner quảng cáo bị biến mất hoặc lệch khung hình

### Triệu chứng:
Bài viết hiển thị bình thường nhưng không thấy banner quảng cáo đầu trang, banner giữa các đoạn văn hoặc banner chân trang.

### Nguyên nhân gốc rễ:
- Bạn đã sử dụng đoạn CSS can thiệp vào khung trang chung của Znews, ví dụ:
  ```css
  /* SAI: Phá vỡ cấu trúc layout của CMS */
  .layout-no-sidebar { width: 100vw !important; max-width: none !important; }
  .article-content { margin: 0 auto !important; }
  ```
- Việc ép khung này làm khung chứa quảng cáo bị đẩy ra ngoài vùng hiển thị của trình duyệt hoặc bị script quảng cáo tính sai toạ độ.

### Cách khắc phục:
1. Xóa bỏ hoàn toàn các rule CSS tác động lên `.layout-no-sidebar` hoặc các class bên ngoài container bài viết của bạn.
2. Áp dụng kỹ thuật **tràn lề cục bộ** (xem [CMS_GUIDELINES.md](./CMS_GUIDELINES.md)): Chỉ mở rộng margin âm (`margin-left: -Npx; margin-right: -Npx;`) trên đúng các thẻ ảnh hoặc quote cụ thể.

---

## 📱 Sự cố 2: Trang bị trượt ngang (Horizontal Scrollbar) trên điện thoại

### Triệu chứng:
Khi xem bài trên mobile, người đọc có thể vô tình vuốt trang sang trái hoặc sang phải, lộ ra khoảng trống màu trắng ở mép phải.

### Nguyên nhân:
Một phần tử hình ảnh hoặc bảng (table) có độ rộng cố định vượt quá chiều rộng màn hình điện thoại (thường là > 360px), hoặc dùng `width: 100vw` mà quên trừ đi độ rộng của thanh cuộn hệ thống.

### Cách khắc phục:
1. Thêm thuộc tính bảo vệ chống tràn vào container chính của bài:
   ```css
   .znews-article-wrap {
     overflow-x: hidden;
     max-width: 100%;
   }
   ```
2. Trên màn hình mobile (`@media (max-width: 640px)`), luôn đặt `width: 100% !important; max-width: 100% !important;` cho tất cả ảnh và thẻ iframe.

---

## 🎨 Sự cố 3: Nền bài viết bị "ngả vàng" hoặc chữ bị tàng hình

### Triệu chứng:
- Bạn chọn màu nền pastel/kem (`#f3f0e9`) để tạo cảm giác chất giấy, nhưng khi lên trang Znews nhìn như màn hình bị ố vàng.
- Hoặc bạn chọn bài nền đen (Dark theme), nhưng các đoạn văn biến thành chữ đen xì trên nền đen.

### Nguyên nhân:
1. Nền trang Znews là màu trắng tinh (`#ffffff`). Bất kỳ khối màu kem nhạt nào chèn giữa trang đều bị mắt độc giả so sánh tương phản và cảm thấy "ngả vàng".
2. CMS Znews có rule ghi đè CSS mặc định: `p { color: #222 !important; }`. Khi bạn đổi màu nền thành đen, rule này của CMS biến chữ của bạn thành màu đen, khiến độc giả không thể đọc được.

### Cách khắc phục:
1. **Khuyến nghị tốt nhất**: Quay về dùng nền trắng tinh (`#ffffff`) và chữ đen (`#111111`). Tạo điểm nhấn bằng các đường viền nhẹ hoặc thẻ màu xám nhạt (`#f8fafc`).
2. Nếu bắt buộc làm nền tối, phải thêm rule chống ghi đè 2 lớp:
   ```css
   .container_dark_theme p,
   .container_dark_theme span,
   .container_dark_theme div {
     color: #f1f5f9 !important;
   }
   ```

---

## 🖼️ Sự cố 4: Ảnh bị co nhỏ bất thường (Hẹp hơn cả cột chữ)

### Triệu chứng:
Khi sửa lại một bài viết cũ đã xuất bản, ảnh minh họa tự dưng bị co hẹp lại ở giữa trang thay vì tràn rộng ra mép.

### Nguyên nhân:
Các mẫu code cũ từng dùng công thức:
`width: calc(100% - 40px); max-width: 866px;`
với giả định phần tử cha bị ép rộng ~1164px. Khi bỏ đoạn ép khung cũ, phần tử cha trở về độ rộng thật 600px, khiến công thức trên tính ra độ rộng chỉ còn ~560px (hẹp hơn cả chữ!).

### Cách khắc phục:
Thay thế toàn bộ công thức cũ bằng công thức tràn lề hiện đại:
```css
.bleed-image {
  width: calc(100% + 160px);
  margin-left: -80px;
  margin-right: -80px;
  max-width: 1000px;
}
```

---

## ✍️ Sự cố 5: Lỗi dấu gạch ngang dài (Em-dash)

### Triệu chứng:
Ban biên tập hoặc thư ký tòa soạn trả lại bài vì sử dụng gạch nối dài `—` hoặc `–`.

### Quy chuẩn của Znews:
Báo điện tử Znews áp dụng quy chuẩn biên tập: **Không dùng dấu em-dash (`—`) hay en-dash (`–`) giữa câu để ngắt ý, mà phải thay bằng dấu phẩy (`,`) hoặc dấu hai chấm (`:`)**.

### Cách khắc phục:
- Sử dụng công cụ **Trình tạo bài viết sách (CMS Books)**: Công cụ này đã được tích hợp sẵn bộ lọc regex tự động:
  ```javascript
  function fixEmdash(text) {
    return text.replace(/\s*[—–]\s*/g, ', ');
  }
  ```
- Hoặc dùng chức năng Find & Replace trên trình soạn thảo trước khi xuất bản.

---

## 🌐 Sự cố 6: GitHub Pages báo lỗi 404 hoặc không cập nhật nội dung mới

### Triệu chứng:
Bạn đã push code lên GitHub nhưng khi mở link `https://<username>.github.io/...` thì trang báo 404 hoặc vẫn hiện bản cũ.

### Cách xử lý:
1. **Kiểm tra trạng thái Build**:
   Mở terminal và gõ:
   ```bash
   gh api repos/latanhusesai-beep/znews-editorial-tools/pages --jq .status
   ```
   Nếu trả về `"building"`: hãy đợi thêm 30 giây. Khi trả về `"built"` là trang đã sẵn sàng.
2. **Xoá Cache trình duyệt**:
   Nhấn tổ hợp phím **`Cmd + Shift + R`** (trên Mac) hoặc **`Ctrl + F5`** (trên Windows) để tải lại trang không qua bộ nhớ đệm (Hard Refresh).
3. **Kiểm tra nhánh xuất bản**:
   Vào **Settings** > **Pages** trên GitHub repository, đảm bảo nhánh được chọn là `main` và thư mục là `/ (root)`.
