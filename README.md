# Znews Editorial Studio — Bộ Công Cụ AI & Dàn Trang Báo Chí

Hệ thống công cụ biên tập, dàn trang tạp chí, xử lý ảnh và tạo bài viết chuyên đề chuẩn CMS báo điện tử **Znews**. Hoạt động hoàn toàn trên trình duyệt (Client-side), không phụ thuộc backend, hỗ trợ đầy đủ thiết bị di động và máy tính bàn.

---

## 🚀 Danh sách công cụ tích hợp

### 1. 📰 Znews Magazine Layouts Generator (v10.13)
*File: `tool-znews-magazine-v10-13.html`*
- Dàn trang Magazine & Longform chuyên sâu với hơn 6 phong cách bố cục hiện đại.
- Hỗ trợ import mã nguồn bài viết, tùy biến typography và màu sắc theo chuyên mục.
- Tích hợp hiệu ứng cuộn Parallax mượt mà, sticky elements và đa dạng khối hero cover.
- Sinh mã nhúng HTML/CSS tối ưu, chống xung đột hoàn toàn với CMS Znews.

### 2. 🛡️ Dựng bài đặc biệt No Side-bar (Ad-Safe)
*File: `no-side-bar-ad-safe-tool.html`*
- Giải pháp xây dựng bài viết định dạng `layout-no-sidebar` an toàn tuyệt đối cho quảng cáo.
- Đảm bảo banner quảng cáo đầu trang, giữa bài và cuối bài luôn hiển thị nguyên vẹn.
- Tự động quét và nhận diện cụm ≥3 ảnh liên tiếp để ghép carousel/grid; tự động bắt trích dẫn (quote).
- Tuân thủ công thức tràn lề cục bộ và quy chuẩn nền sáng chữ tối của CMS.

### 3. 📷 Công cụ dựng bài ảnh (Photo Essay)
*File: `photo-essay-tool.html`*
- Thiết kế riêng cho thể loại phóng sự ảnh và visual storytelling.
- Hỗ trợ ảnh bìa toàn cảnh (Hero full-bleed), lưới ảnh so sánh 2-3 cột, chú thích ảnh chi tiết.
- Tính năng chuyển đổi nhanh (1-click converter) từ bài báo ảnh cũ sang cấu trúc chuẩn mới.
- Hiển thị responsive tối ưu trên cả màn hình điện thoại và máy tính.

### 4. 🖼️ Znews Thumb Định Dạng Đặc Biệt
*File: `Znews_Thumb_dinh_dang_dac_biet.html`*
- Tạo ảnh đại diện (Thumbnail) chuẩn kích thước xuất JPG **900 × 600 px**.
- Kho logo định dạng chính thức của Znews: *Photo Essay, Magazine, Minimag, Longform, Special...*
- Công cụ cắt cúp (crop), phóng to/thu nhỏ, xoay và điều chỉnh vị trí logo trực quan.
- Tải ngay file JPG chất lượng cao sẵn sàng xuất bản.

### 5. 📚 Trình tạo bài viết sách (CMS Books)
*File: `bai-viet-sach.html` & `Bai viet sach.html`*
- Soạn thảo và dựng bài giới thiệu sách, review tác phẩm hoặc trích đoạn sách.
- Khối thông tin sách chuyên nghiệp: Ảnh bìa đứng/ngang, Tên sách, Tác giả, Nhà xuất bản, Năm phát hành, Tóm tắt nổi bật.
- Tự động thay thế gạch nối em-dash (`—`, `–`) bằng dấu phẩy theo đúng quy chuẩn biên tập Znews.
- Tách biệt CSS với namespace độc lập `.container_AI`.

### 6. 🎞️ Công cụ tạo Carousel ảnh
*File: `carousel-tool.html`*
- Tạo slide trình chiếu ảnh tương tác nhúng gọn gàng trong bài viết.
- Tự do thiết lập tỷ lệ hiển thị: 16:9, 4:3, 3:2, 1:1 hoặc co giãn tự động.
- Hỗ trợ chú thích riêng cho từng ảnh, số trang (1/N) và vuốt cảm ứng mượt mà trên mobile.
- Mã nhúng siêu nhẹ, không cần nạp thêm thư viện bên ngoài.

### 7. 📖 Cẩm nang Quy chuẩn Kỹ thuật CMS (Ad-Safe)
*File: `guide.html` & `huong-dan-bai-dac-biet-znews-2.md`*
- Toàn bộ 7 quy tắc kỹ thuật vàng khi dựng bài đặc biệt trên Znews.
- Giải mã lỗi layout-no-sidebar, công thức tính biên tràn lề an toàn (`--img-bleed`).
- Cảnh báo các cạm bẫy đổi màu nền, quy định về font chữ hệ thống và cấu trúc HTML CMS cho phép.

---

## 🌐 Hướng dẫn truy cập từ mọi thiết bị (GitHub Pages)

Trang web được thiết kế để triển khai trực tiếp qua **GitHub Pages**:
1. Đẩy mã nguồn lên kho lưu trữ GitHub (Public hoặc GitHub Pro).
2. Vào **Settings** > **Pages** của Repository.
3. Chọn nguồn xuất bản: `Deploy from a branch` > chọn nhánh `main` (hoặc `master`) > thư mục `/ (root)` > nhấn **Save**.
4. Địa chỉ truy cập trực tuyến:
   `https://<username>.github.io/<tên-repo>/`

---

## 💻 Sử dụng trực tiếp trên máy tính cá nhân

Bạn chỉ cần mở trực tiếp file `index.html` bằng bất kỳ trình duyệt nào (Chrome, Safari, Edge, Firefox) hoặc chạy một server tĩnh nội bộ:

```bash
# Sử dụng Python (có sẵn trên macOS/Linux/Windows)
python3 -m http.server 8080
```
Sau đó truy cập: `http://localhost:8080`

---
*Phát triển chuyên biệt cho Ban Biên tập Znews.*
